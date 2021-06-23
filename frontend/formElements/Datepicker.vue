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
        :active="active"
        :label="hint"
        position="is-bottom"
        size="is-large"
        multilined
        type="is-dark"
        always
      >
        <b-datepicker
          :icon="icon"
          :placeholder="placeholder"
          v-mask="'99.99.9999'"
          v-model="model[fieldmodel]"
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
  created() {
    if (this.model.date !== null) {
      this.model.date = new Date(this.model.date)
    }
    if (this.model.sellerBirthYear !== null) {
      this.model.sellerBirthYear = new Date(this.model.sellerBirthYear)
    }
    if (this.model.sellerPassIssuedOn !== null) {
      this.model.sellerPassIssuedOn = new Date(this.model.sellerPassIssuedOn)
    }
    if (this.model.sellerOrgDocDate !== null) {
      this.model.sellerOrgDocDate = new Date(this.model.sellerOrgDocDate)
    }
    if (this.model.custBirthYear !== null) {
      this.model.custBirthYear = new Date(this.model.custBirthYear)
    }
    if (this.model.custPassIssuedOn !== null) {
      this.model.custPassIssuedOn = new Date(this.model.custPassIssuedOn)
    }
    if (this.model.custOrgDocDate !== null) {
      this.model.custOrgDocDate = new Date(this.model.custOrgDocDate)
    }
    if (this.model.regDocDate !== null) {
      this.model.regDocDate = new Date(this.model.regDocDate)
    }
    if (this.model.matcapDesDate !== null) {
      this.model.matcapDesDate = new Date(this.model.matcapDesDate)
    }
    if (this.model.matcapDate !== null) {
      this.model.matcapDate = new Date(this.model.matcapDate)
    }
    if (this.model.crBankDocDate !== null) {
      this.model.crBankDocDate = new Date(this.model.crBankDocDate)
    }
    if (this.model.zlgPayTermDate !== null) {
      this.model.zlgPayTermDate = new Date(this.model.zlgPayTermDate)
    }
    if (this.model.sellerOrgDocPassDate !== null) {
      this.model.sellerOrgDocPassDate = new Date(this.model.sellerOrgDocPassDate)
    }
    if (this.model.custOrgDocPassDate !== null) {
      this.model.custOrgDocPassDate = new Date(this.model.custOrgDocPassDate)
    }
    if (this.model.sellerRepresentDocDate !== null) {
      this.model.sellerRepresentDocDate = new Date(this.model.sellerRepresentDocDate)
    }
    if (this.model.sellerRepresentPassDate !== null) {
      this.model.sellerRepresentPassDate = new Date(this.model.sellerRepresentPassDate)
    }
    if (this.model.custRepresentDocDate !== null) {
      this.model.custRepresentDocDate = new Date(this.model.custRepresentDocDate)
    }
    if (this.model.custRepresentPassDate !== null) {
      this.model.custRepresentPassDate = new Date(this.model.custRepresentPassDate)
    }
  }
};
</script>

<style>
</style>