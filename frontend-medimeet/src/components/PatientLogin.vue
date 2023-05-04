<template>
    <div id="signin-page">
        <h2>Sign in to your Patient account</h2>
        <p id="centered">Did you want to sign in to a Doctor account? Click here</p>
        <div id="container">
            <div id="row">
                <div id="col-lg-4 col-md-6 col-sm-8 mx-auto">
                    <div id="card signin" v-bind:class="{ error: emptyFields }">
                        <form id="form">
                            <p>Email address</p>
                            <input v-model="email" type="email" id="form-inputs" required>
                            <p>Password</p>
                            <input v-model="password" type="password" id="form-inputs" required>
                            <input type="radio" id="remember" name="remember" value="Remember me">
                            <p>Forgot your password</p>
                            <input type="submit" id="button" @click="doLogin" value="Sign in">
                            <p id="centered">Or continue with</p>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
        
    
</template>

<script>
    export default {
        name: 'PatientSignin',
        data() {
            return{
                input: {
                    email: "",
                    password: "",
                    emptyFields: false
                }
            }
        },
        methods: {
            doLogin(){
                if (this.input.email != "" && this.input.password != ""){
                    /*check against database if not do the below*/
                    console.log("The email address and / or password is incorrect");
                }
            }
        }
    }
</script>

<style>
    h2{
        align-items: center;
    }

    #centered{
        align-items: center;
    }
</style>