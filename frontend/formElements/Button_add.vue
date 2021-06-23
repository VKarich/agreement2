<template>
  <div class="buttons">
      <b-button type="is-info" size="is-small" icon-left="folder-plus" expanded rounded @click="test">{{ label }}</b-button>
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
    "changeAdd",
    "quantityOfProperty",
  ],
  data() {
    return {
      elem: JSON.parse(JSON.stringify(this.fields[this.i].fields)),
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
          if (this.fields[this.i].fields[c][x] == 'Button_add') {
            this.fields[this.i].fields[c][x] = "Button_remove"
          }
      }
      for (let y = 0; y <= 13; y++) {
        this.elem[y].id = this.fields[this.i].fields[y].id + (this.quantityOfProperty + 1);
        this.elem[y].def_key = this.quantityOfProperty + 1;

        if (this.elem[y].visible) {
          this.elem[y].visible.dep_name = this.fields[this.i].fields[y].visible.dep_name[this.fields[this.i].fields[y].def_key + 1];
        }
        if (this.elem[y].type == "Button_remove") {
          this.elem[y].type = 'Button_add'
        }
        this.fields[this.i].fields.push(this.elem[y]);
      }
      this.changeAdd()
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