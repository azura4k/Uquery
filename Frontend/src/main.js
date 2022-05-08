import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import BootstrapVue3 from 'bootstrap-vue-3'
import VueCookies from 'vue3-cookies'
import VueGtag from "vue-gtag";
import ScriptX from 'vue-scriptx'
import Ads from 'vue-google-adsense'

import "@/assets/css/bootstrap.min.css"
import "bootstrap"

const app = createApp(App);

app.use(router);
app.use(BootstrapVue3)
app.use(VueCookies, {
    expireTimes: "1d",
    path: "/",
    domain: "https://uquery.azura4k.com",
    secure: true,
})
app.use(VueGtag, {
  config: { id: "G-1XTYZHVZBG" }
})
app.use(ScriptX)
app.use(Ads.Adsense)
app.mount("#app");
