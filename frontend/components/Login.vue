<template>
   <v-app id="inspire">
      <v-main>
         <v-container fluid fill-height>
            <v-layout align-center justify-center>
               <v-flex xs12 sm8 md4>
                  <v-card class="elevation-12">
                     <v-toolbar dark color="primary">
                        <v-toolbar-title>Login form</v-toolbar-title>
                     </v-toolbar>
                     <v-card-text>
                        <v-form>
                           <v-text-field
                              name="email"
                              label="Email"
                              type="text"
                              v-model="email"
                           ></v-text-field>
                           <v-text-field
                              id="password"
                              name="password"
                              label="Password"
                              type="password"
                              v-model="password"
                           ></v-text-field>
                        </v-form>
                     </v-card-text>
                     <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" @click="loginHandler">Login</v-btn>
                     </v-card-actions>
                  </v-card>
               </v-flex>
            </v-layout>
         </v-container>
      </v-main>
   </v-app>
</template>

<script>

export default {
   name: 'Login',
   data() {
      return {
         email: null,
         password: null
      }
   },
   methods: {
     async loginHandler() {
         const data = { 'email': this.email, 'password': this.password }
         console.log(data);
         try{
            const response = await this.$auth.loginWith('local', { data: data})
            console.log(response)
            this.$auth.$storage.setUniversal('email', response.data.email)
            await this.$auth.setUserToken(response.data.access_token, response.data.refresh_token)

         } catch(e) {
            console.log(e.message)
         }
      }
   }
};
</script>

<style></style>
