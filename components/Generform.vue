<template>
  <div class="second_selection">
    <div
      id="sec_"
      v-if="select_first_step == 'Договор купли-продажи недвижимого имущества'"
    >
      <div id="left_menu">
        <form-builder
          :model="model"
          :schema_test="schema_test"
          :select_second_step="select_second_step"
          :select_third_step="select_third_step"
          :sendData="sendData"
        ></form-builder>
      </div>
      <div id="right_menu">
        <dkp
          :model="model"
          :select_second_step="select_second_step"
          :select_third_step="select_third_step"
        />
      </div>
    </div>
    <div id="sec_" v-if="select_first_step == 'Договор аренды'">
      <div id="left_menu">
        <form-builder
          :model="model"
          :schema_test="schema_test"
          :select_second_step="select_second_step"
          :select_third_step="select_third_step"
          :sendData="sendData"
        ></form-builder>
      </div>
      <div id="right_menu"></div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import dkp from "@/agreements/dogovor_kupli_prodazhi";
import model_out from "@/model.json";
import axios from "axios";
import formBuilder from "./formBuilder.vue";

import mainInfo_out from "@/schema/main_info.json";
import flSeller_out from "@/schema/fl_seller.json";
import ulSeller_out from "@/schema/ul_seller.json";
import mainObject_out from "@/schema/main_object.json";
import mainPayment_out from "@/schema/main_payment.json";

const flBuyer_out = JSON.parse(JSON.stringify(flSeller_out).replaceAll('Продавца', 'Покупателя').replaceAll('продавца', 'покупателя').replaceAll('seller', 'cust'));
const ulBuyer_out = JSON.parse(JSON.stringify(ulSeller_out).replaceAll('Продавца', 'Покупателя').replaceAll('продавца', 'покупателя').replaceAll('seller', 'cust'));

const mainInfo = mainInfo_out.groups;
const flSeller_1 = {
  legend: flSeller_out.groups[0].legend,
  fields: flSeller_out.groups[0].fields.slice(0, 4),
};
const flSeller_2 = {
  legend: flSeller_out.groups[0].legend,
  fields: flSeller_out.groups[0].fields.slice(4),
};
const ulSeller_1 = {
  legend: ulSeller_out.groups[0].legend,
  fields: ulSeller_out.groups[0].fields.slice(0, 4),
};
const ulSeller_2 = {
  legend: ulSeller_out.groups[0].legend,
  fields: ulSeller_out.groups[0].fields.slice(4),
};
const flBuyer_1 = {
  legend: flBuyer_out.groups[0].legend,
  fields: flBuyer_out.groups[0].fields.slice(0, 4),
};
const flBuyer_2 = {
  legend: flBuyer_out.groups[0].legend,
  fields: flBuyer_out.groups[0].fields.slice(4),
};
const ulBuyer_1 = {
  legend: ulBuyer_out.groups[0].legend,
  fields: ulBuyer_out.groups[0].fields.slice(0, 4),
};
const ulBuyer_2 = {
  legend: ulBuyer_out.groups[0].legend,
  fields: ulBuyer_out.groups[0].fields.slice(4),
};
const mainObject = mainObject_out.groups;

const mainPayment = mainPayment_out.groups;

const dick = JSON.stringify(flSeller_1).toLowerCase().replaceAll('продавца', 'покупателя')

const fl_fl = mainInfo
  .concat(flSeller_1)
  .concat(flSeller_2)
  .concat(flBuyer_1)
  .concat(flBuyer_2)
  .concat(mainObject)
  .concat(mainPayment);

// const rubles = require("rubles").rubles;

