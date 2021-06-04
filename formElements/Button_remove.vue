<template>
  <div class="buttons">
      <b-button type="is-info" expanded @click="test">{{ 'Убрать объект недвижимости' }}</b-button>
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
    "i",
    "fields",
    "changeAdd"
  ],
  data() {
    return {
    };
  },
  methods: {
    test() {
      let len = this.fields[this.i].fields.length;
      for (let c = 0; c <= len -1; c++) {
        let x = Object.keys(this.fields[this.i].fields[c]).filter(
            (key) =>
              JSON.stringify(key).match("type")
          );
          if (this.fields[this.i].fields[c][x] == 'Button_remove') {
            this.fields[this.i].fields[c][x] = "Button_add"
          }
      }
      for (let y = 0; y <= (len-1); y++) {
        this.fields[this.i].fields.splice((len-14), 14)
      }
      this.changeAdd()
    },
  },
};
</script>

<style>
</style>