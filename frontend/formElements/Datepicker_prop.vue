<template>
  <div>
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
        size="is-large"
        multilined
        :active="active"
        type="is-dark"
        always
      >
        <b-datepicker
          :icon="icon"
          :placeholder="placeholder"
          v-mask="'99.99.9999'"
          v-model="model[fieldmodel][def_key]"
          :locale="locale"
          editable
          :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
          :firstDayOfWeek="1"
          :openOnFocus="true"
          :required="required"
        >
        </b-datepicker>
      </b-tooltip>
    </b-field>
  </div>
</template>

<script>
import AwesomeMask from "awesome-mask";

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
    "validation-message",
    "position",
    "fieldmodel",
    "model",
    "def_key"
  ],
  directives: {
    mask: AwesomeMask,
  },
  data() {
    return {
      locale: "ru-t-en-cyrl-gb-h0-hybrid",
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