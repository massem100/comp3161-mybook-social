
<template>
  
  <div id="app">

    <router-view> </router-view>


  </div>

</template>

<script type = 'module'>

import app_header from "/components/app-header.vue";
export default {
    name: 'App', 
    components: {
            app_header
    }
}
</script>

<style>

</style>