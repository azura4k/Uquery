# Copyright Devin B (Azura4k) 2022. All Rights Reserved.
from ast import Pass
from curses.ascii import EM
from flask import Flask
from flask_restful import Resource, Api
from flask_mail import Mail, Message
from flask_cors import CORS
import secrets
from mysql.connector import (connection)
import os
from difflib import SequenceMatcher
import atexit
from datetime import date
from libgravatar import Gravatar
import bcrypt




#Backend API
class Backend():
    def __init__(self, config):
        self.Sessions = dict()
        self.Data = connection.MySQLConnection(**config)
        try:
            self.Data.connect()
        except Exception as err:
            print(err)
        self.Query = self.Data.cursor(buffered=True)
        #Database Setup Tables
        try:
            self.WriteCommand("CREATE TABLE Users (UID VARCHAR(50) NOT NULL UNIQUE,Username TEXT NOT NULL UNIQUE, Password TEXT NOT NULL, Email	TEXT NOT NULL UNIQUE, DateJoined TEXT NOT NULL, Bio TEXT NOT NULL, GravatarPfP TEXT NOT NULL, PRIMARY KEY(UID));")
        except Exception as e :
            print(e)
        try:
            self.WriteCommand("CREATE TABLE Sessions (Token	VARCHAR(50) NOT NULL UNIQUE, UID VARCHAR(50) NOT NULL UNIQUE, RefreshToken VARCHAR(50) NOT NULL UNIQUE,SessionStartTime TEXT NOT NULL, PRIMARY KEY(UID));")
        except Exception as e :
            print(e)
        try:
            self.WriteCommand("CREATE TABLE Aliases (Name TEXT NOT NULL, Platform TEXT NOT NULL, RegisteredDate	TEXT NOT NULL, OwnerUID VARCHAR(50) NOT NULL, RegistrationID VARCHAR(100) NOT NULL, PRIMARY KEY(RegistrationID) );")
        except Exception as e :
            print(e)

    #Adding and Removing Aliases
    def AddAlias(self, Platform, Name, UID, Token):
        Platform = str(Platform)
        if self.IsActiveSession(UID,Token):
            if not self.AliasExistsAlready(Name, Platform):
                try:
                    self.WriteCommand(f"INSERT INTO `Aliases` (`Name`, `Platform`, `RegisteredDate`, `OwnerUID`, `RegistrationID`) VALUES ('{Name}', '{Platform}', '{self.GetDateTime()}', '{UID}', '{self.UidGen()}');")
                    return "C601"
                except Exception as e:
                    print(e)
                    return str(e)
            else:
                return "EC601"
        else:
            return "EC505"
    def RemoveAlias(self, Platform, Name, UID, Token):
        Platform = str(Platform)
        if self.IsActiveSession(UID, Token):
            if self.AliasExistsAlready(Name, Platform):
                try:
                    self.WriteCommand(f"DELETE FROM `Aliases` WHERE `Name`='{Name}' AND `Platform`='{Platform}' AND `OwnerUID`='{UID}';")
                    return "C602"
                except Exception as e:
                    print(e)
                    return "EC603"
            else:
                return "EC604"
        else:
            return "EC505"
    def RemoveAllAliases(self, UID, Token):
        if self.IsActiveSession(UID, Token):
            try:
                self.WriteCommand(f"DELETE FROM `Aliases` WHERE `Aliases`.`OwnerUID`='{UID}'")
                return "C603"
            except Exception as e:
                print(e)
                return "EC603"
        else:
            return "EC505"
    def AliasExistsAlready(self, Alias, Platform):
        Platform = str(Platform)
        self.Query.execute(f"SELECT * FROM `Aliases` WHERE EXISTS (SELECT * FROM `Aliases` WHERE `Aliases`.`Name`='{Alias}' AND `Aliases`.`Platform`='{Platform}')")
        if self.Query.fetchone() is not None:
            return True
        else:
            return False
    def GetUserAliases(self, OwnerUID):
        self.Query.execute(f"SELECT `Name`, `Platform` FROM `Aliases` WHERE `OwnerUID`='{str(OwnerUID)}';")
        return self.Query.fetchall()
    # Search Command
    def SearchPlatform(self, UsernameSearched):
        UsernameSearched = str(UsernameSearched).lower()
        try:
            self.Query.execute("Select * From Aliases")
            Aliases = self.Query.fetchall()
            SearchResults = list()
            for Alias in Aliases:
                Alias = list(Alias)
                if str(Alias[0]).lower().startswith(UsernameSearched[:2]):
                    Alias.append(round(SequenceMatcher(None, UsernameSearched, str(Alias[0]).lower()).ratio() * 100))
                    Alias.append(self.GetUserAliases(Alias[3]))
                    SearchResults.append(Alias)
                        
                #Sort Results by Percentage Decending before returning 
            SearchResults = sorted(SearchResults, key=lambda x: x[4], reverse=True)
            return SearchResults        
        except Exception as E:
            print(E)
            return "EC603"

    #User creation and deletion
    def CreateUser(self, Username, Password, Email, Bio,):
        #TODO ADD VALUE DETECTORS, FE EMAIL IS EMAIL AND PASSWORD IS A PASSWORD
        try:
            G = Gravatar(Email)
            self.WriteCommand(f"INSERT INTO `Users` (`UID`, `Username`, `Password`, `Email`, `DateJoined`, `Bio`, `GravatarPfP`) VALUES ('{self.UidGen()}', '{Username}', '{Password}', '{Email}', '{self.GetDateTime()}', '{Bio}', '{G.get_image()}');")
            return "C505"
        except Exception as e:
            print(e)
            if str(e).startswith("Duplicate"):
                return "EC507"
            else:
                return "EC506"
    def DeleteUser(self, UID, Password, Token):
        UID = str(UID)
        Token = str(Token)
        Password = str(Password)
        if self.IsActiveSession(UID, Token):
            try:    
                #Fetch Profile
                self.Query.execute(f"SELECT * FROM `Users` WHERE `Users`.`UID`='{UID}'")
                data = self.Query.fetchall()
                # If data is not None
                if data is not None :
                    #Test Password
                    if data[0][2] == Password:
                        self.WriteCommand(f"DELETE FROM `Users` WHERE `Users`.`UID`='{UID}';")
                        self.RemoveAllAliases(UID, Token)
                        self.Logout(UID)
                        return "C504"
                    else:
                        return "EC502"
            except Exception as e:
                print(e)
                return "EC506"
        else:
            return "EC505"
    def Login(self, Username, Password):
        try:
            #String Variables
            Username = str(Username)
            Password = str(Password)

            #Fetch Profile
            self.Query.execute(f"SELECT * FROM Users WHERE Username='{Username}'")
            data = self.Query.fetchall() 
            data = list(data) 
            # If data is not None
            if data is not None :
                #Test Password
                if data[0][2] == Password:
                    #Add Session Data 
                    SessionData = self.AddSession(data[0][0])
                    filteredData = list(data[0][:2] + data[0][3:])
                    filteredData.append(SessionData)
                    return filteredData

                #Return Incorrect Password
                else:
                    return "EC502"
            #Return Incorrect Username
            else :
                return "EC501"
        except Exception as e:
            print(e)
            if str(e).startswith("list index"):
                return "EC501"
            return "EC506"
    def Logout(self, UID):
        if self.PrivIsActiveSession(UID):
            if self.RemoveSession(UID) == "C504":
                return "C504"
            else:
                return "EC503"
        else:
            return "EC505"         
    def GetProfileInfo(self, UID):
        self.Query.execute(f"SELECT Username,UID,GravatarPfP,Bio FROM Users WHERE UID='{UID}'")
        Data = self.Query.fetchall()
        Data.append(self.GetUserAliases(UID))
        return Data
    def ForgotPassword(self, Email):
        TempPassword = secrets.token_urlsafe(9)    
        if self.UserExists(Email):
            try:
                msg = Message()
                msg.add_recipient(str(Email))
                msg.subject = "Lost Password Overrrr Here"
                msg.body = f"Hello user designated at {Email}, we heard you lost your password, so we emailed you a temp password so you can change it yourself. This password expires in 30 minutes, so do it quick. Thank you. Your Password is: {TempPassword}"
                msg.sender = "no-reply@uquery.azura4k.com"
                mail.send(msg)
                try: 
                    self.SetTempPassword(Email, TempPassword) == "C507"
                    print(TempPassword)
                    return "C507"
                except:
                    return "EC506"
            except Exception as e:
                print(e)
                return "EC506"
        else:
            return "EC508"
    def UserExists(self, Email):
        self.Query.execute(f"SELECT * FROM Users WHERE EXISTS (SELECT * FROM Users WHERE Email='{Email}');")
        if self.Query.fetchone() is not None:
            return True
        else:
            return False
    def UpdateUserInfo(self, UID, Token, Username, Email, Bio):
        if self.IsActiveSession(UID, Token):
            G = Gravatar(Email)
            try:
                self.WriteCommand(f"UPDATE Users SET `Username`='{Username}', `Email`='{Email}', `Bio`='{Bio}', `GravatarPfP`='{G.get_image()}' WHERE `Users`.`UID`='{UID}';")
                return "C506"
            except Exception as e:
                print(e)
                return "EC506"
        else:
            return "EC505"
    def UpdatePassword(self, UID, Token, NewPassword):
        if self.IsActiveSession(UID, Token):
            try:
                NewPassword = self.HashPassword(NewPassword)
                self.Query.execute(f"Select `Email` From `Users` Where `Users`.`UID`='{UID}';")
                Email = str(self.Query.fetchone())
                Email = Email.replace("(", "")
                Email = Email.replace(")", "")
                Email = Email.replace("'", "")
                msg = Message()
                msg.add_recipient(Email)
                msg.subject = "Hey, Hey, Did you reset your password?"
                msg.body = f"Hello user designated at {Email}, We got word you decided to reset your password, so we sent you this email to tell you. Just on the off chance you did not. If you did, ignore this and delete it, if you didnt, oh boy. If you did not reset your password, please go click forgot password immediately to keep your account and your aliases secure. Hurry!!!!!!! "
                msg.sender = "no-reply@uquery.azura4k.com"
                mail.send(msg)
                self.WriteCommand(f"UPDATE Users SET `Password`='{NewPassword}' WHERE `Users`.`UID`='{UID}';")
                return "C508"
            except Exception as e:
                return "EC506"
        else:
            return "EC505"
    #Tools and Security
    def UidGen(self):
        Token = secrets.token_urlsafe(16)
        Token = Token.replace("_", "")
        Token = Token.replace("-", "")
        return Token
    def GetDateTime(self):
        return str(date.today())
    def AddSession(self, UID):
        #Stringify and Generate Variables
        UID = str(UID)
        Token = secrets.token_urlsafe(20)
        Token = Token.replace("_", "")
        Token = Token.replace("-", "")
        RefreshToken = secrets.token_urlsafe(25)
        #Attempt to Write new Session into Sessions
        try:
            self.WriteCommand(f"INSERT INTO Sessions (Token, UID, RefreshToken, SessionStartTime) VALUES ('{Token}', '{UID}', '{RefreshToken}', '{self.GetDateTime()}');")
            return [Token, RefreshToken]
        except Exception as e:
            self.WriteCommand(f"UPDATE Sessions SET `Token`='{Token}', `RefreshToken`='{RefreshToken}', `SessionStartTime`='{self.GetDateTime()}' WHERE `UID`='{UID}' ;")
            return [Token, RefreshToken]
    def RemoveSession(self, UID):
        try:
            self.WriteCommand(f"DELETE FROM `Sessions` WHERE `Sessions`.`UID`='{UID}';")
            return "C504"
        except Exception as e:
            print(e)
            return "EC503"
    def IsActiveSession(self, UID, Token):
        self.Query.execute(f"SELECT * FROM `Sessions` WHERE EXISTS (SELECT * FROM Sessions WHERE `UID`='{UID}' AND `Token`='{Token}')")
        if self.Query.fetchone() is not None:
            return True
        else:
            return False
    def PrivIsActiveSession(self, UID):
        self.Query.execute(f"SELECT * FROM `Sessions` WHERE EXISTS (SELECT * FROM Sessions WHERE `UID`='{UID}')")
        if self.Query.fetchone() is not None:
            return True
        else:
            return False   
    def SetTempPassword(self, Email, TempPassword):
        try:
            self.WriteCommand(f"UPDATE Users SET Password='{TempPassword}' WHERE Email='{Email}'")
            return "C507"
        except Exception as e:
            print(e)
            return "EC506"
    def HashPassword(self, Password):
        return bcrypt.hashpw(str(Password), bcrypt.gensalt())
    def IsMatchingPassword(self, PasswordToCheck, HashedPassword):
        return bcrypt.checkpw(str(PasswordToCheck), HashedPassword)

    def WriteCommand(self, Command):
        Command = str(Command)
        self.Query.execute(Command)
        #self.Data.backup(self.Data)
        self.Data.commit()         
    def ShutdownAPI(self):
        #TODO Remove all Sessions 
        print("API Shutdown Protical Initiated")
        self.WriteCommand("DELETE FROM SESSIONS")
        print("All Sessions Logged Out")
        self.Data.commit()
        print("Database Edits have been Commited")
        self.Data.close()
        print("API Shutdown Protical Compleated")

