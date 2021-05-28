<template>
  <b-field :label="label">
    <b-tooltip
      class="fixed"
      :active="hintExist()"
      :label="hint"
      :position="position"
      size="is-large"
      multilined
    >
      <b-select
        :placeholder="placeholder"
        v-model="model[fieldmodel]"
        :selected="null"
        expanded
        :icon="icon"
        required
      >
        <option v-for="(nat, index) in values" :key="index">
          {{ nat.name }}
        </option>
      </b-select>
    </b-tooltip>
  </b-field>
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
    "message",
    "fieldmodel",
    "values",
    "position",
    "model"
  ],
  data() {
    return {
    };
  },
  methods: {
    hintExist() {
      if (this.hint == null) {
        return false
      } return true
    }
  }
};
</script>

<style>
</style>