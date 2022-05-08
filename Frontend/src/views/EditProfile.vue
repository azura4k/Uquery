<template>
    <div class="container-fluid">
                    <h3 class="text-dark mb-4">Edit Profile</h3>
                    <div class="row mb-3">
                        <div class="col-lg-4">
                            <div class="card mb-3">
                                <div class="card-body text-center shadow"><img class="rounded-circle mb-3 mt-4" :src="this.GravatarLink" width="160" height="160"></div>
                            </div>
                        </div>
                        <div class="col-lg-8">
                            <div class="row">
                                <div class="col">
                                    <div class="card shadow mb-3">
                                        <div class="card-header py-3">
                                            <p class="text-primary m-0 font-weight-bold">User Settings</p>
                                        </div>
                                        <div class="card-body">
                                            <form>
                                                <div class="form-row">
                                                    <div class="col">
                                                        <div class="form-group">
                                                            <label for="username"><strong>Username</strong></label>
                                                            <input class="form-control" type="text" ref="username" placeholder="Username" name="username" :value="this.Username">
                                                        </div>
                                                    </div>
                                                    <div class="col">
                                                        <div class="form-group">
                                                            <label for="email"><strong>Email Address</strong></label>
                                                            <input class="form-control" type="email" ref="email" placeholder="Enter an Email" name="email" :value="this.Email"></div>
                                                    </div>
                                                </div>
                                                <div class="form-row">
                                                    <div class="col">
                                                        <div class="form-group"><label for="first_name">
                                                            <strong>New Password</strong><br></label>
                                                            <input class="form-control" type="password" ref="password" placeholder="Password" name="password"></div>
                                                    </div>
                                                    <div class="col">
                                                        <div class="form-group">
                                                            <label for="last_name"><strong>Re-Enter Password</strong></label>
                                                            <input class="form-control" type="password" ref="repassword" placeholder="password" name="password"></div>
                                                    </div>
                                                </div>
                                                <div class="form-group"><button class="btn btn-primary btn-sm" type="button" @click="SaveUserInfo()">Save Settings</button></div>
                                            </form>
                                        </div>
                                    </div>
                                    <div class="card shadow mb-3">
                                        <div class="card-header py-3">
                                            <p class="text-primary m-0 font-weight-bold">Bio</p>
                                        </div>
                                        <div class="card-body">
                                            <form>
                                                <textarea class="form-control" ref="bio" placeholder="Enter your Bio Here" style="resize: none;margin-bottom: 15px;"></textarea>
                                                <div class="form-group"><button class="btn btn-primary btn-sm" type="button" @click="SaveUserInfo()">Save Settings</button></div>
                                            </form>
                                        </div>
                                    </div>
                                    <div class="card shadow">
                                        <div class="card-header py-3">
                                            <p class="text-primary m-0 font-weight-bold">Aliases</p>
                                        </div>
                                        <div class="card-body">
                                            <form>
                                                <div class="form-group">
                                                    <div class="table-responsive">
                                                        <table class="table">
                                                            <thead>
                                                                <tr>
                                                                    <th>Username</th>
                                                                    <th>Platform</th>
                                                                    <th>Delete</th>
                                                                </tr>
                                                            </thead>
                                                            <tbody>
                                                                <tr v-for="Alias in this.Aliases">
                                                                    <td>{{Alias[0]}}</td>
                                                                    <td>{{Alias[1]}}</td>
                                                                    <td><button class="btn btn-primary" type="button" style="background: var(--red);" @click="RemoveAlias(Alias[0],Alias[1])">X</button></td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </div>
                                                </div>
                                                <div class="form-row">
                                                    <div class="col">
                                                        <div class="form-group"><label for="city"><strong>Username</strong></label><input class="form-control" type="text" ref="aliasname" placeholder="Your Username" name="aliasname"></div>
                                                    </div>
                                                    <div class="col">
                                                        <div class="form-group"><label for="country"><strong>Platform</strong></label>
                                                        <select class="form-control" ref="platform">
                                                                <option value="Playstation">Playstation</option>
                                                                <option value="Xbox">Xbox</option>
                                                                <option value="Steam">Steam</option>
                                                                <option value="Nintendo">Nintendo</option>
                                                                <option value="Instagram">Instagram</option>
                                                                <option value="Snapchat">Snapchat</option>
                                                                <option value="Twitter">Twitter</option>
                                                                <option value="TikTok">TikTok</option>
                                                                <option value="Tumblr">Tumblr</option>
                                                                <option value="DeviantArt">DeviantArt</option>
                                                                <option value="Reddit">Reddit</option>
                                                                <option value="Discord">Discord</option>
                                                        </select></div>
                                                    </div>
                                                </div>
                                                <div class="form-group"><button class="btn btn-primary btn-sm" type="button" @click="AddAlias()">Add Alias</button></div>
                                            </form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
