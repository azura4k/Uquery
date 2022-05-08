<template>
    <div class="container-fluid">
        <h3 class="text-dark mb-4">Profile</h3>
        <div class="row mb-3">
            <div class="col-lg-4">
                <div class="card mb-3">
                    <div class="card-body text-center shadow"><img class="rounded-circle mb-3 mt-4" :src="Profile[0][2]" width="160" height="160">
                        <h1>{{Profile[0][0]}}</h1>
                    </div>
                </div>
            </div>
            <div class="col-lg-8">
                <div class="row">
                    <div class="col">
                        <div class="card shadow">
                            <div class="card-header py-3">
                                <p class="text-primary m-0 font-weight-bold">Bio</p>
                            </div>
                            <div class="card-body">
                                <p>{{Profile[0][3]}}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-8">
                <div class="row">
                    <div class="col" style="margin-top: 20px;">
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
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr v-for="Alias in Profile[1]">
                                                        <td>{{Alias[0]}}</td>
                                                        <td>{{Alias[1]}}</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
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
import axios from 'axios';
export default {
    name: 'viewprofile',
    props: ['UID'],
    data(){
        return{
                Profile : []
            }
    },
     created() {
            console.log(this.UID)
            var URL = 'https://uquery-azura4k.herokuapp.com/account/public/' + this.UID;
            axios.get(URL)
            .then((response) => {
                this.Profile = response.data
                console.log(this.Profile)
            })
            .catch((error) => {
                console.log(error)
            })
        }
}
</script>