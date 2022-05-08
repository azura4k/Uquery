<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-9 col-lg-12 col-xl-10">
                <div class="card shadow-lg o-hidden border-0 my-5">
                    <div class="card-body p-0">
                        <div class="row">
                            <div class="col-lg-6 d-none d-lg-flex">
                                <div class="flex-grow-1 bg-login-image"
                                    style="background-image: url('https://images.pexels.com/photos/220201/pexels-photo-220201.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2');"></div>
                            </div>
                            <div class="col-lg-6">
                                <div class="p-5">
                                    <div class="text-center">
                                        <h4 class="text-dark mb-4">Welcome Back!</h4>
                                    </div>
                                    <form class="user">
                                        <div class="form-group"><input class="form-control form-control-user"
                                                type="name" aria-describedby="Username" ref="Username"
                                                placeholder="Enter Username" name="username"></div>
                                        <div class="form-group"><input ref="Password" class="form-control form-control-user"
                                                type="password" id="exampleInputPassword" placeholder="Password"
                                                name="password"></div><button
                                            class="btn btn-primary btn-block text-white btn-user"
                                            type="button" @click="login()">Login</button>
                                        <hr>
                                    </form>
                                    <div class="text-center"><router-link tag="a" class="small" to="forgotpassword">Forgot Password?</router-link></div>
                                    <div class="text-center"><router-link tag="a" class="small" to="signup">Create an Account!</router-link></div>
                                </div>
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
    name:'signin',
    methods : {
        login(){
            const Username = this.$refs.Username.value;
            const Password = this.$refs.Password.value;
            
            if (String(Username).length >= 5 && String(Password).length >= 5){
                const url = "https://uquery-azura4k.herokuapp.com/account/login/"
                + Username
                + "/"
                + Password;
                axios.post(url).then((response) => {
                    if(response.data == "EC500"){}
                    else if(response.data == "EC500"){alert("Authentication Error")}
                    else if(response.data == "EC501"){alert("Username Not Found")}
                    else if(response.data == "EC502"){alert("Incorrect Password")}
                    else if(response.data == "EC503"){alert("Session Management Error")}
                    else if(response.data == "EC504"){alert("User Already Logged In")}
                    else if(response.data == "EC506"){alert("Internal Error")}
                    else {
                        const data = response.data
                        this.$cookies.set("UID", data[0])
                        this.$cookies.set("Username", data[1])
                        this.$cookies.set("Email", data[2])
                        this.$cookies.set("CreationDate", data[3])
                        this.$cookies.set("Gravatar", data[5])
                        this.$cookies.set("Token", data[6][0])
                        this.$cookies.set("RefreshToken", data[6][1])
                        this.$emit('UserLoggedIn')
                        this.$router.push({path: "/editprofile", name: "editprofile"})

                    } 
                })
            }
            else{
                alert("Your Username or Password is not long enough")
            }

        }
    }
}
</script>