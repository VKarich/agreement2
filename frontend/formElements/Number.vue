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
          v-model="model[fieldmodel]"
          :placeholder="placeholder"
          :maxlength="maxlength"
          :validation-message="message"
          :has-counter="false"
          :required="required"
          @change.native="saveCost(fieldmodel)"
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
    "min"
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
    saveCost(fieldmodel) {
      if (fieldmodel == 'cost') {
        for (let i in this.model) {
          if (JSON.stringify(i).includes('paySum') && !JSON.stringify(i).includes('WSum')) {
            this.model[i] = this.model[fieldmodel];
            this.model.nal = this.model[fieldmodel];
            this.model.bznal = this.model[fieldmodel];
          }
        }
      }
    }
  }
};
</script>

<style>
</style>