<template>
    <div class="container-fluid">
        <h3 class="text-dark mb-4 row">Search Results</h3>
        <div id="ResultsTable" class="card shadow col-10">
            <div class="card-header py-3">
                <p class="text-primary m-0 font-weight-bold">Results of Search for: {{UsernameSearched}}</p>
            </div>
            <div class="card-body">
                <div class="table-responsive table mt-2" id="dataTable" role="grid" aria-describedby="dataTable_info">
                    <table class="table my-0" id="dataTable">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Platform</th>
                                <th>Match %</th>
                                <th>Registration Date</th>
                                <th>View Profile</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="result" v-for="Result in this.Results">
                                <td>{{Result[0]}}</td>
                                <td>{{Result[1]}}</td>
                                <td>{{Result[5]}}</td>
                                <td>{{Result[2]}}</td>
                                <td>
                                    <button class="btn" @click="ViewProfile(Result[3])"><i
                                            class="fa fa-chevron-right"></i><i class="fa fa-chevron-right"></i></button>
                                </td>
                            </tr>
                        </tbody>
                        <tfoot>
                            <tr></tr>
                        </tfoot>
                    </table>
                </div>
            </div>
        </div>
        <div class=" col-2">
            <Adsense data-ad-client="ca-pub-7523622703086767" data-ad-slot="3157675441" data-ad-format="auto"></Adsense>
        </div>
    </div>
</template>

<style scoped>
    #dataTable{
        overflow-x: hidden;
    }
</style>

<script>
    import axios from 'axios';
    export default {
        name: 'results',
        props: ['UsernameSearched'],
        data() {
            return {
                Results: []
            }
        },
        created() {
            var URL = 'https://uquery-azura4k.herokuapp.com/alias/search/' + this.UsernameSearched;
            axios.post(URL)
                .then((response) => {

                    this.Results = response.data

                })
                .catch((error) => {
                    console.log(error)
                })
        },
        methods: {
            ViewProfile(Uid) {
                this.$router.push({
                    path: '/viewprofile/:UID',
                    name: 'viewprofile',
                    params: {
                        UID: Uid
                    }
                })
            }
        }
    }
</script>