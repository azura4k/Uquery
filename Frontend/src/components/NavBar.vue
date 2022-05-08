<template >
  <div class="row" id="wrapper">
    <nav class="navbar navbar-dark align-items-start sidebar sidebar-dark accordion bg-gradient-primary p-2">
      <div class="container-fluid d-flex flex-column p-0"><a
          class="navbar-brand d-flex justify-content-center align-items-center sidebar-brand m-0" href="Search.html">
          <div class="sidebar-brand-icon rotate-n-15"><i class="fas fa-laugh-wink"></i></div>
          <div class="sidebar-brand-text mx-3"><span>Uquery</span></div>
        </a>
        <hr class="sidebar-divider my-0">
        <ul class="navbar-nav text-light" id="accordionSidebar">
          <li class="nav-item">
            <router-link tag="a" class="nav-link" to="/"><i class="fa fa-search"></i><span>Search</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" v-if="LoggedIn" class="nav-link" to="/editprofile">
              <i class="fas fa-user"></i>
              <span>Profile</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" v-if="!LoggedIn" class="nav-link" to="/signin">
              <i class="fas fa-key"></i>
              <span>Sign In</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" v-if="!LoggedIn" class="nav-link" to="/signup">
              <i class="fas fa-clipboard"></i>
              <span>Sign Up</span>
            </router-link>
          </li>
                    <li class="nav-item">
            <a v-if="LoggedIn" @click="SignOut()" class="nav-link" to="/signup">
              <i class="fas fa-clipboard"></i>
              <span>Sign Out</span>
            </a>
          </li>
          <li class="nav-item">
            <router-link tag="a" class="nav-link" to="/about">
              <i class="fas fa-question"></i>
              <span>About</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link tag="a" class="nav-link" to="/legal">
              <i class="fas fa-gavel"></i>
              <span>Legal</span>
            </router-link>
          </li>
        </ul>
        <div class="text-center d-none d-md-inline"><button class="btn rounded-circle border-0" id="sidebarToggle"
            type="button"></button></div>
      </div>
    </nav>
    <div class="d-flex flex-column" id="content-wrapper">
      <div id="content">
        <nav class="navbar navbar-light navbar-expand bg-white shadow mb-4 topbar static-top">
          <div class="container-fluid"><button class="btn btn-link d-md-none rounded-circle mr-3" id="sidebarToggleTop"
              type="button"><i class="fas fa-bars"></i></button>
            <form class="form-inline d-none d-sm-inline-block mr-auto ml-md-3 my-2 my-md-0 mw-100 navbar-search">
              <div class="input-group">
                <input class="bg-light form-control border-0 small" type="text" ref="Query" placeholder="Search for ...">
                <div class="input-group-append"><button @click="getResults()" class="btn btn-primary py-0" type="button"><i
                      class="fas fa-search"></i></button></div>
              </div>
            </form>
            <ul class="navbar-nav flex-nowrap ml-auto">
              <li class="nav-item dropdown d-sm-none no-arrow"><a class="dropdown-toggle nav-link" aria-expanded="false"
                  data-toggle="dropdown" href="#"><i class="fas fa-search"></i></a>
                <div class="dropdown-menu dropdown-menu-right p-3 animated--grow-in" aria-labelledby="searchDropdown">
                  <form class="form-inline mr-auto navbar-search w-100">
                    <div class="input-group"><input class="bg-light form-control border-0 small" type="text"
                        placeholder="Search for ...">
                      <div class="input-group-append"><button class="btn btn-primary py-0" type="button"><i
                            class="fas fa-search"></i></button></div>
                    </div>
                  </form>
                </div>
              </li>
              <li class="nav-item dropdown no-arrow">
                <div class="nav-item dropdown no-arrow"><a class="dropdown-toggle nav-link" aria-expanded="false"
                    data-toggle="dropdown" href="#"><span
                      class="d-none d-lg-inline mr-2 text-gray-600 small">Serengon4k</span><img
                      class="border rounded-circle img-profile" src="assets/img/avatars/avatar1.jpeg"></a>
                  <div class="dropdown-menu shadow dropdown-menu-right animated--grow-in"><a class="dropdown-item"
                      href="#"><i class="fas fa-user fa-sm fa-fw mr-2 text-gray-400"></i>&nbsp;Profile</a><a
                      class="dropdown-item" href="#"><i
                        class="fas fa-cogs fa-sm fa-fw mr-2 text-gray-400"></i>&nbsp;Settings</a><a
                      class="dropdown-item" href="#"><i
                        class="fas fa-list fa-sm fa-fw mr-2 text-gray-400"></i>&nbsp;Activity log</a>
                    <div class="dropdown-divider"></div><a class="dropdown-item" href="#"><i
                        class="fas fa-sign-out-alt fa-sm fa-fw mr-2 text-gray-400"></i>&nbsp;Logout</a>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </nav>
        <div class="container-fluid">
          <!-- <RouterView :key="$route.fullPath" /> -->
        </div>
        <footer class="bg-white sticky-footer">
          <div class="container my-auto">
            <div class="text-center my-auto copyright"><span>Copyright © Azura4k 2022</span></div>
          </div>
        </footer>
      </div>
    </div>
  </div>
