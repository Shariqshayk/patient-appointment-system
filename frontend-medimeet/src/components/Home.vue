<template>
      <header id="home-page">
            <img id="background-image" src="../images/homepagephoto.jpg" height="120"> 
      <div id="home-content">
            <img id="logo" src="../images/medimeet.png" height="120">  
            <h1 id="header">Welcome to <strong class="primary">MediMeet!</strong> </h1>
            <h2 id="header2">Your Medical Concerns <strong>Ends Here!</strong></h2>
            <p id="paragraph1">Our biggest aim is for patients to have meetings with their doctors quickly and efficiently.
                  We allow patients to go straight to the department and book appointments for their problem, cutting out
                  the middleman of the GP for their bigger concerns. With MediMeet patients can book  appointments with specialists,
                  upload medical documents in order for doctors to see. Additionally, MediMeet provides a survey for patients who are
                  not confident which doctor they should have an appointment with.</p>
            <div id="body1">
                  <a href="#/patientlogin"><button id="home-button1" class="btn">Patient Login</button></a>
                  <a href="#/doctorlogin"><button id="home-button2" class="btn">Doctor Login</button></a>
            </div>      
      </div>     
</header>

</template>

<style>
#home-page {
  width: 100vh;
  height: 100vh;
}  

#home-content {
  bottom: 22cm;
}

#header{
  margin-top: 2cm;
  margin-left: 2cm;
}

#header2{
  margin-left: 2cm;
}

#paragraph1{
  margin-top: 10mm;
  margin-left: 2cm;
  max-width: 600px;
}

#logo{
  margin-left: 1cm;
}

#background-image{
  margin-left: 12cm;
  height: 100vh;
  max-width: 140%;
	clip-path: polygon(50% 0%, 100% 0%, 100% 100%, 0% 100%);
}

#home-button1{
  margin-top: 1cm;
  margin-left: 2.5cm;
  width: 150px;
  height: 50px;
  background-color: rgb(71, 140, 252);
  color: white;
}

#home-button2{
  margin-top: 1cm;
  margin-left: 5mm;
  width: 150px;
  height: 50px;
  background-color: white;
  color: rgb(71, 140, 252);
  box-shadow: 0px 0px 3px gray;
}
</style>

<script>
export default{
      name: "Home",  
}
</script>
