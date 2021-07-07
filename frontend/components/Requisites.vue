<template>
  <div id="signature">
        <div class="lf" v-if="select_second_step == 'ФЛ'">
          <p>
            <b>{{ seller }}:</b>
          </p>
          <p>
            {{ data_model.sellerFullName }}
          </p>
        </div>
        <div class="rf" v-if="select_third_step == 'ФЛ'">
          <p>
            <b>{{ buyer }}:</b>
          </p>
          <p>
            {{ data_model.custFullName }}
          </p>
        </div>
        <div class="lf" v-if="select_second_step == 'ЮЛ'">
          <p>
            <b>{{ seller }}:</b>
          </p>
          <p>
            {{ data_model.sellerOrgLegalForm }} "{{
              data_model.sellerOrgName
            }}"
          </p>
          <p>
            Юридический адрес: {{ data_model.sellerOrgRegAddressUR }}
          </p>
          <p>ОГРН: {{ data_model.sellerOrgOGRN }}</p>
          <p>ИНН: {{ data_model.sellerOrgINN }}</p>
          <p>КПП: {{ data_model.sellerOrgKPP }}</p>
          <p>Р/С: {{ data_model.sellerOrgRS }}</p>
          <p>КС: {{ data_model.sellerOrgKS }}</p>
          <p>Банк: {{ data_model.sellerOrgBank }}</p>
          <p>БИК: {{ data_model.sellerOrgBankBik }}</p>
          <p>Номер телефона: {{ data_model.sellerOrgTel }}</p>
          <p>
            Почтовый адрес: {{ data_model.sellerOrgPostAddress }}
          </p>
          <p>В лице: {{ data_model.sellerCeoFullName }}</p>
        </div>
        <div class="rf" v-if="select_third_step == 'ЮЛ'">
          <p>
            <b>{{ buyer }}:</b>
          </p>
          <p>
            {{ data_model.custOrgLegalForm }} "{{
              data_model.custOrgName
            }}"
          </p>
          <p>
            Юридический адрес: {{ data_model.custOrgRegAddressUR }}
          </p>
          <p>ОГРН: {{ data_model.custOrgOGRN }}</p>
          <p>ИНН: {{ data_model.custOrgINN }}</p>
          <p>КПП: {{ data_model.custOrgKPP }}</p>
          <p>Р/С: {{ data_model.custOrgRS }}</p>
          <p>КС: {{ data_model.custOrgKS }}</p>
          <p>Банк: {{ data_model.custOrgBank }}</p>
          <p>БИК: {{ data_model.custOrgBankBik }}</p>
          <p>Номер телефона: {{ data_model.custOrgTel }}</p>
          <p>Почтовый адрес: {{ data_model.custOrgPostAddress }}</p>
          <p>В лице: {{ data_model.custFullName }}</p>
        </div>
      </div>
</template>

<script>

export default {
  name: "dogovor_kupli_prodazhi",
  props: {
    model: Object,
    schema: Object,
    select_second_step: String,
    select_third_step: String,
    plain: Function,
    add: Boolean,
    seller: String,
    buyer: String
  },
  data() {
    return {
      data_model: null
    }
  },
  created() {
    this.data_model = JSON.parse(JSON.stringify(this.model))
    for (let i in this.data_model) {
      this.data_model[i] = '_________________';
      this.data_model.propertyRegDocDate = [];
    }
  },
  watch: {
    model: {
      deep: true,
      handler(newValue) {
        for (let i in newValue) {
          if (newValue[i]) {
            this.data_model[i] = newValue[i]
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