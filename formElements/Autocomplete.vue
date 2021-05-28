<template>
  <section>
    <b-field :label="label">
      <b-tooltip
        class="fixed"
        position="is-top"
        :active="hintExist()"
        size="is-large"
        :label="hint"
        multilined
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
    };
  },
  methods: {
    hintExist() {
      if (this.hint == null) {
        return false
      } return true
    }
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