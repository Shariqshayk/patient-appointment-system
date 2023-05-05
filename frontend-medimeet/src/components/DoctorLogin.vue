<template>
    <div id="signin-page">
        <a href="/"><img id="logo-patientlogin" src="../images/medimeet.png" height="120"></a>
        <h2>Sign in to your <strong>Doctor</strong> account</h2>
        <p>Did you want to sign in to a Patient account? <a href="#/patientlogin" id="link">Click here</a></p>
        <div id="container">
            <div id="row">
                <div>
                    <div id="card signin" v-bind:class="{ error: emptyFields }">
                        <form id="form">
                            <p id="input-label1">Email address</p>
                            <input v-model="email" type="email" class="form-control" id="form-inputs" required>
                            <p id="input-label2">Password</p>
                            <input v-model="password" type="password" class="form-control" id="form-inputs" required>
                            <br>
                            <p id="remember"><input type="radio" name="remember" value="Remember me"> Remember Me</p>
                            <p id="forgot">Forgot your password</p>
                            <input type="submit" id="button-patient" class="btn" @click="doLogin" value="Sign in">
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
        name: 'DoctorSignin',
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

    #signin-page{
    text-align: center;
    padding-top: 1cm;
    }

    #container{
    padding-top: 2cm;
    box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
    border-radius: 8px;
    width: 0;
    min-height: 400px;
    min-width: 450px;
    padding-top: 0;
    margin: 0 auto;
    }

    #link{
        text-decoration: none;
        color: rgb(70, 140, 250);
    }
    
    #form{
        padding-top: 0.5cm;
    }

    #input-label1{
        top: 10px;
        right: 3.7cm;
    }

    #input-label2{
        top: 10px;
        right: 4.1cm;
    }

    #remember{
        top: 15px;
        left: 1cm;
        float: left;
    }

    #forgot{
        top: 15px;
        left: 1.3cm;
    }

    #button-patient{
    margin-top: 1cm;
    background-color: rgb(70, 140, 250);
    color: white;
    box-shadow: 0px 0px 3px gray;
    width: 10cm;
    }

    #form-inputs{
        width: 10cm;
        height: 1.1cm;
        left: 0.9cm;
    }

</style>