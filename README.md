# Uquery
Gamber is an online database of gamer aliases. This here is the code repository for it.
Gamber is used to help players mark down their old usernames and point old friends into the new direction.


# How Uquery Works
Users register an account and then register all their old usernames. These usernames are platform specific, and following platform guidelines, no username can be used twice on a platform. As such, each platform database has usernames specific to them. Its truly first come first serve, so register all your usernames. Players who wish to override another player using their username will soon have the oppertunity to prove their username. 

# REST API DOCUMENTATION
All the REST API Commands and Usage Updated will be stored here. Only the Alias Database Is currently accessable to the public. 
<br>
**Whatever Is In Between the `( >` is the variable that needs to be placed.**

## Open API Endpoints

### Search Platform Database:
POST `/alias/search/(Name)`

### Get public profile info
GET `/account/public/(UID)`

## Authentication Required Endports
#### Create A Profile & Delete A Profile
##### Creating A Profile
When You make a profile, pretty much a user is signed in, and session managed.<br>
POST `/account/create/(Username)/(Password)/(Email)` <br>

##### Updating A Profile
Updates a profile with the presented information<br>
POST `/account/update/(UID)/(Token)/(Username)/(Bio)/(Email)` 
<br>

##### Deleting A Profile
When you delete a profile, it not only deletes the profile, but all aliases associated with the UID. To delete a profile, you need the UID and Token. Just do the following. <br>
DELETE `/account/delete/(UID)/(Password)/(Token)`

##### Resetting a Password
Post here to reset password<br>
POST `/account/forgotpasswords/(Email)` 
<br>
Post here with token to manuel reset without email<br>
POST `/account/updatepw/(UID)/(Token)/(NewPassword)/(RePassword)` 
<br>

***
#### Sign In & Sign Out
Signing In is very important, as majority of database writing privs can only be used when a User is Signed in. 
##### Signing In:
To Sign in, Simply do the following: <br>
POST `/account/login/(Username)/(Password)`<br>
You should get a return that looks like the following: <br>
```json
[
    "000000000000000000",
    "TestingUsername",
    "test@test.com",
    "2022-03-16",
    "Insert Bio Here",
    "Insert Gravatar Here",
    [
        "testtoken",
        "testrefreshtoken"
    ]
]
```
<br>
##### Signing Out:
Signing out is way more simple, just do the following: <br>
DELETE `/account/logout/(UID)/(Token)` <br>
***

#### Aliases
Now comes the fun part, here is how to read and write to the Aliases Database.

##### Writing
To write to an alias database. Note that if someone already owns this username, or the user is not authenticated, then writing, and deleting will not work.

###### Adding and Deleting
To Add an Alias or delete it, Simply post to the following:
POST `/alias/crud/(Platform)/(Name)/(UID)/(Token)`
DELETE `/alias/crud/(Platform)/(Name)/(UID)/(Token)`
<br>

***
### Codes and Error Codes
- EC500: Authentication Errors
- EC501: Username Not Found
- EC502: Incorrect Password
- EC503: Session Management Error
- EC504: User Already Logged In
- EC505: User is not Logged In
- EC506: Internal Error
- EC507: User is Already Registered
- EC508: Email not Found
- EC509: Passwords do not match


- C500: Authentication Success
- C502: Successfully Logged Out
- C503: Successfully Removed Session
- C504: User Successfully Deleted
- C505: User Successfully Registered
- C506: Information Updated
- C507: Temp Password Sent
- C508: New Password is Set

- EC600:
- EC601: Alias is Already Registered
- EC602: PlatformID is invalid
- EC603: Internal Error
- EC604: Alias is not registered
- C600 Alias Success:
- C601: Alias Successfully Registered
- C602: Alias Successfully Deleted
- C603: All Aliases Related To User Have Been Deleted
