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
        size="is-large"
        :label="hint"
        multilined
        :active="active"
        type="is-dark"
        always
      >
        <b-input
          :icon="icon"
          :type="type"
          :id="id"
          :max="max"
          :min="min"
          v-model="model[fieldmodel][def_key]"
          :placeholder="placeholder"
          :maxlength="maxlength"
          :validation-message="message"
          :has-counter="false"
          :required="required"
        ></b-input>
      </b-tooltip>
    </b-field>
  </section>
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
    "model",
    "max",
    "min",
    "def_key"
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