export default {
  components: {
    dkp,
    formBuilder,
  },
  name: "Generform",
  props: {
    select_first_step: String,
    select_second_step: String,
    select_third_step: String,
    show_first: Boolean,
  },
  data() {
    return {
      selected: null,
      isSwitched: false,
      isSwitchedCustom: "Нет",
      model: model_out,
      fl_fl: mainInfo
        .concat(flSeller_1)
        .concat(flSeller_2)
        .concat(flBuyer_1)
        .concat(flBuyer_2)
        .concat(mainObject)
        .concat(mainPayment),
      fl_ul: mainInfo
        .concat(flSeller_1)
        .concat(flSeller_2)
        .concat(ulBuyer_1)
        .concat(ulBuyer_2)
        .concat(mainObject)
        .concat(mainPayment),
      ul_fl: mainInfo
        .concat(ulSeller_1)
        .concat(ulSeller_2)
        .concat(flBuyer_1)
        .concat(flBuyer_2)
        .concat(mainObject)
        .concat(mainPayment),
      ul_ul: mainInfo
        .concat(ulSeller_1)
        .concat(ulSeller_2)
        .concat(ulBuyer_1)
        .concat(ulBuyer_2)
        .concat(mainObject)
        .concat(mainPayment),
      schema_test: fl_fl,
    };
  },
  methods: {
    sendData() {
      // for (let n in this.model) {
      //   if (this.model[n] !== null && JSON.stringify(this.model[n]).match("00:00:00")) {
      //     console.log(n)
      //     this.model[n] = this.model[n].toLocaleDateString();
      //     this.model.date = this.model.date.toLocaleDateString();
      //   }
      // }
      // this.model.date = this.model.date.toLocaleDateString();
      // this.model.sellerBirthYear = this.model.sellerBirthYear.toLocaleDateString();
      // this.model.sellerOrgDocDate = this.model.sellerOrgDocDate.toLocaleDateString();
      // this.model.sellerOrgDocPassDate = this.model.sellerOrgDocPassDate.toLocaleDateString();
      // this.model.sellerPassIssuedOn = this.model.sellerPassIssuedOn.toLocaleDateString();
      // this.model.custBirthYear = this.model.custBirthYear.toLocaleDateString();
      // this.model.custPassIssuedOn = this.model.custPassIssuedOn.toLocaleDateString();
      // this.model.custOrgDocDate = this.model.custOrgDocDate.toLocaleDateString();
      // this.model.regDocDate = this.model.regDocDate.toLocaleDateString();
      // this.model.matcapDesDate = this.model.matcapDesDate.toLocaleDateString();
      // this.model.matcapDate = this.model.matcapDate.toLocaleDateString();
      // this.model.crBankDocDate = this.model.crBankDocDate.toLocaleDateString();
      // this.model.custOrgDocPassDate = this.model.custOrgDocPassDate.toLocaleDateString();
      // this.model.zlgPayTermDate = this.model.zlgPayTermDate.toLocaleDateString();
      // this.model.sellerRepresentDocDate = this.model.sellerRepresentDocDate.toLocaleDateString();
      // this.model.sellerRepresentPassDate = this.model.sellerRepresentPassDate.toLocaleDateString();
      // this.model.custRepresentDocDate = this.model.custRepresentDocDate.toLocaleDateString();
      // this.model.custRepresentPassDate = this.model.custRepresentPassDate.toLocaleDateString();
      axios
        .post(
          "/generate/dkp/docx",
          {
            model: this.model,
            select_first_step: this.select_first_step,
            select_second_step: this.select_second_step,
            select_third_step: this.select_third_step,
          },
          { responseType: "blob" },
        )
        .then((response) => {
          if (response.status == 200) {
            var blob = new Blob([response.data]);
            var downloadElement = document.createElement("a");
            var href = window.URL.createObjectURL(blob);
            downloadElement.style.display = "none";

            downloadElement.href = href;
            downloadElement.download = "dd.docx";
            document.body.appendChild(downloadElement);
            downloadElement.click();
            document.body.removeChild(downloadElement);
            window.URL.revokeObjectURL(href);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  beforeUpdate() {
    if (this.select_second_step == "ФЛ" && this.select_third_step == "ФЛ") {
      this.schema_test = this.fl_fl;
    }
    if (this.select_second_step == "ФЛ" && this.select_third_step == "ЮЛ") {
      this.schema_test = this.fl_ul;
    }
    if (this.select_second_step == "ЮЛ" && this.select_third_step == "ФЛ") {
      this.schema_test = this.ul_fl;
    }
    if (this.select_second_step == "ЮЛ" && this.select_third_step == "ЮЛ") {
      this.schema_test = this.ul_ul;
    }
  },
  mounted() {
    // if (localStorage.model) {
    //   this.model = JSON.parse(localStorage.model);
    //   this.model.rsPaymentDate = {};
    //   this.model.rsPaymentDateFL = {};
    // }
  },
  watch: {
    model: {
      deep: true,
      handler(newValue) {
        // localStorage.model = JSON.stringify(newValue);
        //newValue.custRepresent == "Нет"
        if (
          newValue.sellerRepresent == "Нет"
        ) {
          let x = Object.keys(newValue).filter(
            (key) => JSON.stringify(key).match("sellerRepresent") && key.length > 15
          );
          for (let n in x) {
            this.model[x[n]] = null;
          }
        }
        if (
          newValue.custRepresent == "Нет"
        ) {
          let x = Object.keys(newValue).filter(
            (key) => JSON.stringify(key).match("custRepresent") && key.length > 15
          );
          for (let n in x) {
            this.model[x[n]] = null;
          }
        }
      },
    }
  },
};
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
select {
  text-align-last: center;
}
@media screen and (max-width: 3280px) {
  #sec_ {
    display: flex;
  }
  #left_menu {
    position: relative;
    border-radius: 10px;
    box-shadow: 0 0.5em 1em -0.125em rgb(10 10 10 / 10%),
      0 0 0 1px rgb(10 10 10 / 2%);
    background-color: rgba(206, 206, 206, 0.041);
    min-width: 390px;
    max-width: 400px;
    float: left;
    padding: 10px;
    padding-bottom: 40px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    margin-right: 10px;
    overflow-y: scroll;
    -webkit-overflow-scrolling: touch;
    height: auto;
    max-height: 68vh;
  }
  #right_menu {
    position: relative;
    border-radius: 10px;
    box-shadow: 0 0.5em 1em -0.125em rgb(10 10 10 / 10%),
      0 0 0 1px rgb(10 10 10 / 2%);
    width: 100%;
    height: 85vh;
    padding-top: 40px;
    padding-bottom: 40px;
    padding-left: 60px;
    padding-right: 60px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    overflow-y: scroll;
    -webkit-overflow-scrolling: touch;
    text-align: left;
    max-height: 68vh;
  }
  .fixed {
    width: 100%;
  }
  .pag {
    padding: 8%;
  }
  .pos {
    font-size: 21px;
    font-weight: bold;
    border-bottom: rgb(201, 201, 201) 1px solid;
    padding-bottom: 2.5%;
    padding-top: 2.5%;
    margin-bottom: 4%;
  }
  #left-button {
    float: left;
    margin-bottom: 100px;
  }
  #right-button {
    float: right;
    margin-bottom: 100px;
  }
  .multiselect {
    box-sizing: inherit;
    display: block;
    position: relative;
    width: 100%;
    min-height: 40px;
    text-align: left;
    color: #35495e;
  }
  .multiselect__tag {
    position: relative;
    display: inline-block;
    padding: 4px 26px 4px 10px;
    border-radius: 5px;
    margin-right: 10px;
    color: #fff;
    line-height: 1;
    background: #4a4a4a;
    margin-bottom: 5px;
    white-space: nowrap;
    overflow: hidden;
    max-width: 100%;
    text-overflow: ellipsis;
  }
  .multiselect__tag {
    align-items: center;
    border: 1px solid transparent;
    display: inline-flex;
    font-size: 1rem;
    justify-content: flex-start;
  }
  .lab {
    margin-bottom: 0.5em;
    color: #363636;
    display: block;
    font-size: 1rem;
    font-weight: 700;
  }
  .lab2 {
    margin-top: 0.5em;
  }
  #dop_payMethod {
    margin-top: 1.2em;
    font-weight: 700;
  }
  .multiselect__option--highlight {
    background: #4a4a4a;
    outline: none;
    color: #fff;
  }
  .multiselect__option--selected.multiselect__option--highlight {
    background: #4a4a4a;
    color: #fff;
  }
  .multiselect__option--highlight:after {
    content: attr(data-select);
    background: #ffdd57;
    color: #fff;
  }
  .multiselect__tag-icon:after {
    content: "\D7";
    color: #ffdd57;
    font-size: 14px;
  }
  .multiselect__tag-icon:hover {
    background: #ffdd57;
  }
}
@media only screen and (min-device-width: 320px) and (max-device-width: 1024px) {
  #sec_ {
    display: block;
  }
  #left_menu {
    position: flex;
    border-radius: 10px;
    box-shadow: 0 0.5em 1em -0.125em rgb(10 10 10 / 10%),
      0 0 0 1px rgb(10 10 10 / 2%);
    background-color: rgba(206, 206, 206, 0.041);
    min-width: 100%;
    max-width: auto;
    float: left;
    padding: 10px;
    padding-bottom: 40px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    overflow-y: scroll;
    -webkit-overflow-scrolling: touch;
    height: auto;
    max-height: 85vh;
    margin-bottom: 10px;
  }
  #right_menu {
    position: flex;
    border-radius: 10px;
    box-shadow: 0 0.5em 1em -0.125em rgb(10 10 10 / 10%),
      0 0 0 1px rgb(10 10 10 / 2%);
    min-width: auto;
    width: auto;
    height: 85vh;
    padding-top: 40px;
    padding-bottom: 40px;
    padding-left: 60px;
    padding-right: 60px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    overflow-y: scroll;
    -webkit-overflow-scrolling: touch;
    text-align: left;
  }
  .fixed {
    width: 100%;
  }
  .pag {
    padding: 8%;
  }
  .pos {
    font-size: 21px;
    font-weight: bold;
    border-bottom: rgb(201, 201, 201) 1px solid;
    padding-bottom: 2.5%;
    padding-top: 2.5%;
    margin-bottom: 4%;
  }
  #left-button {
    float: left;
    margin-bottom: 10px;
  }
  #right-button_2 {
    float: right;
    margin-bottom: 10px;
  }
  .multiselect {
    box-sizing: inherit;
    display: block;
    position: relative;
    width: 100%;
    min-height: 40px;
    text-align: left;
    color: #35495e;
  }
  .multiselect__tag {
    position: relative;
    display: inline-block;
    padding: 4px 26px 4px 10px;
    border-radius: 5px;
    margin-right: 10px;
    color: #fff;
    line-height: 1;
    background: #4a4a4a;
    margin-bottom: 5px;
    white-space: nowrap;
    overflow: hidden;
    max-width: 100%;
    text-overflow: ellipsis;
  }
  .multiselect__tag {
    align-items: center;
    border: 1px solid transparent;
    display: inline-flex;
    font-size: 1rem;
    justify-content: flex-start;
  }
  .lab {
    margin-bottom: 0.5em;
    color: #363636;
    display: block;
    font-size: 1rem;
    font-weight: 700;
  }
  .lab2 {
    margin-top: 1.5em;
  }
  #dop_payMethod {
    margin-top: 1.2em;
    font-weight: 700;
  }
  .multiselect__option--highlight {
    background: #4a4a4a;
    outline: none;
    color: #fff;
  }
  .multiselect__option--selected.multiselect__option--highlight {
    background: #4a4a4a;
    color: #fff;
  }
  .multiselect__option--highlight:after {
    content: attr(data-select);
    background: #ffdd57;
    color: #fff;
  }
  .multiselect__tag-icon:after {
    content: "\D7";
    color: #ffdd57;
    font-size: 14px;
  }
  .multiselect__tag-icon:hover {
    background: #ffdd57;
  }
}
</style>

