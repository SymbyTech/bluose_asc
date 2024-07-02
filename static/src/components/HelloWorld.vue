<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "Loading..."
    };
  },
  mounted() {
    fetch("http://127.0.0.1:8000")
      .then(response => response.json())
      .then(data => {
        this.message = data.message;
      });
  }
};
</script>

<style scoped>
h1 {
  font-family: Arial, sans-serif;
}
</style>
