<template>
  <div class="buttons">
      <b-button type="is-black" expanded @click="sendNumber">{{ label }}</b-button>
  </div>
</template>

<script>
export default {
  props: [
    "placeholder",
    "type",
    "name",
    "id",
    "required",
    "hint",
    "value",
    "params",
    "label",
    "icon",
    "maxlength",
    "minlength",
    "message",
    "fieldmodel",
    "model",
    "pattern",
  ],
  data() {
    return {};
  },
  methods: {
    sendNumber() {
      console.log(this.model.propertyUniqueIdentifier)
    },
    hintExist() {
      if (this.hint == null) {
        return false;
      }
      return true;
    },
  },
};
</script>

<style>
</style>