<style lang="scss">
@import "~bulma/sass/utilities/_all";
// Set your colors
$primary: #1990d4;
$primary-light: findLightColor($primary);
$primary-dark: findDarkColor($primary);
$primary-invert: findColorInvert($primary);
$twitter: #4099ff;
$twitter-invert: findColorInvert($twitter);
$dark: #141414;

// Lists and maps
$custom-colors: null !default;
$custom-shades: null !default;

// Setup $colors to use as bulma classes (e.g. 'is-twitter')
$colors: mergeColorMaps(
  (
    "white": (
      $white,
      $black,
    ),
    "black": (
      $black,
      $white,
    ),
    "light": (
      $light,
      $light-invert,
    ),
    "dark": (
      $dark,
      $dark-invert,
    ),
    "primary": (
      $primary,
      $primary-invert,
      $primary-light,
      $primary-dark,
    ),
    "link": (
      $link,
      $link-invert,
      $link-light,
      $link-dark,
    ),
    "info": (
      $info,
      $info-invert,
      $info-light,
      $info-dark,
    ),
    "success": (
      $success,
      $success-invert,
      $success-light,
      $success-dark,
    ),
    "warning": (
      $warning,
      $warning-invert,
      $warning-light,
      $warning-dark,
    ),
    "danger": (
      $danger,
      $danger-invert,
      $danger-light,
      $danger-dark,
    ),
  ),
  $custom-colors
);

// Links
$link: $primary;
$link-invert: $primary-invert;
$link-focus-border: $primary;
$dropdown-content-radius: 20px;

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>
