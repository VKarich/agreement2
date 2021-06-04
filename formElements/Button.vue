<template>
  <div class="buttons">
      <b-button type="is-black" expanded @click="sendNumber(field)">{{ label }}</b-button>
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
    "field",
  ],
  data() {
    return {
    };
  },
  methods: {
    sendNumber(field) {
      console.log(this.model[field.visible.dep_name])
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