<template>
    <div class="container">
        <div class="card shadow-lg o-hidden border-0 my-5">
            <div class="card-body p-0">
                <div class="row">
                    <div class="col-lg-5 d-none d-lg-flex">
                        <div class="flex-grow-1 bg-register-image"
                            style="background-image: url(https://images.pexels.com/photos/586056/pexels-photo-586056.jpeg?cs=srgb&dl=pexels-spacex-586056.jpg&fm=jpg);"></div>
                    </div>
                    <div class="col-lg-7">
                        <div class="p-5">
                            <div class="text-center">
                                <h4 class="text-dark mb-4">Create an Account!</h4>
                            </div>
                            <form class="user">
                                <div class="form-group">
                                    <input class="form-control form-control-user" ref="Username" type="text"
                                        aria-describedby="emailHelp" placeholder="Username" name="username"></div>
                                <div class="form-group">
                                    <input class="form-control form-control-user" ref="Email" type="email"
                                        aria-describedby="emailHelp" placeholder="Email Address" name="email"></div>
                                <div class="form-group row">
                                    <div class="col-sm-6 mb-3 mb-sm-0">
                                        <input class="form-control form-control-user" ref="Password"
                                            type="password" placeholder="Password" name="password"></div>
                                    <div class="col-sm-6">
                                        <input class="form-control form-control-user" type="password" ref="RePassword"
                                            id="exampleRepeatPasswordInput" placeholder="Repeat Password"
                                            name="password_repeat"></div>
                                </div><button class="btn btn-primary btn-block text-white btn-user"
                                    type="button" @click="SignUpButton()">Register Account</button>
                                <hr>
                                <hr>
                            </form>
                                <div class="text-center"><router-link tag="a" class="small" to="forgotpassword">Forgot Password?</router-link></div>
                                <div class="text-center"><router-link tag="a" class="small" to="signin">Already got one, Login !</router-link></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from "axios";
    export default ({
        name: 'signup',
        methods: {
            SignUpButton() {
                const username = this.$refs.Username.value;
                const email = this.$refs.Email.value;
                const password = this.$refs.Password.value;
                const rePassword = this.$refs.RePassword.value;
                if (password == rePassword){
                    if (String(password).length >= 8 && String(username).length >= 5){
                        if (String(email).includes("@")){
                            const url = "https://uquery-azura4k.herokuapp.com/account/create/"
                            + username 
                            + "/"  
                            + password
                            + "/" 
                            + email;
                            axios.post(url).then((response) => {
                                if (response.data == "EC507"){
                                    alert("Email is in use")
                                }
                                else if (response.data == "EC506"){
                                    alert("Internal Error")
                                }
                                else if (response.data == "C505"){
                                    this.$router.push({path: '/signin/', name: 'signin'})
                                }
                            })
                        }
                        else{
                            alert("Please Enter a proper email address")
                        }
                    }
                    else {
                        alert("Your password or username is not long enough. 5 Characters or more.")
                    }
                }
                else{
                    alert("Passwords are not matching.")
                }
            }
        }
    })
</script>