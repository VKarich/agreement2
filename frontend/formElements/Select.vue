<template>
  <b-field :label="label">
    <template #label>
        {{ label }}
        <b-icon v-if="hint"
          size="is-small"
          icon="help-circle-outline"
          @mouseenter.native="hintExist"
          @mouseout.native="hintExist"
        ></b-icon>
      </template>
    <b-tooltip
      class="fixed"
      :label="hint"
      position="is-bottom"
      size="is-large"
      multilined
      :active="active"
      type="is-dark"
      always
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
    "model",
    "quantityOfProperty",
    "def_key",
    "field"
  ],
  data() {
    return {
      active: false,
    };
  },
  methods: {
    hintExist() {
      if (this.hint) {
        this.active = !this.active;
      } else {
        this.active = false;
      }
    },
  }
};
</script>

<style>
</style>