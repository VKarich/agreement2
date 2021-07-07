<template>
  <div>
    <div>
        <div v-if="select_second_step == 'ФЛ'">
          <p>
            {{ data_model.sellerFullName }},
            {{ data_model.sellerBirthYear }} года
            рождения, место рождения:
            {{ data_model.sellerBirthPlace }}, гражданство:
            {{ data_model.sellerNationality }}, паспорт серия:
            {{ data_model.sellerPassNumberFirst }} номер:
            {{ data_model.sellerPassNumberSec }}, выдан:
            {{ data_model.sellerPassIssuedBy.toUpperCase() }}
            {{ data_model.sellerPassIssuedOn }}, код
            подразделения: {{ data_model.sellerUnitCode }},
            зарегистрированный по адресу
            {{ data_model.sellerRegAddress }}
            <span v-if="JSON.stringify(data_model.sellerRepresent).match('Да, от имени Продавца действует представитель')">
            , в лице Представителя на основании доверенности №{{ data_model.sellerRepresentDocNum }}
            от {{ data_model.sellerRepresentDocDate }}, выданной
            {{ data_model.sellerRepresentDocBy }} на имя
            {{ data_model.sellerRepresentFullName }}. Данные доверенности:
            Паспортные данные: серия:
            {{ data_model.sellerRepresentPassNumFirst }}, номер:
            {{ data_model.sellerRepresentDocPassNumSec }}, выдан:
            {{ data_model.sellerRepresentPassIssuedBy }},
            {{ data_model.sellerRepresentPassDate }}, код подразделения:
            {{ data_model.sellerRepresentUnitCode }}, адрес регистрации:
            {{ data_model.sellerRepresentRegAddress }}</span>, именуемый в дальнейшем
            <b>«Арендодатель»</b>, с одной стороны, и
          </p>
        </div>
        <div v-else-if="select_second_step == 'ЮЛ'">
          <p>
            <b
              >{{ data_model.sellerOrgLegalForm }} "{{
                data_model.sellerOrgName.toUpperCase()
              }}"</b
            >
            в лице {{ data_model.sellerOrgPossition }}
            {{ data_model.sellerCeoFullName }}, действующего на
            основании {{ data_model.sellerOrgDoc.firstLetterCaps() }}
            <span v-if="JSON.stringify(data_model.sellerOrgDoc).toLowerCase().match('доверенности')">
            №{{ data_model.sellerOrgDocNum }} от
            {{ data_model.sellerOrgDocDate }}.
            <br>
            Паспортные данные представителя: серия:
            {{ data_model.sellerOrgDocPassNumFirst }}, номер:
            {{ data_model.sellerOrgDocPassNumSec }}, выдан:
            {{ data_model.sellerOrgPassIssuedBy }},
            {{ data_model.sellerOrgDocPassDate }}, код подразделения:
            {{ data_model.sellerOrgUnitCode }}, адрес регистрации:
            {{ data_model.sellerOrgRegAddress }},</span> с одной стороны, и
          </p>
        </div>
      </div>
      <br>
      <div v-if="select_third_step == 'ФЛ'">
        <p>
          {{ data_model.custFullName }},
          {{ data_model.custBirthYear }} года рождения,
          место рождения: {{ data_model.custBirthPlace }},
          гражданство: {{ data_model.custNationality }}, паспорт
          серия: {{ data_model.custPassNumberFirst }} номер:
          {{ data_model.custPassNumberSec }}, выдан:
          {{ data_model.custPassIssuedBy.toUpperCase() }}
          {{ data_model.custPassIssuedOn }}, код
          подразделения: {{ data_model.custUnitCode }},
          зарегистрированный по адресу
          {{ data_model.custRegAddress }}
          <span v-if="JSON.stringify(data_model.custRepresent).match('Да, от имени Покупателя действует представитель')">
            , в лице Представителя на основании доверенности №{{ data_model.custRepresentDocNum }}
            от {{ data_model.custRepresentDocDate }}, выданной
            {{ data_model.custRepresentDocBy }} на имя
            {{ data_model.custRepresentFullName }}. Данные доверенности:
            Паспортные данные: серия:
            {{ data_model.custRepresentPassNumFirst }}, номер:
            {{ data_model.custRepresentDocPassNumSec }}, выдан:
            {{ data_model.custRepresentPassIssuedBy }},
            {{ data_model.custRepresentPassDate }}, код подразделения:
            {{ data_model.custRepresentUnitCode }}, адрес регистрации:
            {{ data_model.custRepresentRegAddress }}</span>,
            именуемый в дальнейшем
          <b>«Арендатор»</b>, с другой стороны, совместно именуемые
          <b>Стороны, заключили настоящий договор аренды № {{ data_model.number }} (далее по тексту – Договор) на нижеследующих условиях:</b>
        </p>
      </div>
      <div v-else-if="select_third_step == 'ЮЛ'">
        <p>
          <b
            >{{ data_model.custOrgLegalForm }} "{{
              data_model.custOrgName.toUpperCase()
            }}"</b
          >
          в лице {{ data_model.custOrgPossition }}
          {{ data_model.custCeoFullName }}, действующего на основании
          {{ data_model.custOrgDoc.firstLetterCaps() }}
          <span v-if="JSON.stringify(data_model.custOrgDoc).toLowerCase().match('доверенности')">
            №{{ data_model.custOrgDocNum }} от
            {{ data_model.custOrgDocDate }}.
            <br>
            Паспортные данные представителя: серия:
            {{ data_model.custOrgDocPassNumFirst }}, номер:
            {{ data_model.custOrgDocPassNumSec }}, выдан:
            {{ data_model.custOrgPassIssuedBy }},
            {{ data_model.custOrgDocPassDate }}, код подразделения:
            {{ data_model.custOrgUnitCode }}, адрес регистрации:
            {{ data_model.custOrgRegAddress }}</span>, именуемый в дальнейшем
          <b>«Арендатор»</b>, с другой стороны, совместно именуемые
          <b>Стороны, заключили настоящий договор аренды № {{ data_model.number }} (далее по тексту – Договор) на нижеследующих условиях:</b>
        </p>
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

<style>

</style>