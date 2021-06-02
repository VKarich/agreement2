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
          @input="send($event)"
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
  ],
  data() {
    return {};
  },
  methods: {
    hintExist() {
      if (this.hint == null) {
        return false;
      }
      return true;
    },
    send(event) {
      var url = "https://cleaner.dadata.ru/api/v1/clean/email";
      var token = "c729f363f4b7735b7fcb9a097f7c65e063572efd";
      var secret = "864fb6a6e8022261967bd2253f7068d84c9a4e69";
      var query = event;

      var options = {
        method: "POST",
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Token " + token,
          "X-Secret": secret,
        },
        body: JSON.stringify([query]),
      };

      fetch(url, options)
        .then((response) => response.text())
        .then((result) => console.log(result))
        .catch((error) => console.log("error", error));
    },
  },
};
</script>

<style>
</style>