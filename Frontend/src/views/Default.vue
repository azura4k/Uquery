<template>
  <div class="container-fluid">
    <h3 class="text-dark mb-1">Lets Find Someone</h3>
    <div class="card shadow mb-3">
      <div class="card-header py-3">
        <p class="text-primary m-0 font-weight-bold">User Search</p>
      </div>
      <div class="card-body">
        <form>
          <div class="input-group">
            <input ref="Query" class="bg-light form-control border-0 small" type="text"
              placeholder="Search a name ...">
            <div class="input-group-append"><button @click="getResults()" class="btn btn-primary py-0" type="button"><i
                  class="fas fa-search"></i></button></div>
          </div>
        </form>
      </div>
    </div>
    <Adsense
    data-ad-client="ca-pub-7523622703086767"
    data-ad-slot="2917453557"
    data-ad-format="auto">
    </Adsense>
  </div>
</template>

<script>
export default{
  name: 'Default' ,
  methods : {
      getResults() {
        const Name = this.$refs.Query.value;
        this.$router.push({path: '/results', name: 'results', params:{UsernameSearched: Name}})
      }
  }

}
</script>
