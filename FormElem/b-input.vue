<template>
  <div>
    <b-input @input="$emit('input', $event.target.value)"></b-input>
  </div>
</template>

<script>
export default {
};
</script>

<style>
</style>