</template>
<script>
import axios from "axios"
export default {
    name: "editprofile",
    data(){
        return {
            Username : String(),
            Email : String(),
            GravatarLink : String(),
            Bio : String(),
            CreationDate : String(),
            Aliases: Array()
        }
    },
    methods: {
        SaveUserInfo(){
            const Username = this.$refs.username.value;
            const Email = this.$refs.email.value;
            const NewBio = this.$refs.bio.value;
            const Password = this.$refs.password.value;
            const RePassword = this.$refs.repassword.value;
            
            if (Email != this.Email || Username != this.Username || NewBio != this.Bio){
                const url = "https://uquery-azura4k.herokuapp.com/account/update/" 
                + this.$cookies.get("UID")
                + "/"
                + this.$cookies.get("Token")
                + "/"
                + Username 
                + "/"
                + NewBio
                + "/"
                + Email;

                axios.post(url).then((response) =>{
                    if (response.data == "C506"){
                        alert("Information Updated :)")
                        this.$router.go(0)
                    }
                    else if(response.data == "EC506"){
                        alert("Internal Error occured. Try again later")
                    }
                    else if (response.data == "EC505") {
                        alert("Your not authenticated, go login please. How did you even get here?.")
                    }
                })
                
            }
            if (String(Password).length > 0 ){

                if (String(Password).length >= 8){
                    const url = "https://uquery-azura4k.herokuapp.com/account/updatepw/" 
                    + this.$cookies.get("UID")
                    + "/"
                    + this.$cookies.get("Token")
                    + "/"
                    + Password 
                    + "/"
                    + RePassword

                    axios.post(url).then((response) => {
                        if (response.data == "C508"){
                            alert("New Password Set :)")
                            this.$router.go(0)
                        }
                        else if (response.data == "EC509"){alert("Oh no, your passwords dont match. Reenter and try again")}
                        else if (response.data == "EC506") {alert("An error server side. Please contact an admin or seek help.")}
                    })
                }
                else{alert("Password is not long enough. 8 Characters or more")}
            }
        },
        AddAlias(){
            const Name = this.$refs.aliasname.value;
            const Platform = this.$refs.platform.value;
            const url = "https://uquery-azura4k.herokuapp.com/alias/crud/"
            + Platform
            + "/"
            + Name
            + "/"
            + this.$cookies.get("UID")
            + "/"
            + this.$cookies.get("Token")
            axios.post(url).then((response) => {
                if (response.data == "C601"){
                    alert("Successfully Added")
                    this.$router.go(0)
                }
                else if (response.data == "EC601"){
                    alert("Alias is already registered")
                }
                else if (response.data == "EC505") {
                    alert("User is not logged in")
                }
                else if (response.data == "EC506" || response.data == "EC503" || response.data == "EC603") {
                    alert("Internal Error, Try again later")
                }
                
            })
        },
        RemoveAlias(Name, Platform){
            const url = "https://uquery-azura4k.herokuapp.com/alias/crud/"
            + Platform
            + "/"
            + Name
            + "/"
            + this.$cookies.get("UID")
            + "/"
            + this.$cookies.get("Token")
            axios.delete(url).then((response) => {
                if (response.data == "C602"){
                    alert("Successfully Deleted Alias: " + Name)
                    this.$router.go(0)
                }
                else if (response.data == "EC505") {
                    alert("User is not logged in")
                }
                else if (response.data == "EC506" || response.data == "EC503" || response.data == "EC603") {
                    alert("Internal Error, Try again later")
                }
                
            })
        }
    },
    created(){
        if (this.$cookies.isKey("Token")){
            const url = "https://uquery-azura4k.herokuapp.com/account/public/" + this.$cookies.get("UID");
            axios.get(url).then((response) => {
                this.Username = response.data[0][0];
                this.Email = this.$cookies.get("Email");
                this.CreationDate = this.$cookies.get("CreationDate");
                this.GravatarLink = response.data[0][2];
                this.Aliases = response.data[1];
                this.Bio = response.data[0][3];
                this.$refs.bio.value = this.Bio;
            })
        }
        else {
            this.$router.push({path:'/signin', name:'signin'})
        }
        
    }
}
</script>