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
    <input v-model="i"/>
    <p class="pos" v-text="schema_test[i].legend"></p>
    <section
      class="sec"
      v-for="(field, key) in schema_test[i].fields"
      :key="key"
    >
      <div class="hiden">{{ model[field.model] }}</div>
      <component
        class="sec1"
        pack="fas"
        v-if="fieldVisible(field)"
        :is="field.type"
        :type="field.inputType"
        :id="field.id"
        :placeholder="field.placeholder"
        :fieldmodel="field.model"
        :name="field.name"
        v-mask="field.mask"
        :mask="field.mask"
        :required="field.required"
        :label="field.label"
        :position="field.position"
        :maxlength="field.maxlength"
        :minlength="field.minlength"
        :pattern="field.pattern"
        :max="field.max"
        :min="field.min"
        :data="field.data"
        :values="field.values"
        :hint="field.hint"
        :icon="field.icon"
        :message="field.message"
        :value="field.value"
        :params="field.params"
        :model="model"
        :field="field"
        :i="i"
        :fields="schema_test"
        :changeAdd="changeAdd"
        :def_key="field.def_key"
        :changeRemove="changeRemove"
        :quantityOfProperty="quantityOfProperty"
        @input="updateField()"
      >
      </component>
    </section>
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
      <b-button
        id="right-button_2"
        type="is-dark"
        v-show="lastStep"
        @click="sendData"
        >Скачать договор (.docx)</b-button
      >
    </section>
  </div>
</template>

<script>
import Input from "@/formElements/Input.vue";
import Input_prop from "@/formElements/Input_prop.vue";
import Email from "@/formElements/Email.vue";
import Number from "@/formElements/Number.vue";
import Number_prop from "@/formElements/Number_prop.vue";
import Datepicker from "@/formElements/Datepicker.vue";
import Datepicker_prop from "@/formElements/Datepicker_prop.vue";
import Datepicker_prop_range from "@/formElements/Datepicker_prop_range.vue";
import Select from "@/formElements/Select.vue";
import Select_prop from "@/formElements/Select_prop.vue";
import MultiSelect from "@/formElements/MultiSelect.vue";
import Autocomplete from "@/formElements/Autocomplete.vue";
import pseudoLabel from "@/formElements/pseudoLabel.vue";
import GeneratedField from "@/formElements/GeneratedField.vue";
import GeneratedFieldFL from "@/formElements/GeneratedFieldFL.vue";
import Button_add from "@/formElements/Button_add.vue";
import Button_remove from "@/formElements/Button_remove.vue";
import AwesomeMask from "awesome-mask";

const rubles = require("rubles").rubles;

