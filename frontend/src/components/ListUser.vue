<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <h1>Usuários</h1>
      </v-col>
      <v-row style="width: 100%;" v-bind:key="user.pk" v-for="(user, index) in users">
        <v-card class="mx-auto mb-4" style="width: 100%;">
          <v-row>
            <v-col>
              <v-card-title>{{user.fields.nome}}</v-card-title>
              <v-card-subtitle>{{user.fields.funcao}}</v-card-subtitle>
            </v-col>
            <v-col align-self="center" lg="1" md="2" sm="2" xl="1">
              <v-card-actions>
                <v-row>
                  <v-btn icon v-on:click="editUser(user.pk)">
                    <v-icon>mdi-pencil</v-icon>
                  </v-btn>
                </v-row>
                <v-row>
                  <v-btn icon v-on:click="deleteUser(user.pk, index)">
                    <v-icon>mdi-delete</v-icon>
                  </v-btn>
                </v-row>
              </v-card-actions>
            </v-col>
          </v-row>
        </v-card>
        <v-spacer></v-spacer>
      </v-row>

      <v-card-text style="height: 5px; position: fixed; top: 90%; right:36px">
        <v-fab-transition>
          <v-btn v-show="!hidden" color="primary" dark absolute top right fab v-on:click="createUser()">
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </v-fab-transition>
      </v-card-text>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import router from '@/router'
export default {
  name: "ListUser",
  data() {
    return {
      users: [],
    };
  },
  mounted() {
    axios.get("http://localhost:8000/api/users").then((response) => {
      console.log("resposta", response);
      this.users = response.data;
      console.log("users", this.users);
    });
  },
  methods: {
    deleteUser: function (user_id, index) {
      axios
        .delete("http://localhost:8000/api/user/" + user_id)
        .then((response) => {
          if (response.status === 200) this.users.splice(index, 1);
        });
    },
    createUser: function (){
      router.push({path: '/user/'})
    },
    editUser: function(user_id){
      router.push({ path: '/user/' + user_id})
    }
  },
};
</script>
