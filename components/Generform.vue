<template>
  <div class="second_selection">
    <!--v-show="!show_first"-->
    <div
      id="sec_"
      v-if="select_first_step == 'Договор купли-продажи недвижимого имущества'"
    >
      <div id="left_menu">
        <section>
          <b-progress
            :value="Math.round(ms * 16.6)"
            ref="box"
            :max="100"
            size="is-medium"
            show-value
          >
            {{ Math.round(ms * 16.6) + "%" }}
          </b-progress>
        </section>

        <!-- <form> -->

        <!--
          <vue-form-generator :schema="schema" :model="model" :options="formOptions">
          </vue-form-generator>
          -->
        <section v-if="ms == 0">
          <p class="pos" v-text="schema.groups[ms].legend"></p>
          <b-field :label="schema.groups[ms].fields[0].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[ms].fields[0].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                v-model="city"
                type="text"
                :id="schema.groups[ms].fields[0].id"
                icon="city"
                maxlength="20"
                :has-counter="counter"
                :placeholder="schema.groups[ms].fields[0].placeholder"
                :validation-message="schema.groups[ms].fields[0].message"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[ms].fields[1].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[ms].fields[1].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-datepicker
                v-model="date"
                icon="calendar-today"
                placeholder="ДД.ММ.ГГГГ"
                v-mask="'99.99.9999'"
                :locale="locale"
                editable
                :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                :firstDayOfWeek="1"
                :openOnFocus="true"
                required
                validation-message="Введите дату заключения договора"
              >
              </b-datepicker>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[ms].fields[2].label">
            <b-input
              :placeholder="schema.groups[ms].fields[2].placeholder"
              v-model="model.email"
              icon="email"
              type="email"
              maxlength="40"
              :has-counter="counter"
              required
            ></b-input>
          </b-field>
        </section>

        <section v-if="ms == 1 && select_second_step == 'ФЛ'">
          <p class="pos" v-text="schema.groups[ms].legend"></p>
          <b-field :label="schema.groups[ms].fields[0].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[ms].fields[0].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[ms].fields[0].placeholder"
                v-model="model.sellerFullName"
                icon="account"
                :validation-message="schema.groups[ms].fields[0].message"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[ms].fields[1].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[ms].fields[1].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-datepicker
                v-model="sellerBirthYear"
                :maxDate="new Date()"
                icon="calendar-today"
                v-mask="'99.99.9999'"
                :locale="locale"
                placeholder="ДД.ММ.ГГГГ"
                editable
                :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                :firstDayOfWeek="1"
                :openOnFocus="true"
                trap-focus
                :validation-message="schema.groups[ms].fields[1].message"
                required
              >
              </b-datepicker>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[ms].fields[2].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[ms].fields[2].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                v-model="model.sellerBirthPlace"
                icon="city"
                :placeholder="schema.groups[ms].fields[2].placeholder"
                :validation-message="schema.groups[ms].fields[2].message"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[ms].fields[3].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[ms].fields[3].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-select
                :placeholder="schema.groups[ms].fields[3].placeholder"
                v-model="model.sellerNationality"
                :selected="null"
                expanded
                icon="passport"
                required
              >
                <option
                  v-for="(nat, index) in schema.groups[ms].fields[3].values"
                  :key="index"
                >
                  {{ nat.name }}
                </option>
              </b-select>
            </b-tooltip>
          </b-field>
        </section>

        <section v-if="ms == 1 && select_second_step == 'ЮЛ'">
          <p class="pos" v-text="schema.groups[2].legend"></p>
          <b-field :label="schema.groups[2].fields[0].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[2].fields[0].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-autocomplete
                v-model="model.sellerOrgLegalForm"
                :data="filteredDataArray"
                :openOnFocus="true"
                :placeholder="schema.groups[2].fields[0].placeholder"
                clearable
                @select="(option) => (selected = option)"
              >
                <template #empty>Нет совпадений</template>
              </b-autocomplete>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[2].fields[1].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[2].fields[1].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[2].fields[1].placeholder"
                v-model="model.sellerOrgName"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[2].fields[2].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[2].fields[2].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-autocomplete
                v-model="model.sellerOrgPossition"
                :openOnFocus="true"
                icon="account"
                :data="filteredDataArraySellerPos"
                :placeholder="schema.groups[2].fields[2].placeholder"
                clearable
                required
                @select="(option) => (selected = option)"
              >
                <template #empty>Нет совпадений</template>
              </b-autocomplete>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[2].fields[3].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[2].fields[3].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[2].fields[3].placeholder"
                v-model="model.sellerCeoFullName"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
        </section>

        <section v-if="ms == 2 && select_second_step == 'ФЛ'">
          <p class="pos" v-text="schema.groups[1].legend"></p>
          <b-field :label="schema.groups[1].fields[4].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[1].fields[4].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[1].fields[4].placeholder"
                v-model="model.sellerPassNumberFirst"
                :id="schema.groups[1].fields[4].id"
                :maxlength="schema.groups[1].fields[4].maxlength"
                :minlength="schema.groups[1].fields[4].minlength"
                :has-counter="false"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[1].fields[5].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[1].fields[5].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[1].fields[5].placeholder"
                v-model="model.sellerPassNumberSec"
                :maxlength="schema.groups[1].fields[5].maxlength"
                :minlength="schema.groups[1].fields[5].minlength"
                :has-counter="false"
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[1].fields[6].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[1].fields[6].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[1].fields[6].placeholder"
                v-model="model.sellerPassIssuedBy"
                icon="home"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[1].fields[7].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[1].fields[7].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-datepicker
                v-model="sellerPassIssuedOn"
                placeholder="ДД.ММ.ГГГГ"
                :maxDate="new Date()"
                v-mask="'99.99.9999'"
                editable
                :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                :firstDayOfWeek="1"
                :openOnFocus="true"
                icon="calendar-today"
                :locale="locale"
                trap-focus
                required
              >
              </b-datepicker>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[1].fields[8].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[1].fields[8].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[1].fields[8].placeholder"
                v-model="model.sellerUnitCode"
                v-mask="'999-999'"
                :maxlength="schema.groups[1].fields[8].maxlength"
                :minlength="schema.groups[1].fields[8].minlength"
                :has-counter="false"
                pattern="^([0-9]{3}[-]{1}[0-9]{3})?$"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[1].fields[9].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[1].fields[9].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[1].fields[9].placeholder"
                v-model="model.sellerRegAddress"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[1].fields[10].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[1].fields[10].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-select
                :placeholder="schema.groups[1].fields[10].placeholder"
                v-model="model.sellerRepresent"
                :selected="null"
                expanded
                icon="passport"
                required
              >
                <option
                  v-for="(nat, index) in schema.groups[1].fields[10].values"
                  :key="index"
                >
                  {{ nat.name }}
                </option>
              </b-select>
            </b-tooltip>
          </b-field>

          <section
            v-if="
              JSON.stringify(model.sellerRepresent).match(
                'Да, от имени Продавца действует представитель'
              )
            "
          >
            <b-field :label="schema.groups[1].fields[12].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[1].fields[12].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[1].fields[12].placeholder"
                  v-model="model.sellerRepresentDocNum"
                  type="text"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>
            <b-field :label="schema.groups[1].fields[13].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[1].fields[13].hint"
                position="is-top"
                size="is-large"
                multilined
              >
                <b-datepicker
                  v-model="sellerRepresentDocDate"
                  :maxDate="new Date()"
                  placeholder="ДД.ММ.ГГГГ"
                  v-mask="'99.99.9999'"
                  editable
                  :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                  :firstDayOfWeek="1"
                  :openOnFocus="true"
                  icon="calendar-today"
                  :locale="locale"
                  required
                  trap-focus
                >
                </b-datepicker>
              </b-tooltip>
            </b-field>
            <b-field :label="schema.groups[1].fields[21].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[1].fields[21].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[1].fields[21].placeholder"
                  v-model="model.sellerRepresentDocBy"
                  type="text"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>
            <b-field :label="schema.groups[1].fields[20].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[1].fields[20].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[1].fields[20].placeholder"
                  v-model="model.sellerRepresentFullName"
                  icon="account"
                  :validation-message="schema.groups[1].fields[20].message"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>
            <b-field :label="schema.groups[1].fields[14].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[1].fields[14].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[1].fields[14].placeholder"
                  v-model="model.sellerRepresentPassNumFirst"
                  :maxlength="schema.groups[1].fields[14].maxlength"
                  :minlength="schema.groups[1].fields[14].minlength"
                  :has-counter="false"
                  type="text"
                  :min="0"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>
            <b-field :label="schema.groups[1].fields[15].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[1].fields[15].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[1].fields[15].placeholder"
                  v-model="model.sellerRepresentDocPassNumSec"
                  :maxlength="schema.groups[1].fields[15].maxlength"
                  :minlength="schema.groups[1].fields[15].minlength"
                  :has-counter="false"
                  type="text"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>

            <b-field :label="schema.groups[1].fields[16].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[1].fields[16].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[1].fields[16].placeholder"
                  v-model="model.sellerRepresentPassIssuedBy"
                  type="text"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>

            <b-field :label="schema.groups[1].fields[17].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[1].fields[17].hint"
                position="is-top"
                size="is-large"
                multilined
              >
                <b-datepicker
                  v-model="sellerRepresentPassDate"
                  :maxDate="new Date()"
                  placeholder="ДД.ММ.ГГГГ"
                  v-mask="'99.99.9999'"
                  editable
                  :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                  :firstDayOfWeek="1"
                  :openOnFocus="true"
                  icon="calendar-today"
                  :locale="locale"
                  trap-focus
                  required
                >
                </b-datepicker>
              </b-tooltip>
            </b-field>

            <b-field :label="schema.groups[1].fields[18].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[1].fields[18].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[1].fields[18].placeholder"
                  v-model="model.sellerRepresentUnitCode"
                  pattern="^([0-9]{3}[-]{1}[0-9]{3})?$"
                  v-mask="'999-999'"
                  :maxlength="schema.groups[1].fields[18].maxlength"
                  :minlength="schema.groups[1].fields[18].minlength"
                  :has-counter="false"
                  type="text"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>

            <b-field :label="schema.groups[1].fields[19].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[1].fields[19].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[1].fields[19].placeholder"
                  v-model="model.sellerRepresentRegAddress"
                  type="text"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>
          </section>
        </section>

        <section v-if="ms == 2 && select_second_step == 'ЮЛ'">
          <p class="pos" v-text="schema.groups[2].legend"></p>
          <b-field :label="schema.groups[2].fields[4].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[2].fields[4].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-autocomplete
                v-model="model.sellerOrgDoc"
                icon="account"
                :data="filteredDataArraySellerDoc"
                :placeholder="schema.groups[2].fields[4].placeholder"
                :openOnFocus="true"
                clearable
                required
                @select="(option) => (selected = option)"
              >
                <template #empty>Нет совпадений</template>
              </b-autocomplete>
            </b-tooltip>
          </b-field>
          <b-field
            v-if="model.sellerOrgDoc.toLowerCase() == 'доверенности'"
            :label="schema.groups[2].fields[5].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[2].fields[5].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[2].fields[5].placeholder"
                v-model="model.sellerOrgDocNum"
                type="text"
                :min="0"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field
            v-if="model.sellerOrgDoc.toLowerCase() == 'доверенности'"
            :label="schema.groups[2].fields[6].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[2].fields[6].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-datepicker
                v-model="sellerOrgDocDate"
                :maxDate="new Date()"
                placeholder="ДД.ММ.ГГГГ"
                v-mask="'99.99.9999'"
                editable
                :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                :firstDayOfWeek="1"
                :openOnFocus="true"
                icon="calendar-today"
                :locale="locale"
                required
                trap-focus
              >
              </b-datepicker>
            </b-tooltip>
          </b-field>
          <b-field
            v-if="
              model.sellerOrgDoc.toLowerCase() == 'доверенности' &&
              model.sellerOrgDocDate
            "
            :label="schema.groups[2].fields[7].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[2].fields[7].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[2].fields[7].placeholder"
                v-model="model.sellerOrgDocPassNumFirst"
                :maxlength="schema.groups[2].fields[7].maxlength"
                :minlength="schema.groups[2].fields[7].minlength"
                :has-counter="false"
                type="text"
                :min="0"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field
            v-if="
              model.sellerOrgDoc.toLowerCase() == 'доверенности' &&
              model.sellerOrgDocPassNumFirst
            "
            :label="schema.groups[2].fields[8].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[2].fields[8].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[2].fields[8].placeholder"
                v-model="model.sellerOrgDocPassNumSec"
                :maxlength="schema.groups[2].fields[8].maxlength"
                :minlength="schema.groups[2].fields[8].minlength"
                :has-counter="false"
                type="text"
                :min="0"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field
            v-if="model.sellerOrgDoc.toLowerCase() == 'доверенности'"
            :label="schema.groups[2].fields[9].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[2].fields[9].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[2].fields[9].placeholder"
                v-model="model.sellerOrgPassIssuedBy"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field
            v-if="model.sellerOrgDoc.toLowerCase() == 'доверенности'"
            :label="schema.groups[2].fields[10].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[2].fields[10].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-datepicker
                v-model="sellerOrgDocPassDate"
                :maxDate="new Date()"
                placeholder="ДД.ММ.ГГГГ"
                v-mask="'99.99.9999'"
                editable
                :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                :firstDayOfWeek="1"
                :openOnFocus="true"
                icon="calendar-today"
                :locale="locale"
                trap-focus
                required
              >
              </b-datepicker>
            </b-tooltip>
          </b-field>

          <b-field
            v-if="model.sellerOrgDoc.toLowerCase() == 'доверенности'"
            :label="schema.groups[2].fields[11].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[2].fields[11].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[2].fields[11].placeholder"
                v-model="model.sellerOrgUnitCode"
                pattern="^([0-9]{3}[-]{1}[0-9]{3})?$"
                v-mask="'999-999'"
                :maxlength="schema.groups[2].fields[11].maxlength"
                :minlength="schema.groups[2].fields[11].minlength"
                :has-counter="false"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field
            v-if="model.sellerOrgDoc.toLowerCase() == 'доверенности'"
            :label="schema.groups[2].fields[12].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[2].fields[12].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[2].fields[12].placeholder"
                v-model="model.sellerOrgRegAddress"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <p class="pos" v-text="schema.groups[8].legend"></p>
          <b-field :label="schema.groups[8].fields[0].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[8].fields[0].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[8].fields[0].placeholder"
                v-model="model.sellerOrgRegAddressUR"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[8].fields[1].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[8].fields[1].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[8].fields[1].placeholder"
                v-model="model.sellerOrgOGRN"
                :type="schema.groups[8].fields[1].inputType"
                :maxlength="schema.groups[8].fields[1].maxlength"
                :minlength="schema.groups[8].fields[1].minlength"
                :has-counter="false"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[8].fields[2].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[8].fields[2].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[8].fields[2].placeholder"
                v-model="model.sellerOrgINN"
                :type="schema.groups[8].fields[2].inputType"
                :maxlength="schema.groups[8].fields[2].maxlength"
                :minlength="schema.groups[8].fields[2].minlength"
                :has-counter="false"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[8].fields[3].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[8].fields[3].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[8].fields[3].placeholder"
                v-model="model.sellerOrgKPP"
                :maxlength="schema.groups[8].fields[3].maxlength"
                :minlength="schema.groups[8].fields[3].minlength"
                :has-counter="false"
                :type="schema.groups[8].fields[3].inputType"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[8].fields[4].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[8].fields[4].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[8].fields[4].placeholder"
                v-model="model.sellerOrgRS"
                :type="schema.groups[8].fields[4].inputType"
                :maxlength="schema.groups[8].fields[4].maxlength"
                :minlength="schema.groups[8].fields[4].minlength"
                :has-counter="false"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[8].fields[5].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[8].fields[5].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[8].fields[5].placeholder"
                v-model="model.sellerOrgKS"
                :type="schema.groups[8].fields[5].inputType"
                :maxlength="schema.groups[8].fields[5].maxlength"
                :minlength="schema.groups[8].fields[5].minlength"
                :has-counter="false"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[8].fields[6].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[8].fields[6].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[8].fields[6].placeholder"
                v-model="model.sellerOrgBank"
                :type="schema.groups[8].fields[6].inputType"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[8].fields[7].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[8].fields[7].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[8].fields[7].placeholder"
                v-model="model.sellerOrgBankBik"
                :type="schema.groups[8].fields[7].inputType"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[8].fields[8].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[8].fields[8].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[8].fields[8].placeholder"
                v-model="model.sellerOrgTel"
                :type="schema.groups[8].fields[8].inputType"
                v-mask="'+9(999)999-99-99'"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[8].fields[9].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[8].fields[9].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[8].fields[9].placeholder"
                v-model="model.sellerOrgPostAddress"
                :type="schema.groups[8].fields[9].inputType"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
        </section>

        <section v-if="ms == 3 && select_third_step == 'ФЛ'">
          <p class="pos" v-text="schema.groups[3].legend"></p>
          <b-field :label="schema.groups[3].fields[0].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[3].fields[0].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[3].fields[0].placeholder"
                v-model="model.custFullName"
                icon="account"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[3].fields[1].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[3].fields[1].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-datepicker
                v-model="custBirthYear"
                :maxDate="new Date()"
                icon="calendar-today"
                placeholder="ДД.ММ.ГГГГ"
                v-mask="'99.99.9999'"
                editable
                :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                :firstDayOfWeek="1"
                :openOnFocus="true"
                :locale="locale"
                trap-focus
                required
              >
              </b-datepicker>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[3].fields[2].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[3].fields[2].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                v-model="model.custBirthPlace"
                icon="city"
                :placeholder="schema.groups[3].fields[2].placeholder"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[3].fields[3].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[3].fields[3].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-select
                :placeholder="schema.groups[3].fields[3].placeholder"
                v-model="model.custNationality"
                expanded
                icon="passport"
                required
              >
                <option
                  v-for="(nat, index) in schema.groups[3].fields[3].values"
                  :key="index"
                >
                  {{ nat.name }}
                </option>
              </b-select>
            </b-tooltip>
          </b-field>
        </section>

        <section v-if="ms == 4 && select_third_step == 'ФЛ'">
          <p class="pos" v-text="schema.groups[3].legend"></p>
          <b-field :label="schema.groups[3].fields[4].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[3].fields[4].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[3].fields[4].placeholder"
                v-model="model.custPassNumberFirst"
                :id="schema.groups[3].fields[4].id"
                :maxlength="schema.groups[3].fields[4].maxlength"
                :minlength="schema.groups[3].fields[4].minlength"
                :has-counter="false"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[3].fields[5].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[3].fields[5].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[3].fields[5].placeholder"
                v-model="model.custPassNumberSec"
                :maxlength="schema.groups[3].fields[5].maxlength"
                :minlength="schema.groups[3].fields[5].minlength"
                :has-counter="false"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[3].fields[6].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[3].fields[6].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[3].fields[6].placeholder"
                v-model="model.custPassIssuedBy"
                icon="home"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[3].fields[7].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[3].fields[7].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-datepicker
                v-model="custPassIssuedOn"
                :maxDate="new Date()"
                placeholder="ДД.ММ.ГГГГ"
                v-mask="'99.99.9999'"
                editable
                :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                :firstDayOfWeek="1"
                :openOnFocus="true"
                icon="calendar-today"
                :locale="locale"
                trap-focus
                required
              >
              </b-datepicker>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[3].fields[8].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[3].fields[8].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[3].fields[8].placeholder"
                v-model="model.custUnitCode"
                pattern="^([0-9]{3}[-]{1}[0-9]{3})?$"
                v-mask="'999-999'"
                :maxlength="schema.groups[3].fields[8].maxlength"
                :minlength="schema.groups[3].fields[8].minlength"
                :has-counter="false"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[3].fields[9].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[3].fields[9].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[3].fields[9].placeholder"
                v-model="model.custRegAddress"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[3].fields[10].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[3].fields[10].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-select
                :placeholder="schema.groups[3].fields[10].placeholder"
                v-model="model.custRepresent"
                :selected="null"
                expanded
                icon="passport"
                required
              >
                <option
                  v-for="(el, index) in schema.groups[3].fields[10].values"
                  :key="index"
                >
                  {{ el.name }}
                </option>
              </b-select>
            </b-tooltip>
          </b-field>

          <section
            v-if="
              JSON.stringify(model.custRepresent).match(
                'Да, от имени Покупателя действует представитель'
              )
            "
          >
            <b-field :label="schema.groups[3].fields[12].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[3].fields[12].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[3].fields[12].placeholder"
                  v-model="model.custRepresentDocNum"
                  type="text"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>
            <b-field :label="schema.groups[3].fields[13].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[3].fields[13].hint"
                position="is-top"
                size="is-large"
                multilined
              >
                <b-datepicker
                  v-model="custRepresentDocDate"
                  :maxDate="new Date()"
                  placeholder="ДД.ММ.ГГГГ"
                  v-mask="'99.99.9999'"
                  editable
                  :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                  :firstDayOfWeek="1"
                  :openOnFocus="true"
                  icon="calendar-today"
                  :locale="locale"
                  required
                  trap-focus
                >
                </b-datepicker>
              </b-tooltip>
            </b-field>
            <b-field :label="schema.groups[3].fields[21].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[3].fields[21].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[3].fields[21].placeholder"
                  v-model="model.custRepresentDocBy"
                  type="text"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>
            <b-field :label="schema.groups[3].fields[20].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[3].fields[20].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[3].fields[20].placeholder"
                  v-model="model.custRepresentFullName"
                  icon="account"
                  :validation-message="schema.groups[3].fields[20].message"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>
            <b-field :label="schema.groups[3].fields[14].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[3].fields[14].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[3].fields[14].placeholder"
                  v-model="model.custRepresentPassNumFirst"
                  :maxlength="schema.groups[3].fields[14].maxlength"
                  :minlength="schema.groups[3].fields[14].minlength"
                  :has-counter="false"
                  type="text"
                  :min="0"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>
            <b-field :label="schema.groups[3].fields[15].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[3].fields[15].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[3].fields[15].placeholder"
                  v-model="model.custRepresentDocPassNumSec"
                  :maxlength="schema.groups[3].fields[15].maxlength"
                  :minlength="schema.groups[3].fields[15].minlength"
                  :has-counter="false"
                  type="text"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>

            <b-field :label="schema.groups[3].fields[16].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[3].fields[16].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[3].fields[16].placeholder"
                  v-model="model.custRepresentPassIssuedBy"
                  type="text"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>

            <b-field :label="schema.groups[3].fields[17].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[3].fields[17].hint"
                position="is-top"
                size="is-large"
                multilined
              >
                <b-datepicker
                  v-model="custRepresentPassDate"
                  :maxDate="new Date()"
                  placeholder="ДД.ММ.ГГГГ"
                  v-mask="'99.99.9999'"
                  editable
                  :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                  :firstDayOfWeek="1"
                  :openOnFocus="true"
                  icon="calendar-today"
                  :locale="locale"
                  trap-focus
                  required
                >
                </b-datepicker>
              </b-tooltip>
            </b-field>

            <b-field :label="schema.groups[3].fields[18].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[3].fields[18].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[3].fields[18].placeholder"
                  v-model="model.custRepresentUnitCode"
                  pattern="^([0-9]{3}[-]{1}[0-9]{3})?$"
                  v-mask="'999-999'"
                  :maxlength="schema.groups[3].fields[18].maxlength"
                  :minlength="schema.groups[3].fields[18].minlength"
                  :has-counter="false"
                  type="text"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>

            <b-field :label="schema.groups[3].fields[19].label">
              <b-tooltip
                class="fixed"
                :label="schema.groups[3].fields[19].hint"
                position="is-bottom"
                size="is-large"
                multilined
              >
                <b-input
                  :placeholder="schema.groups[3].fields[19].placeholder"
                  v-model="model.custRepresentRegAddress"
                  type="text"
                  required
                ></b-input>
              </b-tooltip>
            </b-field>
          </section>
        </section>

        <section v-if="ms == 3 && select_third_step == 'ЮЛ'">
          <p class="pos" v-text="schema.groups[4].legend"></p>
          <b-field :label="schema.groups[4].fields[0].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[4].fields[0].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-autocomplete
                v-model="model.custOrgLegalForm"
                :data="filteredDataArrayCust"
                :placeholder="schema.groups[4].fields[0].placeholder"
                :openOnFocus="true"
                clearable
                required
                @select="(option) => (selected = option)"
              >
                <template #empty>Нет совпадений</template>
              </b-autocomplete>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[4].fields[1].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[4].fields[1].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[4].fields[1].placeholder"
                v-model="model.custOrgName"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[4].fields[2].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[4].fields[2].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-autocomplete
                v-model="model.custOrgPossition"
                icon="account"
                :openOnFocus="true"
                :data="filteredDataArrayCustPos"
                :placeholder="schema.groups[4].fields[2].placeholder"
                clearable
                required
                @select="(option) => (selected = option)"
              >
                <template #empty>Нет совпадений</template>
              </b-autocomplete>
            </b-tooltip>
          </b-field>
          <b-field :label="schema.groups[4].fields[3].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[4].fields[3].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[4].fields[3].placeholder"
                v-model="model.custCeoFullName"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
        </section>

        <section v-if="ms == 4 && select_third_step == 'ЮЛ'">
          <p class="pos" v-text="schema.groups[4].legend"></p>
          <b-field :label="schema.groups[4].fields[4].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[4].fields[4].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-autocomplete
                v-model="model.custOrgDoc"
                icon="account"
                :data="filteredDataArrayCustDoc"
                :placeholder="schema.groups[4].fields[4].placeholder"
                :openOnFocus="true"
                clearable
                required
                @select="(option) => (selected = option)"
              >
                <template #empty>Нет совпадений</template>
              </b-autocomplete>
            </b-tooltip>
          </b-field>
          <b-field
            v-if="model.custOrgDoc.toLowerCase() == 'доверенности'"
            :label="schema.groups[4].fields[5].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[4].fields[5].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[4].fields[5].placeholder"
                v-model="model.custOrgDocNum"
                type="text"
                :min="0"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field
            v-if="model.custOrgDoc.toLowerCase() == 'доверенности'"
            :label="schema.groups[4].fields[6].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[4].fields[6].hint"
              position="is-top"
              size="is-large"
              multilined
            >
              <b-datepicker
                v-model="custOrgDocDate"
                :maxDate="new Date()"
                placeholder="ДД.ММ.ГГГГ"
                v-mask="'99.99.9999'"
                editable
                :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                :firstDayOfWeek="1"
                :openOnFocus="true"
                icon="calendar-today"
                :locale="locale"
                trap-focus
                required
              >
              </b-datepicker>
            </b-tooltip>
          </b-field>
          <b-field
            v-if="
              model.custOrgDoc.toLowerCase() == 'доверенности' &&
              model.custOrgDocDate
            "
            :label="schema.groups[4].fields[7].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[4].fields[7].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[4].fields[7].placeholder"
                v-model="model.custOrgDocPassNumFirst"
                :maxlength="schema.groups[4].fields[7].maxlength"
                :minlength="schema.groups[4].fields[7].minlength"
                :has-counter="false"
                type="text"
                :min="0"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
          <b-field
            v-if="
              model.custOrgDoc.toLowerCase() == 'доверенности' &&
              model.custOrgDocPassNumFirst
            "
            :label="schema.groups[4].fields[8].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[4].fields[8].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[4].fields[8].placeholder"
                v-model="model.custOrgDocPassNumSec"
                :maxlength="schema.groups[4].fields[8].maxlength"
                :minlength="schema.groups[4].fields[8].minlength"
                :has-counter="false"
                type="text"
                :min="0"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field
            v-if="
              model.custOrgDoc.toLowerCase() == 'доверенности' &&
              model.custOrgDocPassNumSec
            "
            :label="schema.groups[4].fields[9].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[4].fields[9].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[4].fields[9].placeholder"
                v-model="model.custOrgPassIssuedBy"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field
            v-if="
              model.custOrgDoc.toLowerCase() == 'доверенности' &&
              model.custOrgPassIssuedBy
            "
            :label="schema.groups[4].fields[10].label"
          >
            <b-datepicker
              v-model="custOrgDocPassDate"
              :maxDate="new Date()"
              placeholder="ДД.ММ.ГГГГ"
              v-mask="'99.99.9999'"
              editable
              :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
              :firstDayOfWeek="1"
              :openOnFocus="true"
              icon="calendar-today"
              :locale="locale"
              trap-focus
              required
            >
            </b-datepicker>
          </b-field>

          <b-field
            v-if="
              model.custOrgDoc.toLowerCase() == 'доверенности' &&
              model.custOrgDocPassDate
            "
            :label="schema.groups[4].fields[11].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[4].fields[11].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[4].fields[11].placeholder"
                v-model="model.custOrgUnitCode"
                v-mask="'999-999'"
                pattern="^([0-9]{3}[-]{1}[0-9]{3})?$"
                :maxlength="schema.groups[4].fields[11].maxlength"
                :minlength="schema.groups[4].fields[11].minlength"
                :has-counter="false"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field
            v-if="
              model.custOrgDoc.toLowerCase() == 'доверенности' &&
              model.custOrgUnitCode
            "
            :label="schema.groups[4].fields[12].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[4].fields[12].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[4].fields[12].placeholder"
                v-model="model.custOrgRegAddress"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[9].fields[0].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[9].fields[0].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[9].fields[0].placeholder"
                v-model="model.custOrgRegAddressUR"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[9].fields[1].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[9].fields[1].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[9].fields[1].placeholder"
                v-model="model.custOrgOGRN"
                :type="schema.groups[9].fields[1].inputType"
                :maxlength="schema.groups[9].fields[1].maxlength"
                :minlength="schema.groups[9].fields[1].minlength"
                :has-counter="false"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[9].fields[2].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[9].fields[2].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[9].fields[2].placeholder"
                v-model="model.custOrgINN"
                :maxlength="schema.groups[9].fields[2].maxlength"
                :minlength="schema.groups[9].fields[2].minlength"
                :has-counter="false"
                :type="schema.groups[9].fields[2].inputType"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[9].fields[3].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[9].fields[3].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[9].fields[3].placeholder"
                v-model="model.custOrgKPP"
                :type="schema.groups[9].fields[3].inputType"
                :maxlength="schema.groups[9].fields[3].maxlength"
                :minlength="schema.groups[9].fields[3].minlength"
                :has-counter="false"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[9].fields[4].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[9].fields[4].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[9].fields[4].placeholder"
                v-model="model.custOrgRS"
                :type="schema.groups[9].fields[4].inputType"
                :maxlength="schema.groups[9].fields[4].maxlength"
                :minlength="schema.groups[9].fields[4].minlength"
                :has-counter="false"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[9].fields[5].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[9].fields[5].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[9].fields[5].placeholder"
                v-model="model.custOrgKS"
                :type="schema.groups[9].fields[5].inputType"
                :maxlength="schema.groups[9].fields[5].maxlength"
                :minlength="schema.groups[9].fields[5].minlength"
                :has-counter="false"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[9].fields[6].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[9].fields[6].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[9].fields[6].placeholder"
                v-model="model.custOrgBank"
                :type="schema.groups[9].fields[6].inputType"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[9].fields[7].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[9].fields[7].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[9].fields[7].placeholder"
                v-model="model.custOrgBankBik"
                :type="schema.groups[9].fields[7].inputType"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[9].fields[8].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[9].fields[8].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[9].fields[8].placeholder"
                v-model="model.custOrgTel"
                :type="schema.groups[9].fields[8].inputType"
                v-mask="'+9(999)999-99-99'"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[9].fields[9].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[9].fields[9].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[9].fields[9].placeholder"
                v-model="model.custOrgPostAddress"
                :type="schema.groups[9].fields[9].inputType"
                required
              ></b-input>
            </b-tooltip>
          </b-field>
        </section>

        <section v-if="ms == 5">
          <p class="pos" v-text="schema.groups[5].legend"></p>
          <b-field :label="schema.groups[5].fields[0].label">
            <b-select
              v-model="model.propertyName"
              :placeholder="schema.groups[5].fields[0].placeholder"
              expanded
              icon="home"
              required
            >
              <option
                v-for="(property, index) in schema.groups[5].fields[0].values"
                :key="index"
                required
              >
                {{ property.name }}
              </option>
            </b-select>
          </b-field>

          <b-field :label="schema.groups[5].fields[1].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[5].fields[1].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[5].fields[1].placeholder"
                v-model="model.propertyFloorArea"
                type="number"
                :min="0"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field
            v-if="model.propertyName == 'Земельный участок'"
            :label="schema.groups[5].fields[10].label"
          >
            <b-select
              v-model="model.propertyLandCat"
              :placeholder="schema.groups[5].fields[10].placeholder"
              expanded
              icon="home"
            >
              <option
                v-for="(catproperty, index) in schema.groups[5].fields[10]
                  .values"
                :key="index"
                required
              >
                {{ catproperty.name }}
              </option>
            </b-select>
          </b-field>

          <b-field
            v-if="model.propertyName == 'Земельный участок'"
            :label="schema.groups[5].fields[11].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[5].fields[11].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[5].fields[11].placeholder"
                v-model="model.propertyLandUsed"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field
            v-if="model.propertyName !== 'Земельный участок'"
            :label="schema.groups[5].fields[2].label"
          >
            <b-tooltip
              class="fixed"
              :label="schema.groups[5].fields[2].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[5].fields[2].placeholder"
                v-model="model.propertyNumRoom"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field
            v-if="model.propertyName == 'Жилой дом'"
            label="Количество этажей"
          >
            <b-input
              :placeholder="schema.groups[5].fields[3].placeholder"
              v-model="model.propertyLevel"
              type="text"
              required
            ></b-input>
          </b-field>

          <b-field
            v-if="model.propertyName == 'Квартира'"
            :label="schema.groups[5].fields[3].label"
          >
            <b-input
              :placeholder="schema.groups[5].fields[3].placeholder"
              v-model="model.propertyLevel"
              type="text"
              :min="0"
              required
            ></b-input>
          </b-field>

          <b-field :label="schema.groups[5].fields[4].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[5].fields[4].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[5].fields[4].placeholder"
                v-model="model.propertyAddress"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[5].fields[5].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[5].fields[5].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[5].fields[5].placeholder"
                v-model="model.propertyUniqueIdentifier"
                :maxlength="24"
                :has-counter="false"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[5].fields[6].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[5].fields[6].hint"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[5].fields[6].placeholder"
                v-model="model.propertyDoc"
                type="text"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <b-field :label="schema.groups[5].fields[8].label">
            <b-datepicker
              v-model="regDocDate"
              :maxDate="new Date()"
              icon="calendar-today"
              placeholder="ДД.ММ.ГГГГ"
              v-mask="'99.99.9999'"
              editable
              :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
              :firstDayOfWeek="1"
              :openOnFocus="true"
              :locale="locale"
              required
            >
            </b-datepicker>
          </b-field>

          <b-field :label="schema.groups[5].fields[7].label">
            <b-input
              :placeholder="schema.groups[5].fields[7].placeholder"
              v-model="model.regDocNumber"
              type="text"
              required
            ></b-input>
          </b-field>
        </section>

        <section v-if="ms == 6">
          <p class="pos" v-text="schema.groups[6].legend"></p>
          <b-field :label="schema.groups[5].fields[12].label">
            <b-tooltip
              class="fixed"
              :label="schema.groups[5].fields[12].label"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <b-input
                :placeholder="schema.groups[5].fields[12].placeholder"
                v-model="model.cost"
                type="text"
                :maxlength="12"
                :has-counter="false"
                required
              ></b-input>
            </b-tooltip>
          </b-field>

          <label class="lab">{{ schema.groups[5].fields[13].label }}</label>
          <multiselect
            v-model="model.payMethod"
            :options="schema.groups[5].fields[13].values"
            :multiple="true"
            :maxHeight="Number(200)"
            :tag-placeholder="schema.groups[5].fields[13].placeholder"
            :placeholder="schema.groups[5].fields[13].placeholder"
            label="name"
            track-by="name"
            required
          >
          </multiselect>

          <section>
            <section
              v-if="
                JSON.stringify(model.payMethod).match('Материнский капитал')
              "
            >
              <b-field class="lab2" :label="schema.groups[5].fields[14].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[5].fields[14].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[5].fields[14].placeholder"
                    v-model="model.paySumMatCap"
                    type="number"
                    :min="0"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[5].fields[15].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[5].fields[15].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[5].fields[15].placeholder"
                    v-model="model.matcap"
                    type="text"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[5].fields[16].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[5].fields[16].hint"
                  position="is-top"
                  size="is-large"
                  multilined
                >
                  <b-datepicker
                    v-model="matcapDesDate"
                    icon="calendar-today"
                    placeholder="ДД.ММ.ГГГГ"
                    v-mask="'99.99.9999'"
                    editable
                    :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                    :firstDayOfWeek="1"
                    :openOnFocus="true"
                    :locale="locale"
                    required
                  >
                  </b-datepicker>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[5].fields[17].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[5].fields[17].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[5].fields[17].placeholder"
                    v-model="model.matcapDesNum"
                    type="number"
                    :min="0"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[5].fields[18].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[5].fields[18].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[5].fields[18].placeholder"
                    v-model="model.matcapSer"
                    type="number"
                    :min="0"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[5].fields[19].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[5].fields[19].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[5].fields[19].placeholder"
                    v-model="model.matcapNum"
                    type="number"
                    :min="0"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[5].fields[20].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[5].fields[20].hint"
                  position="is-top"
                  size="is-large"
                  multilined
                >
                  <b-datepicker
                    v-model="matcapDate"
                    :maxDate="new Date()"
                    icon="calendar-today"
                    placeholder="ДД.ММ.ГГГГ"
                    v-mask="'99.99.9999'"
                    editable
                    :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                    :firstDayOfWeek="1"
                    :openOnFocus="true"
                    :locale="locale"
                  >
                  </b-datepicker>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[5].fields[21].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[5].fields[21].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[5].fields[21].placeholder"
                    v-model="model.matcapOwner"
                    type="text"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>
            </section>

            <section v-if="JSON.stringify(model.payMethod).match('Рассрочка')">
              <b-field class="lab2" :label="schema.groups[6].fields[1].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[6].fields[1].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[6].fields[1].placeholder"
                    v-model="model.paySumRS"
                    type="number"
                    :min="0"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[6].fields[0].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[6].fields[0].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[6].fields[0].placeholder"
                    v-model="model.quantityPayments"
                    type="number"
                    :min="0"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <div class="lab">
                <b-field
                  v-for="one in Number(model.quantityPayments)"
                  :key="one"
                  :label="'Дата платежа: №' + one"
                >
                  <b-datepicker
                    v-model="model.rsPaymentDate[one]"
                    icon="calendar-today"
                    placeholder="ДД.ММ.ГГГГ"
                    v-mask="'99.99.9999'"
                    editable
                    :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                    :firstDayOfWeek="1"
                    :openOnFocus="true"
                    :locale="locale"
                    :focusable="true"
                    range
                  >
                  </b-datepicker>

                  <b-tooltip
                    label="Введите сумму платежа за указанный период"
                    position="is-bottom"
                    size="is-small"
                    multilined
                  >
                    <b-input
                      placeholder="Введите сумму платежа"
                      v-model="model.rsPayment[one]"
                      type="number"
                      :min="0"
                      required
                    ></b-input>
                  </b-tooltip>
                </b-field>
              </div>

              <b-field :label="schema.groups[6].fields[2].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[6].fields[2].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-select
                    v-model="model.zlgPay"
                    :placeholder="schema.groups[6].fields[2].placeholder"
                    expanded
                    icon="home"
                  >
                    <option
                      v-for="(property, index) in schema.groups[6].fields[2]
                        .values"
                      :key="index"
                      required
                    >
                      {{ property.name }}
                    </option>
                  </b-select>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[6].fields[3].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[6].fields[3].hint"
                  position="is-top"
                  size="is-large"
                  multilined
                >
                  <b-datepicker
                    v-model="zlgPayTermDate"
                    icon="calendar-today"
                    placeholder="ДД.ММ.ГГГГ"
                    v-mask="'99.99.9999'"
                    editable
                    :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                    :firstDayOfWeek="1"
                    :openOnFocus="true"
                    :locale="locale"
                  >
                  </b-datepicker>
                </b-tooltip>
              </b-field>
            </section>

            <section
              v-if="JSON.stringify(model.payMethod).match('Ипотека банка')"
            >
              <b-field class="lab2" :label="schema.groups[7].fields[0].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[0].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[0].placeholder"
                    v-model="model.paySumIB"
                    type="number"
                    :min="0"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[1].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[1].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[1].placeholder"
                    v-model="model.crBankName"
                    type="text"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[2].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[2].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[2].placeholder"
                    v-model="model.crBankNumber"
                    type="text"
                    :maxlength="35"
                    :has-counter="false"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[3].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[3].hint"
                  position="is-top"
                  size="is-large"
                  multilined
                >
                  <b-datepicker
                    v-model="crBankDocDate"
                    icon="calendar-today"
                    placeholder="ДД.ММ.ГГГГ"
                    v-mask="'99.99.9999'"
                    editable
                    :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                    :firstDayOfWeek="1"
                    :openOnFocus="true"
                    :locale="locale"
                  >
                  </b-datepicker>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[4].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[4].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[4].placeholder"
                    v-model="model.crBankDocTown"
                    type="text"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[5].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[5].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[5].placeholder"
                    v-model="model.crBankDocQMonth"
                    type="number"
                    :min="0"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[6].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[6].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[6].placeholder"
                    v-model="model.crBankOgrn"
                    type="text"
                    :minlength="13"
                    :maxlength="13"
                    :has-counter="false"
                    validation-message=""
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[7].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[7].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[7].placeholder"
                    v-model="model.crBankInn"
                    type="text"
                    :minlength="10"
                    :maxlength="10"
                    :has-counter="false"
                    position="is-top"
                    validation-message="ИНН банка состоит из 10 цифр. Проверьте правильность реквизитов"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[8].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[8].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[8].placeholder"
                    v-model="model.crBankKpp"
                    type="text"
                    :minlength="10"
                    :maxlength="10"
                    :has-counter="false"
                    position="is-top"
                    :validation-message="schema.groups[7].fields[8].message"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[9].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[9].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[9].placeholder"
                    v-model="model.crBankRs"
                    type="number"
                    :min="0"
                    :has-counter="false"
                    position="is-top"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[10].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[10].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[10].placeholder"
                    v-model="model.crBankKs"
                    type="number"
                    :min="0"
                    :has-counter="false"
                    position="is-top"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[11].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[11].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[11].placeholder"
                    v-model="model.crBankBik"
                    type="number"
                    :min="0"
                    :has-counter="false"
                    position="is-top"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[12].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[12].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[12].placeholder"
                    v-model="model.crBankAddress"
                    :type="schema.groups[7].fields[12].inputType"
                    :has-counter="false"
                    position="is-top"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[13].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[13].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[13].placeholder"
                    v-model="model.crBankPostAddress"
                    :type="schema.groups[7].fields[13].inputType"
                    :has-counter="false"
                    position="is-top"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>
            </section>

            <section
              v-if="JSON.stringify(model.payMethod).match('Ипотека физ. лица')"
            >
              <b-field class="lab2" :label="schema.groups[7].fields[14].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[14].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[14].placeholder"
                    v-model="model.paySumFL"
                    :type="schema.groups[7].fields[14].inputType"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[15].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[15].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[15].placeholder"
                    v-model="model.quantityPaymentsFL"
                    type="number"
                    :min="0"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <div class="lab">
                <b-field
                  v-for="one in Number(model.quantityPaymentsFL)"
                  :key="one"
                  :label="'Дата платежа: №' + one"
                >
                  <b-datepicker
                    v-model="model.rsPaymentDateFL[one]"
                    icon="calendar-today"
                    placeholder="ДД.ММ.ГГГГ"
                    v-mask="'99.99.9999'"
                    editable
                    :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                    :firstDayOfWeek="1"
                    :openOnFocus="true"
                    :locale="locale"
                    :focusable="true"
                    range
                  >
                  </b-datepicker>

                  <b-tooltip
                    label="Введите сумму платежа за указанный период"
                    position="is-bottom"
                    size="is-small"
                    multilined
                  >
                    <b-input
                      placeholder="Введите сумму платежа"
                      v-model="model.rsPaymentFL[one]"
                      type="number"
                      :min="0"
                      required
                    ></b-input>
                  </b-tooltip>
                </b-field>
              </div>

              <b-field :label="schema.groups[6].fields[3].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[6].fields[3].hint"
                  position="is-top"
                  size="is-large"
                  multilined
                >
                  <b-datepicker
                    v-model="zlgPayTermDate"
                    icon="calendar-today"
                    placeholder="ДД.ММ.ГГГГ"
                    v-mask="'99.99.9999'"
                    editable
                    :monthNames="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]"
                    :firstDayOfWeek="1"
                    :openOnFocus="true"
                    :locale="locale"
                  >
                  </b-datepicker>
                </b-tooltip>
              </b-field>
            </section>

            <section v-if="JSON.stringify(model.payMethod).match('Аккредитив')">
              <b-field class="lab2" :label="schema.groups[7].fields[16].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[16].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[16].placeholder"
                    v-model="model.paySumA"
                    :type="schema.groups[7].fields[16].inputType"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[17].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[17].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[17].placeholder"
                    v-model="model.acrDays"
                    :type="schema.groups[7].fields[17].inputType"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[18].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[18].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[18].placeholder"
                    v-model="model.acrBankName"
                    :type="schema.groups[7].fields[18].inputType"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[19].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[19].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[19].placeholder"
                    v-model="model.acrBankTown"
                    :type="schema.groups[7].fields[19].inputType"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[20].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[20].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[20].placeholder"
                    v-model="model.acrBankSellerNumber"
                    :type="schema.groups[7].fields[20].inputType"
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[21].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[21].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[21].placeholder"
                    v-model="model.acrBankSellerName"
                    :type="schema.groups[7].fields[21].inputType"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>
            </section>

            <section
              v-if="JSON.stringify(model.payMethod).match('Наличный расчет')"
            >
              <b-field class="lab2" :label="schema.groups[7].fields[22].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[22].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[22].placeholder"
                    v-model="model.nal"
                    :type="schema.groups[7].fields[22].inputType"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>
            </section>

            <section
              v-if="JSON.stringify(model.payMethod).match('Безналичный расчет')"
            >
              <b-field class="lab2" :label="schema.groups[7].fields[23].label">
                <b-input
                  :placeholder="schema.groups[7].fields[23].placeholder"
                  v-model="model.bznal"
                  :type="schema.groups[7].fields[23].inputType"
                  required
                ></b-input>
              </b-field>

              <b-field :label="schema.groups[7].fields[24].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[24].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[24].placeholder"
                    v-model="model.bznalBankNum"
                    :type="schema.groups[7].fields[24].inputType"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>

              <b-field :label="schema.groups[7].fields[25].label">
                <b-tooltip
                  class="fixed"
                  :label="schema.groups[7].fields[25].hint"
                  position="is-bottom"
                  size="is-large"
                  multilined
                >
                  <b-input
                    :placeholder="schema.groups[7].fields[25].placeholder"
                    v-model="model.bznalBankName"
                    :type="schema.groups[7].fields[25].inputType"
                    required
                  ></b-input>
                </b-tooltip>
              </b-field>
            </section>
          </section>

          <!-- <b-field
              v-if="payMethodA"
              id="dop_payMethod"
              label="Необходим дополнительный способ оплаты"
            >
              <b-switch
                v-model="isSwitchedCustom"
                true-value="Да"
                false-value="Нет"
              >
                {{ isSwitchedCustom }}
              </b-switch>
            </b-field>

            <section v-if="isSwitchedCustom == 'Да'">
            <b-field :label="schema.groups[5].fields[13].label">
              <b-select
                :placeholder="schema.groups[5].fields[13].placeholder"
                v-model="payMethodB"
                expanded
                icon="money"
                required
              >
                <option
                  v-for="(element, index) in schema.groups[5].fields[13].values"
                  :key="index"
                >
                  {{ element.name }}
                </option>
              </b-select>
            </b-field>
            </section> -->
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
        <!--
          <savefile :model="model" />
          -->

        <!-- </form> -->
      </div>
      <div id="right_menu">
        <dkp
          :model="model"
          :select_second_step="select_second_step"
          :select_third_step="select_third_step"
          :city="city"
        />
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */ 
import dkp from "@/agreements/dogovor_kupli_prodazhi";
import Multiselect from "vue-multiselect";
import model_out from "@/model.json";
import schema_out from "@/schema.json";
import axios from "axios";
import AwesomeMask from "awesome-mask";

