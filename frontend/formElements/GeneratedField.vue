<template>
  <div class="lab">
    <b-field
      v-for="one in Number(model.quantityPayments)"
      :key="one"
      :label="'Дата платежа: №' + one"
    >
      <b-datepicker
        v-model="model[fieldmodel[0]][one]"
        icon="calendar-today"
        placeholder="ДД.ММ.ГГГГ"
        :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
        :firstDayOfWeek="1"
        :openOnFocus="true"
        locale="ru-t-en-cyrl-gb-h0-hybrid"
        :focusable="true"
        range
      >
      </b-datepicker>

      <b-tooltip
        label="Введите сумму платежа за указанный период"
        position="is-bottom"
        size="is-small"
        type="is-dark"
        multilined
      >
        <b-input
          placeholder="Введите сумму платежа"
          v-model="model[fieldmodel[1]][one]"
          type="number"
          :min="0"
          required
        ></b-input>
      </b-tooltip>
    </b-field>
  </div>
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
    "message",
    "fieldmodel",
    "values",
    "position",
    "model",
  ],
  data() {
    return {
    };
  },
};
</script>

<style>
</style>