</template>


<style>
  @import url("@/assets/fonts/fontawesome5-overrides.min.css");
  @import url("@/assets/css/bootstrap.min.css");
  @import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css");
  @import url("https://use.fontawesome.com/releases/v5.12.0/css/all.css");

  #sidemenu {
    margin: 0px;
  }

  #wrapper {
    flex-wrap: nowrap;
  }

  .col {
    margin: 0px;
  }

  body {
    height: 100vh;
    overflow-x: hidden;
    max-width: 100vw;
  }
</style>

<script>
export default {
    name: 'Navbar',
    methods: {
      getResults() {
        const Name = this.$refs.Query.value;
        this.$router.push({path: '/results', name: 'results', params:{UsernameSearched: Name}})
      },
      SignOut(){
        this.$cookies.remove("UID")
        this.$cookies.remove("Username")
        this.$cookies.remove("RefreshToken")
        this.$cookies.remove("CreationDate")
        this.$cookies.remove("Token")
        this.$cookies.remove("Email")
        this.$cookies.remove("Gravatar")
        this.LoggedIn = false;
        this.$router.go(0)
      }
    },
    data(){
      return {
          LoggedIn: Boolean()
      }
    },
    mounted() {
      (function ($) {
        "use strict"; // Start of use strict
        // Toggle the side navigation
        $("#sidebarToggle, #sidebarToggleTop").on('click', function (e) {
          $("body").toggleClass("sidebar-toggled");
          $(".sidebar").toggleClass("toggled");
          if ($(".sidebar").hasClass("toggled")) {
            $('.sidebar .collapse').collapse('hide');
          };
        });

        $(window).load(function () {
          if ($(window).width() < 768) {
            $('.sidebar').toggleClass('hide');
          }
        });

        // Close any open menu accordions when window is resized below 768px
        $(window).resize(function () {
          if ($(window).width() < 768) {
            $('.sidebar .collapse').collapse('hide');
          };
        });

        // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
        $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function (e) {
          if ($(window).width() > 768) {
            var e0 = e.originalEvent,
              delta = e0.wheelDelta || -e0.detail;
            this.scrollTop += (delta < 0 ? 1 : -1) * 30;
            e.preventDefault();
          }
        });

        // Scroll to top button appear
        $(document).on('scroll', function () {
          var scrollDistance = $(this).scrollTop();
          if (scrollDistance > 100) {
            $('.scroll-to-top').fadeIn();
          } else {
            $('.scroll-to-top').fadeOut();
          }
        });

        // Smooth scrolling using jQuery easing
        $(document).on('click', 'a.scroll-to-top', function (e) {
          var $anchor = $(this);
          $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top)
          }, 1000, 'easeInOutExpo');
          e.preventDefault();
        });

      })(jQuery); // End of use strict
      

      if (this.$cookies.isKey("Token")){
          this.LoggedIn = true;
      }
      else{
        this.LoggedIn = false;
      }
    }
}
</script>
