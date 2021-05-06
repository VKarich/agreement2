<template>
  <div>
    <section>
          <b-progress
            :value="Math.round(i * 16.6)"
            ref="box"
            :max="100"
            size="is-medium"
            show-value
          >
            {{ Math.round(i * 16.6) + "%" }}
          </b-progress>
        </section>
    <label
      v-for="(legend, key) in config.groups[i].legend"
      :key="key"
      >{{ legend }}</label
    >
    <div v-for="(field, key) in config.groups[i].fields" :key="key">
      <label>{{ field.label }}</label>
      <component
        :is="field.type"
        :type="field.inputType"
        :v-model="field.model"
        :placeholder="field.placeholder"
        :name="field.name"
        :value="field.value"
        :params="field.params"
        @input="updateField($event, field)"
      >
      </component>
    </div>
    <section class="pag">
      <b-button
            id="left-button"
            type="is-primary"
            v-show="lr"
            @click="Back"
            @mouseenter="disIsValid"
            >Назад</b-button
          >
      <b-button
            id="right-button"
            type="is-dark"
            outlined
            v-show="ls"
            @click="Next"
            :disabled="dis"
            @mouseenter="isValid"
            >Продолжить</b-button
          >
    </section>
  </div>
</template>

<script>
// import Vue from 'vue'
export default {
  props: ["config", "model"],
  data() {
    return {
      i: 0,
      valid: 0,
      ls: true,
      lr: false,
      dl: false,
      dis: false,
      formValues: {},
    };
  },
  created() {
    // this.config.map(f => {
    //   Vue.set(this.formValues, f.model, null)
    //   console.log(this.config)
    // })
    console.log(this.config.groups);
  },
  methods: {
    updateField(event, field) {
      console.log(field.label);
      console.log(this.formValues);
    },
    Next() {
      if (this.valid === 0) {
        this.i += 1;
        this.$refs.box.$el.scrollIntoView({ behavior: "smooth" });
      }
      if (this.i >= 6) {
        this.ls = false;
        this.dl = true;
      }
      if (this.i >= 1) {
        this.lr = true;
      }
    },
    Back() {
      this.i -= 1;
      if (this.i === 0) {
        this.lr = false;
      }
      if (this.i <= 6) {
        this.ls = true;
        this.$refs.box.$el.scrollIntoView({ behavior: "smooth" });
      }
      if (this.i != 6) {
        this.dl = false;
      }
    },
    isValid() {
      return (this.valid = document.getElementsByClassName(
        "input is-danger"
      ).length);
    },
    disIsValid() {
      this.valid = 0;
    },
  },
};
</script>

<style scoped>
.pag {
  padding: 8%;
}
</style>