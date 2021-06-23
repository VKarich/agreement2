<template>
  <section>
    <p class="separator" v-text="label"></p>
  </section>
</template>

<script>
export default {
  props: ["label"],
};
</script>

<style>
.separator {
  font-size: 21px;
    font-weight: bold;
    border-bottom: rgb(201, 201, 201) 1px solid;
    padding-bottom: 2.5%;
    padding-top: 2.5%;
}
</style>