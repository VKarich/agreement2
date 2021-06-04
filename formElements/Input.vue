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
          :pattern="pattern"
          :minlength="minlength"
          :validation-message="message"
          :has-counter="false"
          :required="required"
          @change.native="send(fieldmodel)"
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
    "minlength",
    "message",
    "fieldmodel",
    "model",
    "pattern",
  ],
  data() {
    return {
    };
  },
  methods: {
    send(fieldmodel) {
      if (fieldmodel.indexOf('propertyUniqueIdentifier') > -1) {
        console.log(this.model[fieldmodel])
      }
    },
    hintExist() {
      if (this.hint == null) {
        return false
      } return true
    },
  }
};
</script>

<style>
</style>