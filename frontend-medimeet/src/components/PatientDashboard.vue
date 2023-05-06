<template>
    <div id="container-header">
        <img id="logo-dashboard" src="../images/medimeet.png" height="100">
        <hr id="h-line">
        <header id="dashboard-header">
            <h3>Dashboard</h3>
        </header>
        <div>
            <i class="fa fa-search"></i>
            <input type="text" class="form-control form-input" id="search-bar" placeholder="Search for a doctor">
        </div>
    </div>   
    <div id="dashboard">
    <div id="dashed-border">
        <h5 id="header-dash">Suggested Doctors</h5>
    </div>
    </div>
</template>

<script>
    export default{
        name: 'PatientDashboard',
    }
</script>