#--------------------------------------------------
#API STUFF
# Initialization
app = Flask("Uquery")
app.secret_key = secrets.token_urlsafe(24)
api = Api(app)
CORS(app)
app.config['MAIL_SERVER']= os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = bool(os.getenv('MAIL_USE_TLS'))
app.config['MAIL_USE_SSL'] = bool(os.getenv('MAIL_USE_SSL'))

dbconfig = {
  'user': os.getenv('user'),
  'password': os.getenv('password'),
  'host': os.getenv('host'),
  'database': os.getenv('database'),
  'raise_on_warnings': bool(os.getenv('raise_on_warnings'))
}
mail = Mail(app)
# Calling Class so its not called and reloaded every time
B = Backend(dbconfig)



class Default(Resource):
    def get(self):
        # Make Website Return
        return {'hello': 'world'}

#User Functions
class CreateUser(Resource):
    def post(self, Username, Password, Email):
        return B.CreateUser(Username, Password, Email, "You can Put a Bio Here")

class UpdateUser(Resource):
    def post(self, UID, Token, Username, Bio, Email):
        return B.UpdateUserInfo(UID, Token, Username, Email, Bio)

class DeleteUser(Resource):
    def delete(self, UID, Password, Token):
        return B.DeleteUser(UID, Password, Token)