const rubles = require("rubles").rubles;

export default {
  components: {
    Multiselect,
    dkp,
  },
  directives: {
    mask: AwesomeMask,
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
      dis: false,
      lastStep: false,
      valid: null,
      counter: false,
      date: null,
      city: "",
      email: "",
      sellerBirthYear: null,
      sellerOrgDocDate: null,
      sellerOrgDocPassDate: null,
      sellerPassIssuedOn: null,
      custBirthYear: null,
      custPassIssuedOn: null,
      custOrgDocDate: null,
      regDocDate: null,
      matcapDesDate: null,
      matcapDate: null,
      crBankDocDate: null,
      custOrgDocPassDate: null,
      zlgPayTermDate: null,
      sellerRepresentDocDate: null,
      sellerRepresentPassDate: null,
      custRepresentDocDate: null,
      custRepresentPassDate: null,
      locale: "ru-t-en-cyrl-gb-h0-hybrid",
      ls: true,
      lr: false,
      dl: false,
      ms: 0,
      model: model_out,
      schema: schema_out,
      // payMethodA: "",
      // payMethodB: "",
      // payMethodC: "",
      // payMethodD: "",
    };
  },
  methods: {
    sendData() {
      axios
        .post(
          "/generate/dkp/docx",
          {
            model: this.model,
            select_first_step: this.select_first_step,
            select_second_step: this.select_second_step,
            select_third_step: this.select_third_step,
          },
          { responseType: "blob" }
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
    Next() {
      if (this.valid === 0) {
        this.ms += 1;
        this.$refs.box.$el.scrollIntoView({ behavior: "smooth" });
      }
      if (this.ms >= 6) {
        this.ls = false;
        this.dl = true;
      }
      if (this.ms >= 1) {
        this.lr = true;
      }
    },
    Back() {
      this.ms -= 1;
      if (this.ms === 0) {
        this.lr = false;
      }
      if (this.ms <= 6) {
        this.ls = true;
        this.$refs.box.$el.scrollIntoView({ behavior: "smooth" });
      }
      if (this.ms != 6) {
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
  computed: {
    filteredDataArray() {
      return this.schema.groups[2].fields[0].data.filter((option) => {
        return (
          option
            .toString()
            .toLowerCase()
            .indexOf(this.model.sellerOrgLegalForm.toLowerCase()) >= 0
        );
      });
    },
    filteredDataArrayCust() {
      return this.schema.groups[4].fields[0].data.filter((option) => {
        return (
          option
            .toString()
            .toLowerCase()
            .indexOf(this.model.custOrgLegalForm.toLowerCase()) >= 0
        );
      });
    },
    filteredDataArraySellerPos() {
      return this.schema.groups[2].fields[2].data.filter((option) => {
        return (
          option
            .toString()
            .toLowerCase()
            .indexOf(this.model.sellerOrgPossition.toLowerCase()) >= 0
        );
      });
    },
    filteredDataArrayCustPos() {
      return this.schema.groups[4].fields[2].data.filter((option) => {
        return (
          option
            .toString()
            .toLowerCase()
            .indexOf(this.model.custOrgPossition.toLowerCase()) >= 0
        );
      });
    },
    filteredDataArraySellerDoc() {
      return this.schema.groups[2].fields[4].data.filter((option) => {
        return (
          option
            .toString()
            .toLowerCase()
            .indexOf(this.model.sellerOrgDoc.toLowerCase()) >= 0
        );
      });
    },
    filteredDataArrayCustDoc() {
      return this.schema.groups[4].fields[4].data.filter((option) => {
        return (
          option
            .toString()
            .toLowerCase()
            .indexOf(this.model.custOrgDoc.toLowerCase()) >= 0
        );
      });
    }
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
    if (this.ms == 0) {
      if (this.city && this.date && this.model.email) {
        this.dis = false;
      } else {
        this.dis = true;
      }
    }
    if (this.ms == 1) {
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
    if (this.ms == 2) {
      if (this.select_second_step == "ФЛ") {
        if (
          this.model.sellerPassNumberFirst &&
          this.model.sellerPassNumberSec &&
          this.model.sellerPassIssuedBy &&
          this.model.sellerPassIssuedOn &&
          this.model.sellerPassIssuedBy &&
          this.model.sellerUnitCode &&
          this.model.sellerRegAddress
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
    if (this.ms == 3) {
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
    if (this.ms == 4) {
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
    if (this.ms == 5) {
      if (this.model.propertyName) {
        this.dis = false;
      } else {
        this.dis = true;
      }

      if (this.model.propertyName == "Квартира") {
        if (
          this.model.propertyNumRoom &&
          this.model.propertyLevel &&
          this.model.propertyFloorArea &&
          this.model.propertyAddress &&
          this.model.propertyUniqueIdentifier &&
          this.model.propertyDoc &&
          this.model.regDocDate &&
          this.model.regDocNumber
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }

      if (this.model.propertyName == "Земельный участок") {
        if (
          this.model.propertyLandCat &&
          this.model.propertyLandUsed &&
          this.model.propertyFloorArea &&
          this.model.propertyAddress &&
          this.model.propertyUniqueIdentifier &&
          this.model.propertyDoc &&
          this.model.regDocDate &&
          this.model.regDocNumber
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }
      if (this.model.propertyName == "Жилой дом") {
        if (
          this.model.propertyFloorArea &&
          this.model.propertyNumRoom &&
          this.model.propertyUniqueIdentifier &&
          this.model.propertyLevel &&
          this.model.propertyAddress &&
          this.model.propertyDoc &&
          this.model.regDocDate &&
          this.model.regDocNumber
        ) {
          this.dis = false;
        } else {
          this.dis = true;
        }
      }
    }
    if (this.ms == 6) {
      if (this.model.cost && this.model.payMethod) {
        this.lastStep = true;
      } else {
        this.lastStep = false;
      }
    }
    if (this.ms < 6) {
      this.lastStep = false;
    }
  },
  mounted() {
    if (localStorage.model) {
      this.model = JSON.parse(localStorage.model)
    }
  },
  watch: {
    model: {
      deep: true,
      handler(newValue) {
        localStorage.model = JSON.stringify(newValue)
        if ((newValue.sellerRepresent == 'Нет') || (newValue.custRepresent == 'Нет')) {
          let x = Object.keys(newValue).filter(key => (JSON.stringify(key).match('Represent') && key.length > 15));
            for (let n in x) {
              this.model[x[n]] = '';
            }
        }
      },
      city(newValue) {
        console.log(newValue)
      }
    },
    date(newDate) {
      this.model.date = newDate.toLocaleDateString();
    },
    city(newCity) {
      this.model.city = newCity;
    },
    sellerBirthYear(newSellerBirthYear) {
      this.model.sellerBirthYear = newSellerBirthYear.toLocaleDateString();
    },
    sellerOrgDocDate(newSellerOrgDocDate) {
      this.model.sellerOrgDocDate = newSellerOrgDocDate.toLocaleDateString();
    },
    sellerOrgDocPassDate(newSellerOrgDocPassDate) {
      this.model.sellerOrgDocPassDate = newSellerOrgDocPassDate.toLocaleDateString();
    },
    sellerPassIssuedOn(newSellerPassIssuedOn) {
      this.model.sellerPassIssuedOn = newSellerPassIssuedOn.toLocaleDateString();
    },
    custBirthYear(newCustBirthYear) {
      this.model.custBirthYear = newCustBirthYear.toLocaleDateString();
    },
    custPassIssuedOn(newCustPassIssuedOn) {
      this.model.custPassIssuedOn = newCustPassIssuedOn.toLocaleDateString();
    },
    custOrgDocDate(newCustOrgDocDate) {
      this.model.custOrgDocDate = newCustOrgDocDate.toLocaleDateString();
    },
    regDocDate(newRegDocDate) {
      this.model.regDocDate = newRegDocDate.toLocaleDateString();
    },
    matcapDesDate(newMatcapDesDate) {
      this.model.matcapDesDate = newMatcapDesDate.toLocaleDateString();
    },
    matcapDate(newMatcapDate) {
      this.model.matcapDate = newMatcapDate.toLocaleDateString();
    },
    crBankDocDate(newCrBankDocDate) {
      this.model.crBankDocDate = newCrBankDocDate.toLocaleDateString();
    },
    custOrgDocPassDate(newCustOrgDocPassDate) {
      this.model.custOrgDocPassDate = newCustOrgDocPassDate.toLocaleDateString();
    },
    zlgPayTermDate(newZlgPayTermDate) {
      this.model.zlgPayTermDate = newZlgPayTermDate.toLocaleDateString();
    },
    sellerRepresentDocDate(newsellerRepresentDocDate) {
      this.model.sellerRepresentDocDate = newsellerRepresentDocDate.toLocaleDateString();
    },
    sellerRepresentPassDate(newsellerRepresentPassDate) {
      this.model.sellerRepresentPassDate = newsellerRepresentPassDate.toLocaleDateString();
    },
    custRepresentDocDate(newcustRepresentDocDate) {
      this.model.custRepresentDocDate = newcustRepresentDocDate.toLocaleDateString();
    },
    custRepresentPassDate(newcustRepresentPassDate) {
      this.model.custRepresentPassDate = newcustRepresentPassDate.toLocaleDateString();
    },
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
    max-height: 85vh;
  }
  #right_menu {
    position: relative;
    border-radius: 10px;
    box-shadow: 0 0.5em 1em -0.125em rgb(10 10 10 / 10%),
      0 0 0 1px rgb(10 10 10 / 2%);
    min-width: 798px;
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
