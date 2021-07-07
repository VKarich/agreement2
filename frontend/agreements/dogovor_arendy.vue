<template>
  <div>
    <div id="header">
        <p><strong>{{String(textFromAgreement.dogovor_arendy.main.header_title).format()
          }}</strong>
        </p>
        <p><strong v-for="(property, index) in data_model.propertyName"
            :key="index">{{ property + " " }}</strong>
        </p>
      </div>
      <div id="date">
        <p id="left">
          <strong>{{ textFromAgreement.dogovor_arendy.main.city.format() }}</strong>
        </p>
        <p id="right">
          <strong>{{ textFromAgreement.dogovor_arendy.main.date.format() }}</strong>
        </p>
      </div>
    <div>
      <Sides :model="model" :select_second_step="select_second_step" :select_third_step="select_third_step" />
    </div>
    <div v-for="(paragraph, index) in textFromAgreement.dogovor_arendy.paragraphs" :key="index">
        <p id="header" v-if="check_header(paragraph, index)"><strong> {{ index.replace("paragraph_", "") + "." }} {{ paragraph.header_title }} </strong></p>
        <div v-for="(text, i) in paragraph.main_text.slice(0)" :key="i">
          <p v-if="check(text, paragraph, i, index)" v-html="index.replace('paragraph_', '') + '.' + (i + 1)  + '.' + ' ' + text.format()">
          </p>
        </div>
    </div>
    <div>
      <Requisites :seller="seller" :buyer="buyer" :model="model" :select_second_step="select_second_step" :select_third_step="select_third_step" />
    </div>
  </div>
</template>

<script>
import model from "../../model.json";
import dogovor from "/../dogovor_arendy.json";
import Sides from '../components/Sides.vue'
import Requisites from '../components/Requisites.vue'

const numeralize = require('numeralize-ru');
const rubles = require("rubles").rubles;
let numeral = require('numeral');
const plural = require("plural-ru");

String.prototype.format = function () {
  let a = this;
  for (let k in model) {
    if (model[k] && model[k].length !== 0) {
      a = a.replace("{{ " + k + " }}", model[k]);
    } else {
      a = a.replace("{{ " + k + " }}", "____________");
    }
  }
  if (a.match('undefined')) {
    a = a.replaceAll('undefined', '____________')
  }
  return a;
};

function isInteger(num) {
  return (num ^ 0) === num;
}

function ordinal( cardinal ) {
    var ordinals = [ '____', 'первого', 'второго', 'третьего', 'четвертого', 'пятого', 'шестого', 'седьмого', 'восьмого', 'девятого', 'десятого', 'одиннадцатого', 'двенадцатого', 'тринадцатого', 'цетырнадцатого', 'пятнадцатого', 'шестнадцатого', 'семнадцатого', 'восемнадцатого', 'девятнадцатого', 'двадцатого'];
    var tens = {
        20: 'двадцать',
        30: 'тридцать',
    };
    var ordinalTens = {
        30: 'тридцатого',
    };

    if( cardinal <= 20 ) {                    
        return ordinals[ cardinal ];
    }

    if( cardinal % 10 === 0 ) {
        return ordinalTens[ cardinal ];
    }

    return tens[ cardinal - ( cardinal % 10 ) ] + ' ' + ordinals[ cardinal % 10 ];
}

