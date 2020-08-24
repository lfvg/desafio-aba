<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center" v-on:click="goHome()">
        ABA
      </div>
    </v-app-bar>

    <v-content>
      <router-view/>
      
    </v-content>
  </v-app>
</template>

<script>
import router from '@/router'

export default {
  
  name: 'App',
  methods: {
    goHome: function(){
      router.push({ path: '/'})
    }
  },

  data: () => ({
    //
  }),
 

};
</script>
