<template>
  <section>
    <label class="lab">{{ label }}</label>
    <multiselect
      v-model="model[fieldmodel]"
      :options="values"
      :multiple="true"
      :maxHeight="Number(200)"
      :tag-placeholder="placeholder"
      :placeholder="placeholder"
      label="name"
      track-by="name"
      required
    >
    </multiselect>
  </section>
</template>

<script>
import Multiselect from "vue-multiselect";

export default {
  components: {
    Multiselect,
  },
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
    "message",
    "fieldmodel",
    "values",
    "position",
    "model",
  ],
  data() {
    return {
    };
  },
};
</script>

<style>
</style>