class Login(Resource):
    def post(self, Username, Password):
        return B.Login(Username, Password)
class Logout(Resource):
    def delete(self, UID):
        return B.Logout(UID)
class GetPublicUserInfo(Resource):
    def get(self, UID):
        return B.GetProfileInfo(str(UID))
#TODO PASSWORD AND EMAIL RESET
class PasswordReset(Resource):
    def post(self, Email):
        return B.ForgotPassword(Email)

class UpdatePassword(Resource):
    def post(self, UID, Token, NewPassword, RePassword ):
        if NewPassword == RePassword:
            return B.UpdatePassword(UID, Token, NewPassword) 
        else:
            return "EC509"

#Alias Stuff
class Alias(Resource):
    def post(self, Platform, Name, UID, Token):
        return B.AddAlias(Platform, Name, UID, Token)
    def delete(self, Platform, Name, UID, Token):
        return B.RemoveAlias(Platform, Name, UID, Token)

class Search(Resource):
    def post(self, Name):
        return B.SearchPlatform(Name)

#Default Resource, Return Page
api.add_resource(Default, '/')
#Account Features
api.add_resource(CreateUser, '/account/create/?Username=<Username>&Password=<Email>&Email=<Email>')
api.add_resource(DeleteUser, 'account/delete/?UID=<UID>&Token=<Token>')
api.add_resource(Login, '/account/login/<Username>/<Password>')
api.add_resource(Logout, '/account/logout/<UID>')
api.add_resource(GetPublicUserInfo, '/account/public/<UID>')
api.add_resource(UpdateUser, '/account/update/<UID>/<Token>/<Username>/<Bio>/<Email>')
api.add_resource(UpdatePassword, '/account/updatepw/<UID>/<Token>/<NewPassword>/<RePassword>')
api.add_resource(PasswordReset, '/account/forgotpasswords/<Email>')
api.add_resource(Alias, '/alias/crud/<Platform>/<Name>/<UID>/<Token>')
api.add_resource(Search, '/alias/search/<Name>')

def OnExit():
    B.ShutdownAPI()

atexit.register(OnExit)
def main():
    app.run(
        host='0.0.0.0', 
        debug=False, 
        port=int(os.environ.get('PORT', 5000))
    )
main()
