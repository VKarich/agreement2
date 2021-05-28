<template>
  <section>
    <b-field :label="label">
      <b-tooltip
        class="fixed"
        position="is-bottom"
        :active="hintExist()"
        size="is-large"
        :label="hint"
        multilined
      >
        <b-input
          :icon="icon"
          :type="type"
          :id="id"
          v-model="model[fieldmodel]"
          :placeholder="placeholder"
          :maxlength="maxlength"
          :validation-message="message"
          :has-counter="false"
          :required="required"
          @input="$emit('input', $event)"
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