export default {
  name: "dogovor_kupli_prodazhi",
  props: {
    model: Object,
    schema: Array,
    select_first_step: String,
    select_second_step: String,
    select_third_step: String,
  },
  components: {
    Sides,
    Requisites
  },
  data() {
    return {
      data_model: null,
      textFromAgreement: dogovor,
      seller: 'Арендодатель',
      buyer: 'Арендатор'
    };
  },
  methods: {
    check(text, paragraph, i) {
      for (let i in this.model.propertyName) {
        if (this.model.propertyName[i] == 'Квартира') {
          this.model.property[i] = ` ${this.model.propertyName[i]}, кадастровый номер: ${this.model.propertyUniqueIdentifier[i]}, общей площадью ${this.model.propertyFloorArea[i]} м2, количество комнат: ${this.model.propertyNumRoom[i]}, этаж: ${this.model.propertyLevel[i]}, расположенная по адресу ${this.model.propertyAddress[i]}`;
          this.model.forWhat = `для проживания в нем Арендатора`;
          this.model.forNonLiving = ` `;
        }
        if (this.model.propertyName[i] == 'Земельный участок') {
          this.model.property[i] = ` ${this.model.propertyName[i]}, кадастровый номер: ${this.model.propertyUniqueIdentifier[i]}, общей площадью ${this.model.propertyFloorArea[i]} м2, категория земель: ${this.model.propertyLandCat[i]}, разрешенное использование: ${this.model.propertyLandUsed[i]}, расположенный по адресу ${this.model.propertyAddress[i]}`;
          this.model.forWhat = `для проживания в нем Арендатора`;
          this.model.forNonLiving = ` `;
        }
        if (this.model.propertyName[i] == 'Жилой дом') {
          this.model.property[i] = ` ${this.model.propertyName[i]}, кадастровый номер: ${this.model.propertyUniqueIdentifier[i]}, общей площадью ${this.model.propertyFloorArea[i]} м2, количество комнат: ${this.model.propertyNumRoom[i]}, количество этажей: ${this.model.propertyLevel[i]}, расположенный по адресу ${this.model.propertyAddress[i]}`;
          this.model.forWhat = `для проживания в нем Арендатора`;
          this.model.forNonLiving = ` `;
        }
        if (this.model.propertyName[i] == 'Нежилое здание' && !JSON.stringify(this.model.propertyName).match('участок') && !JSON.stringify(this.model.propertyName).match('Квартира') && !JSON.stringify(this.model.propertyName).match('Жилой')) {
          this.model.property[i] = ` ${this.model.propertyName[i]}, кадастровый номер: ${this.model.propertyUniqueIdentifier[i]}, общей площадью ${this.model.propertyFloorArea[i]} м2, количество этажей: ${this.model.propertyLevel[i]}, расположенное по адресу ${this.model.propertyAddress[i]}`;
          this.model.forWhat = `для размещения ${model.propertySpecPurpose}`;
          this.model.forNonLiving = `сведения об объеме поставляемой энергии (предельной мощности сети),`;
        }
        if (this.model.propertyName[i] == 'Нежилое помещение' && !JSON.stringify(this.model.propertyName).match('участок') && !JSON.stringify(this.model.propertyName).match('Квартира') && !JSON.stringify(this.model.propertyName).match('Жилой')) {
          this.model.property[i] = ` ${this.model.propertyName[i]}, кадастровый номер: ${this.model.propertyUniqueIdentifier[i]}, общей площадью ${this.model.propertyFloorArea[i]} м2, этаж: ${this.model.propertyLevel[i]}, расположенное по адресу ${this.model.propertyAddress[i]}`;
          this.model.forWhat = `для размещения ${model.propertySpecPurpose}`;
          this.model.forNonLiving = `сведения об объеме поставляемой энергии (предельной мощности сети),`;
        }
      }

      if (text.match('автоматически продлевается на тот')) {
        if (JSON.stringify(model.contractExtention).match('Нет') || model.contractExtention.length < 1) {
          paragraph.add_info[i] = 'false'
        } else {
          paragraph.add_info[i] = 'true'
        }
      }

      if (text.match('Арендная плата вносится Арендатором') || text.match('Сумма любого произведенного Арендатором')) {
        if (this.select_second_step == 'ЮЛ' && this.select_third_step == 'ЮЛ') {
          paragraph.add_info[i] = 'true'
        } else {
          paragraph.add_info[i] = 'false'
        }
      }

      if (text.match('Внесение платы за коммунальные услуги')) {
        if (model.publicServices == 'Нет') {
          paragraph.add_info[i] = 'false'
        }
        if (model.publicServices == 'Да') {
          paragraph.add_info[i] = 'true'
        }
      }

      if (text.match('производить текущий ремонт')) {
        if (model.construction == 'отсутствует') {
          paragraph.add_info[i] = 'false'
        } else {
          paragraph.add_info[i] = 'true'
        }
      }

      if (text.match('сведения о количестве и составе отходов')) {
        if (JSON.stringify(model.propertyName).includes('Нежилое') && model.waste == 'Да' ) {
          paragraph.add_info[i] = 'true'
        } else {
          paragraph.add_info[i] = 'false'
        }
      }

      text.match('удерживать Имущество')

      if (text.match('субаренду')) {
        if (model.sublease == 'Да') {
          paragraph.add_info[i] = 'true'
        } else {
          paragraph.add_info[i] = 'false'
        }
      }

      if (text.match('удерживать Имущество')) {
        if (model.catch_property == 'Да') {
          paragraph.add_info[i] = 'true'
        } else {
          paragraph.add_info[i] = 'false'
        }
      }

      if (text.match('капитальный ремонт Имущества')) {
        if (model.repairs == 'Да') {
          paragraph.add_info[i] = 'true'
        } else {
          paragraph.add_info[i] = 'false'
        }
      }

      if (text.match('Арендатор имеет право с письменного') || text.match('Размещать в арендуемом') || text.match('Размещать рекламу') || text.match('Осуществлять за свой счёт перепланировку')  || text.match('Устанавливать за свой счет') || text.match('Арендатор не вправе') || text.match('Хранить в арендуемом') || text.match('Создавать препятствия')  || text.match('Без согласования')  || text.match('Устанавливать и эксплуатировать') || text.match('стороны назначают из числа своих')) {
        if (JSON.stringify(model.propertyName).includes('Нежилое')) {
          paragraph.add_info[i] = 'true'
        } else {
          paragraph.add_info[i] = 'false'
        }
      }

      if (text.match('сведений о полном фирменном наименовании')) {
        if (this.select_second_step == 'ЮЛ' || this.select_third_step == 'ЮЛ') {
          paragraph.add_info[i] = 'true'
        } else {
          paragraph.add_info[i] = 'false'
        }
      }
      

      if (text.match('стоимость улучшений Имущества')) {
        if (model.compensation == 'Да') {
          paragraph.add_info[i] = 'true'
        } else {
          paragraph.add_info[i] = 'false'
        }
      }

      if (text.match('При нецелевом использовании')) {
        if (model.misuse == 'Да') {
          paragraph.add_info[i] = 'true'
        } else {
          paragraph.add_info[i] = 'false'
        }
      }

      if (text.match('центрального отопления, электроснабжения')) {
        if (model.liability == 'Да') {
          paragraph.add_info[i] = 'false'
        } else {
          paragraph.add_info[i] = 'true'
        }
      }

      if (text.match('Арендодатель вправе в любое время')) {
        if (model.arg_change == 'Убрать') {
          paragraph.add_info[i] = 'false'
        } else {
          paragraph.add_info[i] = 'true'
        }
      }

      if (text.match('Арендатор, надлежащим образом')) {
        if (model.arg_change2 == 'Убрать') {
          paragraph.add_info[i] = 'false'
        } else {
          paragraph.add_info[i] = 'true'
        }
      }

      if (text.match('своего долга третьему') || text.match('Арендатором своего долга')) {
        if (model.arg_change3 == 'Убрать') {
          paragraph.add_info[i] = 'false'
        } else {
          paragraph.add_info[i] = 'true'
        }
      }

      if (text.match('конфиденциальны и не подлежат') || text.match('принимают все необходимые')) {
        if (model.confidentiality == 'Убрать') {
          paragraph.add_info[i] = 'false'
        } else {
          paragraph.add_info[i] = 'true'
        }
      }

      if (paragraph.add_info[i] == 'true' || !paragraph.add_info[i]) {
        paragraph.add_info[i] = 'true';
        return true
      } else {
        return false
      }
    },
    check_header(paragraph) {
      if (paragraph.header_title == 'КОММУНАЛЬНЫЕ УСЛУГИ') {
        if (model.publicServices == 'Нет') {
          return false
        } else {
          return true
        }
      } if (paragraph.header_title == 'ПОРЯДОК ИЗМЕНЕНИЯ ДОГОВОРА В ЧАСТИ УСЛОВИЯ О РАЗМЕРЕ АРЕНДНОЙ ПЛАТЫ ПО СОГЛАШЕНИЮ СТОРОН') {
          if (model.arg_change == 'Убрать') {
            return false
          } else {
            return true
        }
      } if (paragraph.header_title == 'ПРЕИМУЩЕСТВЕННОЕ ПРАВО НА ЗАКЛЮЧЕНИЕ ДОГОВОРА НА НОВЫЙ СРОК. ВОЗОБНОВЛЕНИЕ ДОГОВОРА') {
          if (model.arg_change2 == 'Убрать') {
            return false
          } else {
            return true
        }
      } if (paragraph.header_title == 'ПЕРЕМЕНА ЛИЦ В ДОГОВОРЕ И В ОБЯЗАТЕЛЬСТВАХ ИЗ ДОГОВОРА') {
          if (model.arg_change3 == 'Убрать') {
            return false
          } else {
            return true
        }
      } if (paragraph.header_title == 'КОНФИДЕНЦИАЛЬНОСТЬ') {
          if (model.confidentiality == 'Убрать') {
            return false
          } else {
            return true
        }
      } return true
    }
  },
  beforeUpdate() {
    if (model.cost) {
      model.cost_corr = numeral(model.cost).format('₽0,0.00');
    }

    if (model.propertyRentMonths.length !== 0) {
      model.pluralMonths = plural(
        model.propertyRentMonths,
        "месяц",
        "месяца",
        "месяцев"
      );
    } else {
      model.pluralMonths = "месяца";
    }
    model.add_info = " ";
    for (let i in model.propertyName) {
      if (model.propertyRentMonths <= 11) {
        if (
          model.propertyName[i] == "Нежилое здание" ||
          model.propertyName[i] == "Нежилое помещение"
        ) {
          model.add_info =
            "Договор не подлежит государственной регистрации в силу п. 2 ст. 651 Гражданского кодекса РФ.";
        } else {
          model.add_info = " ";
        }
        if (model.propertyName[i] == "Земельный участок") {
          model.add_info =
            " Договор не подлежит государственной регистрации в силу п.2 ст.26 Земельного кодекса РФ.";
        }
      } else {
        if (model.propertyName[i] == "Земельный участок") {
          model.add_info =
            " Договор подлежит государственной регистрации в силу п.2 ст.26 Земельного кодекса РФ.";
        } else {
          model.add_info =
            " Договор подлежит государственной регистрации в силу п.2 ст.651 Гражданского кодекса РФ.";
        }
      }
    }
  },
  created() {
    this.schema[6].fields[0].label = 'Сумма ежемесячной арендной платы:'
    this.data_model = JSON.parse(JSON.stringify(this.model));
    for (let i in this.data_model) {
      this.data_model[i] = "_________________";
      this.data_model.propertyRegDocDate = [];
    }
  },
  computed: {
    nds_() {
      if (this.model.cost) {
        return (this.model.cost * 20 / 120).toFixed(2)
      } return 0
    }
  },
  watch: {
    model: {
      deep: true,
      handler(newValue) {
        for (let i in newValue) {
          if (newValue[i]) {
            this.data_model[i] = newValue[i];
            if (i == 'nds') {
              if (newValue[i] == 'Без учета НДС') {
                model.nds_expanded = ', без учета налога на добавленную стоимость, а равно - любой другой косвенный налог, сбор или пошлину, которыми облагаются или могут быть обложены этот платёж в соответствии с требованиями законодательства Российской Федерации, при этом такие налоги должны уплачиваться (когда это применимо) в установленном законом размере, сверх сумм, указанных в Договоре.'
              }
              if (newValue[i] == 'С учетом НДС') {
                model.ndsWSum = rubles(this.nds_)
                model.nds_expanded = ` с учетом налога на добавленную стоимость в размере ${numeral(this.nds_).format('₽0,0.00')} (${model.ndsWSum})`
              }
            }
            if (model.sides !== 'ЮЛЮЛ') {
              model.nds_expanded = '.'
            }
            if (model.paymentDueDate == 'не позднее трех календарных дней') {
              model.paymentDueDate_expanded = 'в срок не позднее трех календарных дней со дня предоставления Имущества Арендатору'
            } else {
              model.paymentDueDate_expanded = 'при подписании настоящего Договора'
            }
            if (model.costTermDate) {
              model.costTermDateWSum = ordinal(model.costTermDate);
              if (model.costTermDate > 31) {
                model.costTermDate = '';
                model.costTermDateWSum = '';
              }
            }
            if (model.publicServicesPayDate) {
              model.publicServicesPayDateWSum = ordinal(model.publicServicesPayDate);
              if (model.publicServicesPayDate > 31) {
                model.publicServicesPayDate = '';
                model.publicServicesPayDateWSum = '';
              }
            }
            if (model.indemnification) {
              model.indemnification_expanded = '(' + numeralize(model.indemnification, numeralize.GENDER_MASCULINE, numeralize.CASE_GENITIVE) + ') ' + plural(model.indemnification, 'дня', 'дней', 'дней');
              if (model.indemnification > 31) {
                model.indemnification = '';
                model.indemnification_expanded = '';
              }
            }
            if (model.transferAcceptanceCertificateDate) {
              model.transferAcceptanceCertificateDate_expanded = '(' + numeralize(model.transferAcceptanceCertificateDate, numeralize.GENDER_MASCULINE, numeralize.CASE_GENITIVE) + ') ' + plural(model.transferAcceptanceCertificateDate, 'дня', 'дней', 'дней');
              if (model.transferAcceptanceCertificateDate > 31) {
                model.transferAcceptanceCertificateDate = '';
                model.transferAcceptanceCertificateDate_expanded = '';
              }
            }
            if (model.fine) {
              if (isInteger(Number(model.fine))) {
                model.fineWSum = numeralize(model.fine, numeralize.GENDER_MASCULINE, numeralize.CASE_GENITIVE) + ' ' + plural(Number(model.fine), 'процента', 'процентов', 'процентов')
              }
              if (!isInteger(Number(model.fine))) {
                let a = model.fine.split('.');
                if ((a[0] < 1)) {
                  model.fineWSum = 'ноль целых ' + numeralize(a[1], numeralize.GENDER_FEMININE, numeralize.CASE_GENITIVE) + ' ' + plural(Number(a[1]), 'десятой', 'десятых', 'десятых') + ' процента'
                }
                if ((a[0] >= 1)) {
                  model.fineWSum = numeralize(a[0], numeralize.GENDER_MASCULINE, numeralize.CASE_GENITIVE) + ' и ' + numeralize(a[1], numeralize.GENDER_FEMININE, numeralize.CASE_GENITIVE) + ' ' + plural(Number(a[1]), 'десятой', 'десятых', 'десятых') + ' процента'
                }
                if (a[1] > 9) {
                  model.fine = '';
                  model.fineWSum = '';
                }
              }
            }
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
