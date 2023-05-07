<template >
    <div id="regiser">
        <a href="/"><img src="../images/medimeet.png" height="120" id="image"></a>

        <div id="container">
            <form v-bind:class="{ error: emptyFields}" id="form">
                <p id="input-label1">Email address</p>
                <input v-model="email" type="email" class="form-control" id="form-inputs" required>
                <p id="input-label2">Password</p>
                <input v-model="password" type="password" class="form-control" id="form-inputs" required>
                <p id="input-label3">First name</p>
                <input v-model="firstName" type="firstName" class="form-control" id="form-inputs" required>
                <p id="input-label4">Last name</p>
                <input v-model="lastName" type="lastName" class="form-control" id="form-inputs" required>
                <p id="input-label5">City</p>
                <input v-model="city" type="city" class="form-control" id="form-inputs" required>
                <p id="input-label6">Phone number</p>
                <input v-model="phoneNumber" type="phoneNumber" class="form-control" id="form-inputs" required>
                <p id="input-label7">Role</p>
                <select v-model="role" type="role">
                    <option disabled value="">Please select one</option>
                    <option>Patient</option>
                    <option>Doctor</option>
                </select>
                <input type="submit" id="button-register" class="btn" @click="doRegister()" value="Register">
            </form>
        </div>
    </div>
</template>

<script>
export default{
      name: "Register",
      data() {
        return {
            input: {
                email: "",
                password: "",
                firstName: "",
                lastName: "",
                city: "",
                phoneNumber: "",
                role: "",
                emptyFields: false
            }
        }
      },
      methods: {
        doRegister(){
            /*Register script to go here*/
        }
      }
}
</script>
<style>
    #register{
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

    #form{
        padding-top: 0.5cm;
    }

    #input-label1{
        top: 10px;
        right: 3.7cm;
    }

    #input-label2{
        top: 10px;
        right: 3.7cm;
    }

    #input-label3{
        top: 10px;
        right: 3.7cm;
    }

    #input-label4{
        top: 10px;
        right: 3.7cm;
    }

    #input-label5{
        top: 10px;
        right: 3.7cm;
    }

    #input-label6{
        top: 10px;
        right: 3.7cm;
    }

    #input-label7{
        top: 10px;
        right: 3.7cm;
    }

    #button-register{
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

    #image{
        text-align: center;
    }

</style>