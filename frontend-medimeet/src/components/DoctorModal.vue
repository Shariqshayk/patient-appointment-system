<template>
<div id="doctor-modal">
  <div class="modal-top">
    <div>
      <img src="../images/blank-avatar.jpg" height="128">
    </div>
    <div>
      <div class="fw-bold">Name Surname</div>
      <div>Location, County</div>
      <div class="specialisation">Specialisation</div>
    </div>
  </div>
  <div class="modal-bottom">
    <div class="modal-bottom inside">
      <font-awesome-icon icon="fa-solid fa-envelope" />
      Email
    </div>
    <div class="modal-bottom inside">
      <font-awesome-icon icon="fa-solid fa-calendar-check" />
      Book
    </div>
  </div>
</div>
</template>

<script>
export default {
name: "DoctorModal"
}
</script>

<style scoped>
  #doctor-modal {
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.06);
    border-radius: 8px;
    width: fit-content;
  }

  .modal-top {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: auto;
    padding: 32px;
  }

  .modal-bottom {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: auto;
  }

  .modal-bottom.inside {
    gap: 12px;
    padding: 15px 40px;
    border: 1px solid  rgba(0, 0, 0, 0.1);
  }

  .modal-bottom.inside:first-child {
    border-radius: 0 0 0 8px;
  }
  .modal-bottom.inside:last-child {
    border-radius: 0 0 8px 0;
  }

  .specialisation {
    color: #065F46;
    background: #D1FAE5;
    border-radius: 100px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding: 4px 8px;
    margin-top: 12px;
  }

  svg {
    color: #9CA3AF;
  }
</style>
