<template>
  <v-container>
    <v-row justify="center">
        <h1>{{Teste}}</h1>
      <v-col style="width: 60%;">
        <v-form ref="form" v-model="valid" :lazy-validation="lazy">
          <v-text-field solo v-model="user.nome" :counter="50" :rules="nameRules" label="Nome" required></v-text-field>
          <v-text-field solo v-model="user.idade" type="number"  label="Idade" required>{{user.idade}}</v-text-field>
          <v-text-field solo v-model="user.funcao" :counter="50" :rules="nameRules" label="Função" required></v-text-field>
          <v-select
            solo
            v-model="departamentoSelecionado"
            :items="departamentos"
            item-value="pk"
            item-text="fields.nome"
            :rules="[v => !!v || 'Item is required']"
            label="Departamento"
            required
          ></v-select>

          <v-btn color="success" class="mr-4" v-on:click="saveOrUpdateUser()">Salvar</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import router from '@/router'

export default {
  name: "UserForm",
  data() {
    return {
      id: "",
      user: {
        nome: "",
        idade: 0,
        funcao: "",
        departamento: 1
      },
      departamentos: [],
      departamentoSelecionado: null,
      nameRules: [
        (v) => !!v || "Nome não poder ser vazio.",
        (v) =>
          (v && v.length <= 50) || "Nome precisa ter 50 caracteres ou menos.",
      ],
      ageRules: [
        
        (v) =>(v && v.parseInt() >= 0) ||
          "Idade precisa ser um inteiro positivo maior que zero.",
      ],
    };
  },
  methods: {
    saveOrUpdateUser: function () {
        console.log("departamento" , this.departamentoSelecionado)
      if(this.id != "")
      axios.post("http://localhost:8000/api/user/" + this.id, {nome: this.user.nome, 
                                                            idade: this.user.idade, 
                                                            funcao: this.user.funcao,
                                                            departamento: this.departamentoSelecionado})
        .then((response) => {
          if (response.status === 200) router.push({path: '/'})
        });
        else 
        axios.post("http://localhost:8000/api/create/user/", {nome: this.user.nome, 
                                                            idade: this.user.idade, 
                                                            funcao: this.user.funcao,
                                                            departamento: this.departamentoSelecionado})
        .then((response) => {
          if (response.status === 200) router.push({path: '/'})
        });

    },
  },
  mounted() {
      this.id = this.$router.history.current.params.id;
      if(this.id !== ""){
        axios.get("http://localhost:8000/api/user/" + this.id)
        .then((response) => {
          console.log('user response', response)
          if (response.status === 200) {
              this.user.nome = response.data.nome;
              this.user.funcao = response.data.funcao;
              this.user.idade = response.data.idade;
              this.user.departamento = response.data.departamento
          }
        });
      }
    axios.get("http://localhost:8000/api/departamentos").then(response =>{  
        this.departamentos = response.data;
        response.data.map(item =>{
            if(item.pk === this.user.departamento)
              this.departamentoSelecionado = item
        })
      console.log("valor final de departamento", this.departamentoSelecionado)
    })
  }
};
</script>
