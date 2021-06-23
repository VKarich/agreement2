<template>
  <section>
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
        position="is-bottom"
        type="is-dark"
        :active="active"
        size="is-large"
        :label="hint"
        multilined
        always
      >
        <b-input
          :icon="icon"
          :type="type"
          :id="id"
          v-model="model[fieldmodel]"
          :placeholder="placeholder"
          :maxlength="maxlength"
          :pattern="pattern"
          :minlength="minlength"
          :validation-message="message"
          :has-counter="false"
          :required="required"
        ></b-input>
      </b-tooltip>
    </b-field>
  </section>
</template>

<script>
/* eslint-disable */
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
    "quantityOfProperty",
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
  },
};
</script>

<style>
</style>