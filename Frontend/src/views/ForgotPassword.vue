<template>
 <div class="container-fluid">
    <div class="card shadow mb-3">
        <div class="card-header py-3">
            <p class="text-primary m-0 font-weight-bold">Forgot Password</p>
        </div>
        <div class="card-body">
            <form>
                <input class="form-control" ref="email" type="email" placeholder="Enter your Email"
                    style="resize: none;margin-bottom: 15px;"/>
                <div class="form-group"><button class="btn btn-primary btn-sm" type="button"
                        @click="SendPassword()">Reset Password</button></div>
            </form>
        </div>
    </div>
</div>
</template>
<script>
import axios from 'axios'
    export default {
        name: 'forgotpassword',
        methods: {
            SendPassword(){
                const email = this.$refs.email.value;
                if (String(email).length >= 4 && String(email).includes("@")){
                    const url = "https://uquery-azura4k.herokuapp.com/account/forgotpasswords/" + email
                    axios.post(url).then((response) => {
                        console.log(response.data)
                        if (response.data == "EC508"){
                            alert("No User Found")
                        }
                        if (response.data == "EC506"){
                            alert("Internal Error, Try Again. If it doesnt work, contact admins.")
                        }
                        if (response.data == "C507"){
                            alert("Email Sent ->")
                            this.$router.push({path:'/signin', name:'signin'})
                        }
                        
                    })
                }
                else {
                    alert("No Valid Email Sent")
                }
            }
        }
    }
</script>