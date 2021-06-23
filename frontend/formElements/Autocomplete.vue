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
        <b-autocomplete
          v-model="model[fieldmodel]"
          :data="filteredDataArray"
          :openOnFocus="true"
          :placeholder="placeholder"
          clearable
          @select="(option) => (selected = option)"
        >
          <template #empty>Нет совпадений</template>
        </b-autocomplete>
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
    "data"
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
  computed: {
    filteredDataArray() {
      return this.data.filter((option) => {
        return (
          option
            .toString()
            .toLowerCase()
            .indexOf(this.model[this.fieldmodel].toLowerCase()) >= 0
        );
      });
    },
  },
};
</script>

<style>
</style>