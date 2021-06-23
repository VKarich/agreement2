<template>
  <div>
    <div class="unselectable" id="unselectable">
      <div id="header">
        <p>
          <strong
            >{{ textFromAgreement.dogovor_arendy.main.header_title }}
            {{ data_model.number }}</strong
          >
        </p>
        <p>
          <strong> {{ data_model.propertyName }}</strong>
          <!-- <strong v-for="(property, index) in data_model.propertyName" :key="index">{{ property + ' ' }}</strong> -->
          </p>
      </div>
      <div id="date">
        <p id="left">
          <strong
            >{{ textFromAgreement.dogovor_arendy.main.city }}
            {{ data_model.city.firstLetterCaps() }}</strong
          >
        </p>
        <p id="right">
          <strong
            >{{ textFromAgreement.dogovor_arendy.main.date }}
            {{ data_model.date }}</strong
          >
        </p>
      </div>
      <div class="aSide">
        {{ sideA.text_main_info }}
        <span
          v-if="
            JSON.stringify(data_model.sellerRepresent).match(
              JSON.stringify(sideA.add_check_phrase)
            ) ||
            JSON.stringify(data_model.sellerOrgDoc)
              .toLowerCase()
              .match(JSON.stringify(sideA.add_check_phrase))
          "
        >
          {{ sideA.text_add_info }}</span
        >{{ sideA.text_main }}
      </div>

      <div class="bSide">
        {{ sideB.text_main_info }}
        <span
          v-if="
            JSON.stringify(data_model.custRepresent).match(
              JSON.stringify(sideB.add_check_phrase)
            ) ||
            JSON.stringify(data_model.custOrgDoc)
              .toLowerCase()
              .match(JSON.stringify(sideB.add_check_phrase))
          "
        >
          {{ sideB.text_add_info }}</span
        >{{ sideB.text_main }}
      </div>

      <div class="paragraphs" v-for="(pararaph, index) in textFromAgreement.dogovor_arendy.paragraphs" :key="index">
        <p id="header"><strong>{{ pararaph.header_title }}</strong></p>
        <p class="paragraph" v-for="(n, index) in pararaph.main_text" :key="index">{{ pararaph.main_text[index] }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import dogovor from "../../dogovor_arendy.json";
import Vue from "vue";

const plural = require("plural-ru");

String.prototype.firstLetterCaps = function () {
  return this.charAt(0).toUpperCase() + this.slice(1);
};

Vue.filter("date_corr", function (value) {
  if (value instanceof Date) return value.toLocaleDateString();
});

Vue.filter("str_corr", function (value) {
  if (!value) return "_________________";
  return value;
});

let rubles = require("rubles").rubles;
Vue.filter("rubles", function (value) {
  if (value == "_________________") return "_________________";
  return rubles(value);
});

Vue.filter("months", function (value) {
  return plural(value, "месяц", "месяца", "месяцев");
});

Vue.filter("days", function (value) {
  return plural(value, "день", "дня", "дней");
});

export default {
  name: "dogovor_kupli_prodazhi",
  props: {
    model: Object,
    schema: Object,
    select_first_step: String,
    select_second_step: String,
    select_third_step: String,
    plain: Function,
    add: Boolean,
    quantityOfProperty: Number,
  },
  data() {
    return {
      data_model: null,
      textFromAgreement: dogovor,
      sideA: {},
      sideB: {},
      aChoise: "",
      bChoise: "",
      agreement: null,
    };
  },
  beforeUpdate() {
    for (let i in this.textFromAgreement.dogovor_arendy.sides.SideA[
      this.aChoise
    ]) {
      let text =
        this.textFromAgreement.dogovor_arendy.sides.SideA[this.aChoise][i];
      let text_B = this.textFromAgreement.dogovor_arendy.sides.SideB[this.bChoise][i];
      let split = text.split(" ");
      let split_B = text_B.split(" ");

      for (let i in split) {
        if (split[i].match("A_0")) {
          split[i] = split[i].replace(
            "A_0",
            this.textFromAgreement.dogovor_arendy.sides.SideA.label[0]
          );
        }
        if (split[i].match("A_1")) {
          split[i] = split[i].replace(
            "A_1",
            this.textFromAgreement.dogovor_arendy.sides.SideA.label[1]
          );
        }
        if (split[i].match("seller")) {
          let commaClear = split[i].replace(/[,]/g, "");
          split[i] = this.data_model[commaClear];
        }
      }
      
      for (let i in split_B) {
        if (split_B[i].match("A_0")) {
          split_B[i] = split_B[i].replace(
            "A_0",
            this.textFromAgreement.dogovor_arendy.sides.SideB.label[0]
          );
        }
        if (split_B[i].match("A_1")) {
          split_B[i] = split_B[i].replace(
            "A_1",
            this.textFromAgreement.dogovor_arendy.sides.SideB.label[1]
          );
        }
        if (split_B[i].match('cust')) {
          let commaClear_B = split_B[i].replace(/[,]/g, "");
          split_B[i] = this.data_model[commaClear_B];
        }
      }
      this.sideA[i] = split.join(" ");
      this.sideB[i] = split_B.join(" ");
    }
  },
  created() {
    this.data_model = JSON.parse(JSON.stringify(this.model));
    for (let i in this.data_model) {
      this.data_model[i] = "_________________";
      this.data_model.propertyRegDocDate = [];
    }
  },
  watch: {
    select_second_step(newValue) {
      if (newValue == "ФЛ") {
        this.aChoise = "fl";
      } else this.aChoise = "ul";
    },
    select_third_step(newValue) {
      if (newValue == "ФЛ") {
        this.bChoise = "fl";
      } else this.bChoise = "ul";
    },
    model: {
      deep: true,
      handler(newValue) {
        for (let i in newValue) {
          if (newValue[i]) {
            this.data_model[i] = newValue[i];
          }
          if (newValue[i] instanceof Date) {
            this.data_model[i] = newValue[i].toLocaleDateString();
          }
        }
      },
    },
  },
};
</script>

<style scoped>
div,
table {
  margin-bottom: 20px;
}
h1 {
  text-align: center;
}
#header {
  text-align: center;
  margin-bottom: 20px;
}
.paragraph {
  margin-bottom: 20px;
}
strong {
  text-align: center;
}
#signature {
  display: table;
  width: 100%;
}
.lf {
  display: table-cell;
  float: left;
  max-width: 50%;
}
.rf {
  display: table-cell;
  float: right;
  max-width: 50%;
}
#main {
  display: block;
}
.unselectable {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Chrome/Safari/Opera */
  -khtml-user-select: none; /* Konqueror */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently*/
  opacity: 0.8;
}
.watermark {
  opacity: 0.5;
  color: rgb(236, 29, 29);
  position: absolute;
  top: auto;
  left: 80%;
}
.flou {
  color: transparent;
  text-shadow: 0 0 8px #999;
  font-weight: normal;
  filter: blur(5px);
  -webkit-filter: blur(5px);
}
table {
  border: black solid 1px;
  width: 100%;
  table-layout: auto;
  text-align: center;
}
tr td {
  border: black solid 1px;
  padding: 10px;
  text-align: center;
}
.receipt {
  padding-top: 60px;
}
</style>
