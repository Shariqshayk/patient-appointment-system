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
      <div class="dashboard-left">
        <h5 class="header-dash">Suggested Doctors</h5>
        <div class="suggested-doctors-box">
          <doctor-modal></doctor-modal>
          <doctor-modal></doctor-modal>
          <doctor-modal></doctor-modal>
          <doctor-modal></doctor-modal>
        </div>
      </div>
      <div class="dashboard-right">
        <div>
          <h5 class="header-dash">Upcoming appointments</h5>
        </div>
        <div>
          <h5 class="header-dash">Your medical documents</h5>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import DoctorModal from './DoctorModal.vue'

  export default{
    name: 'PatientDashboard',
    components: {
      DoctorModal
    }
  }
</script>

<style scoped>
 .suggested-doctors-box {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 13px;
    padding: 25px;
 }
</style>
