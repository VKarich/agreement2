<template>
  <div class="buttons">
      <b-button type="is-danger" size="is-small" icon-left="folder-remove" expanded rounded  @click="test">{{ 'Убрать объект недвижимости' }}</b-button>
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
    "changeRemove",
    "quantityOfProperty"
  ],
  data() {
    return {
    };
  },
  methods: {
    test() {
      let len = this.fields[this.i].fields.length;
      let len2 = (this.fields[this.i].fields.length - 14);

      for (let n in this.model) {
        if (n.includes('property') && this.model[n].length > 1) {
          this.model[n].splice(-1, this.quantityOfProperty);
        }
      }
      for (let c = len2 - 3; c <= len2 -1; c++) {
        let x = Object.keys(this.fields[this.i].fields[c]).filter(
            (key) =>
              JSON.stringify(key).match("type")
          );
          if (this.fields[this.i].fields[c][x] == 'Button_remove') {
            this.fields[this.i].fields[c][x] = "Button_add"
          }
      }
      for (let y = 0; y <= (len-1); y++) {
        this.fields[this.i].fields.splice((len-14), 14);
      }
      this.changeRemove()
    },
  },
};
</script>

<style>
</style>