export default {
  directives: {
    mask: AwesomeMask,
  },
  components: {
    Input,
    Datepicker,
    Select,
    MultiSelect,
    pseudoLabel,
    Email,
    Number,
    Autocomplete,
    GeneratedField,
    GeneratedFieldFL,
    Button_add,
    Button_remove,
    Select_prop,
    Input_prop,
    Number_prop,
    Datepicker_prop,
    Datepicker_prop_range
  },
  props: [
    "config",
    "select_first_step",
    "select_second_step",
    "select_third_step",
    "schema_test",
    "model",
    "sendData",
    "changeAdd",
    "changeRemove",
    "quantityOfProperty",
  ],
  data() {
    return {
      i: 0,
      valid: null,
      ls: true,
      lr: false,
      dl: false,
      dis: false,
      lastStep: false,
      counter: false,
      checked: false
    };
  },
  methods: {
    updateField() {},
    fieldVisible(field) {
      if (field.visible == null) {
        return true;
      } else {
        if (
          this.model[field.visible.dep_name] &&
          field.visible.dep_type == "Input"
        ) {
          return true;
        }
        if (
          this.model[field.visible.dep_name] &&
          field.visible.dep_type == "Select" &&
          JSON.stringify(field.visible.dep_check).match(
            this.model[field.visible.dep_name]
          )
        ) {
          return true;
        }
        if (
          this.model[field.visible.dep_name] &&
          field.visible.dep_type == "MultiSelect" &&
          JSON.stringify(this.model[field.visible.dep_name]).match(
            field.visible.dep_check
          )
        ) {
          return true;
        }
        if (
          this.model[field.visible.dep_name] &&
          field.visible.dep_type == "Generatedfield" &&
          JSON.stringify(this.model[field.visible.dep_name_payment]).match(
            field.visible.dep_check
          )
        ) {
          return true;
        }
        if (
          this.model.propertyName[field.def_key]
          &&
          field.visible.dep_type == "Select_2" 
          && JSON.stringify(field.visible.dep_check).match(JSON.stringify(this.model.propertyName[field.def_key]))
        ) {
          return true;
        }
        if (
          this.model.propertyName[field.def_key]
          &&
          field.visible.dep_type == "Multi" 
          && JSON.stringify(field.visible.dep_check).match(JSON.stringify(this.model.propertyName[field.def_key]))
          && JSON.stringify(field.visible.dep_dogovor).match(JSON.stringify(this.select_first_step)) 
        ) {
          return true;
        }
        
        if (
          this.model[field.visible.dep_name]
          &&
          field.visible.dep_type == "Multi_payment"
          && JSON.stringify(field.visible.dep_check).match(JSON.stringify(this.model[field.visible.dep_name]))
          && JSON.stringify(field.visible.dep_dogovor).match(JSON.stringify(this.select_first_step)) 
        ) {
          return true;
        }
      }
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
  beforeUpdate() {
    if (this.model.cost) {
      this.model.costWSum = rubles(this.model.cost);
    }
    if (this.model.nal) {
      this.model.nalWSum = rubles(this.model.nal);
    }
    if (this.model.bznal) {
      this.model.bznalWSum = rubles(this.model.bznal);
    }
    if (this.model.paySumA) {
      this.model.paySumAWSum = rubles(this.model.paySumA);
    }
    if (this.model.paySumIB) {
      this.model.paySumIBWSum = rubles(this.model.paySumIB);
    }
    if (this.model.paySumFL) {
      this.model.paySumFLWSum = rubles(this.model.paySumFL);
    }
    if (this.model.paySumMatCap) {
      this.model.paySumMatCapWSum = rubles(this.model.paySumMatCap);
    }
    if (this.model.paySumRS) {
      this.model.paySumRSWSum = rubles(this.model.paySumRS);
    }
    if (this.model.avancesum) {
      this.model.avancesumW = rubles(this.model.avancesum);
    }
    if (this.i == 0) {
      if (this.model.city && this.model.date && this.model.email) {
        this.dis = false;
      } else {
        this.dis = true;
      }
    }
    if (this.i == 1) {
      if (this.select_second_step == "ФЛ") {
        if (
          this.model.sellerFullName &&
          this.model.sellerBirthYear &&
          this.model.sellerBirthPlace &&
          this.model.sellerNationality
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }
      if (this.select_second_step == "ЮЛ") {
        if (
          this.model.sellerOrgLegalForm &&
          this.model.sellerOrgName &&
          this.model.sellerOrgPossition &&
          this.model.sellerCeoFullName
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }
    }
    if (this.i == 2) {
      if (this.select_second_step == "ФЛ") {
        if (
          this.model.sellerPassNumberFirst &&
          this.model.sellerPassNumberSec &&
          this.model.sellerPassIssuedBy &&
          this.model.sellerPassIssuedOn &&
          this.model.sellerPassIssuedBy &&
          this.model.sellerUnitCode &&
          this.model.sellerRegAddress &&
          this.model.sellerRepresent
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }
      if (this.select_second_step == "ЮЛ") {
        if (
          this.model.sellerOrgDoc &&
          this.model.sellerOrgRegAddressUR &&
          this.model.sellerOrgOGRN &&
          this.model.sellerOrgINN &&
          this.model.sellerOrgKPP &&
          this.model.sellerOrgRS &&
          this.model.sellerOrgKS &&
          this.model.sellerOrgBank &&
          this.model.sellerOrgBankBik &&
          this.model.sellerOrgTel &&
          this.model.sellerOrgPostAddress
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }
    }
    if (this.i == 3) {
      if (this.select_third_step == "ФЛ") {
        if (
          this.model.custFullName &&
          this.model.custBirthYear &&
          this.model.custBirthPlace &&
          this.model.custNationality
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }
      if (this.select_third_step == "ЮЛ") {
        if (
          this.model.custOrgLegalForm &&
          this.model.custOrgName &&
          this.model.custOrgPossition &&
          this.model.custCeoFullName
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }
    }
    if (this.i == 4) {
      if (this.select_third_step == "ФЛ") {
        if (
          this.model.custPassNumberFirst &&
          this.model.custPassNumberSec &&
          this.model.custPassIssuedBy &&
          this.model.custPassIssuedOn &&
          this.model.custUnitCode &&
          this.model.custRegAddress
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }
      if (this.select_third_step == "ЮЛ") {
        if (
          this.model.custOrgDoc &&
          this.model.custOrgRegAddressUR &&
          this.model.custOrgOGRN &&
          this.model.custOrgINN &&
          this.model.custOrgKPP &&
          this.model.custOrgRS &&
          this.model.custOrgKS &&
          this.model.custOrgBank &&
          this.model.custOrgBankBik &&
          this.model.custOrgTel &&
          this.model.custOrgPostAddress
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }
    }
    if (this.i == 5) {
      if (this.model.propertyName[this.quantityOfProperty]) {
        this.dis = false;
      } else {
        this.dis = true;
      }

      if (this.model.propertyName[this.quantityOfProperty] == "Квартира") {
        if (
          this.model.propertyNumRoom[this.quantityOfProperty]  &&
          this.model.propertyLevel[this.quantityOfProperty]  &&
          this.model.propertyFloorArea[this.quantityOfProperty]  &&
          this.model.propertyAddress[this.quantityOfProperty]  &&
          this.model.propertyUniqueIdentifier[this.quantityOfProperty] &&
          this.model.propertyDoc[this.quantityOfProperty] &&
          this.model.propertyRegDocDate[this.quantityOfProperty] &&
          this.model.propertyRegDocNumber[this.quantityOfProperty]
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }

      if (this.model.propertyName[this.quantityOfProperty] == "Земельный участок") {
        if (
          this.model.propertyLandCat[this.quantityOfProperty] &&
          this.model.propertyLandUsed[this.quantityOfProperty] &&
          this.model.propertyFloorArea[this.quantityOfProperty] &&
          this.model.propertyAddress[this.quantityOfProperty] &&
          this.model.propertyUniqueIdentifier[this.quantityOfProperty] &&
          this.model.propertyDoc[this.quantityOfProperty] &&
          this.model.propertyRegDocDate[this.quantityOfProperty] &&
          this.model.propertyRegDocNumber[this.quantityOfProperty]
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }
      if (this.model.propertyName[this.quantityOfProperty] == "Жилой дом") {
        if (
          this.model.propertyFloorArea[this.quantityOfProperty] &&
          this.model.propertyNumRoom[this.quantityOfProperty] &&
          this.model.propertyUniqueIdentifier[this.quantityOfProperty] &&
          this.model.propertyLevel[this.quantityOfProperty] &&
          this.model.propertyAddress[this.quantityOfProperty] &&
          this.model.propertyDoc[this.quantityOfProperty] &&
          this.model.propertyRegDocDate[this.quantityOfProperty] &&
          this.model.propertyRegDocNumber[this.quantityOfProperty]
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }
    }
    if (this.i == 6) {
      if (this.model.cost && this.model.payMethod.length !== 0) {
        this.lastStep = true;
      } else {
        this.lastStep = false;
      }
    }
    if (this.i < 6) {
      this.lastStep = false;
    }
  },
};
</script>

<style scoped>
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
.sec1 {
  padding-bottom: 2%;
}
.hiden {
  display: none;
}
#right-button_2 {
    float: right;
  }
</style>