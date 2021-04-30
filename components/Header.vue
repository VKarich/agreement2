<template>
  <div class="selection">
    <section>
      <b-steps
        size="is-small"
        v-model="activeStep"
        :animated="isAnimated"
        :rounded="isRounded"
        :has-navigation="hasNavigation"
        :icon-prev="prevIcon"
        :icon-next="nextIcon"
        :label-position="labelPosition"
        :mobile-mode="mobileMode"
      >
        <b-step-item
          step="1"
          label="Выбор договора"
          :clickable="isStepsClickable"
        >
          <div id="sec">
            <div id="left">
              <p class="selec">Выберите договор</p>
              <b-collapse
                class="card"
                animation="slide"
                v-for="(agr, index) in agrmnstest"
                :key="index"
                :open="isOpen == index"
                @open="isOpen = index"
              >
                <template #trigger="props">
                  <div class="card-header" role="button">
                    <p class="card-header-title">
                      {{ agr.category }}
                    </p>
                    <a class="card-header-icon">
                      <b-icon :icon="props.open ? 'menu-down' : 'menu-up'">
                      </b-icon>
                    </a>
                  </div>
                </template>
                <div>
                  <button
                    v-for="(agrmt, index) in agrmns"
                    :key="index"
                    @click="selection($event)"
                  >
                    {{ agrmt.msg }}
                  </button>
                </div>
              </b-collapse>
            </div>
            <div id="right">
              <p class="main-text">
                Deelly - Твой личный бизнес партнер в юридических вопросах
              </p>

              <p class="sec-text">
                Чтобы создать документ, нужно просто выбрать необходимый вид
                договора, ответить на вопросы и заполнить поля для ввода
                информации
              </p>
              <p class="sec-text">
                В зависимости от Ваших ответов, документ настраивается
                индивидуально под Вашу ситуацию
              </p>
            </div>
          </div>
        </b-step-item>

        <b-step-item
          step="2"
          label="Участники договора"
          :clickable="isStepsClickable"
          :type="{ 'is-success': isProfileSuccess }"
        >
          <h1 class="title has-text-centered">Выберите участников договора</h1>
          <b-field
            class="select_field"
            label="В качестве кого Вы хотели бы заключить договор?"
          >
            <b-tooltip
              label="Физическое лицо - Вы действуете от своего имени. Юридическое лицо - Вы действуете от имени Организации"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <button class="sides" outlined v-for="(donor, index) in donors"
                  :key="index"
                  :value="donor.value"
                  @click="selection_2($event)"
                  >{{ donor.msg }}</button>

            </b-tooltip>
          </b-field>
          <b-field
            class="select_field"
            label="С кем Вы планируете заключить договор?"
          >
            <b-tooltip
              label="Физическое лицо - вторая сторона действует от своего имени. Юридическое лицо - вторая сторона действует от имени Организации"
              position="is-bottom"
              size="is-large"
              multilined
            >
              <button class="sides" v-for="(recipient, index) in recipients"
                  :key="index"
                  :value="recipient.value"
                  @click="selection_3($event)"
                  >{{ recipient.msg }}</button>
            </b-tooltip>
          </b-field>
        </b-step-item>

        <b-step-item
          step="3"
          :visible="showAgrmt"
          label="Заполнение договора"
          :clickable="isStepsClickableAgrmt"
        >
          <div class="generform">
            <generform
              :show_first="show_first"
              :select_first_step="select_agreement"
              :select_second_step="select_from"
              :select_third_step="select_to"
            />
          </div>
        </b-step-item>
      </b-steps>
    </section>
  </div>
</template>

<script>
/* eslint-disable */
import Generform from "./Generform";

export default {
  components: { Generform },
  name: "Header",
  data() {
    return {
      isOpen: 0,
      activeStep: 0,
      activeSecond: 0,
      show_navi: false,
      showAgrmt: true,
      isAnimated: false,
      isRounded: true,
      isStepsClickable: false,
      isStepsClickableAgrmt: false,

      hasNavigation: false,
      customNavigation: false,
      isProfileSuccess: false,

      prevIcon: "chevron-left",
      nextIcon: "chevron-right",
      labelPosition: "bottom",
      mobileMode: "compact",

      onSelect: true,
      activeTab: 0,
      isScrollable: false,
      maxHeight: 200,
      currentMenuAgr: { id: 1, msg: "Список доступных договоров" },
      currentMenuCo1: { id: 1, msg: "Выберите вариант" },
      currentMenuCo2: { id: 1, msg: "Выберите вариант" },
      isPublic: true,
      show_first: true,
      select_agreement: "",
      select_from: "",
      select_to: "",
      agrmns: [
        {
          id: 1,
          msg: "Договор купли-продажи недвижимого имущества",
        },
        {
          id: 1,
          msg: "Договор аренды",
        },
      ],
      agrmnstest: [
        {
          category: "Недвижимость",
        },
      ],
      donors: [
        {
          id: 1,
          msg: "Физическое лицо",
          value: "ФЛ",
        },
        {
          id: 2,
          msg: "Юридическое лицо",
          value: "ЮЛ",
        },
      ],
      recipients: [
        {
          id: 1,
          msg: "Физическое лицо",
          value: "ФЛ",
        },
        {
          id: 2,
          msg: "Юридическое лицо",
          value: "ЮЛ",
        },
      ],
    };
  },
  //   created() {
  //     if (
  //       this.$route.query.agrmt &&
  //       JSON.stringify(this.agrmns).match(this.$route.query.agrmt)
  //     ) {
  //       this.select_agreement = this.$route.query.agrmt;
  //       this.currentMenuAgr.msg = this.$route.query.agrmt;
  //     }
  //   },
  methods: {
    selection(event) {
      this.select_agreement = event.path[0].innerText;
      //   this.$router
      //     .push({ query: { agrmt: this.select_agreement } })
      //     .catch(() => {});
      this.activeStep += 1;
      this.hasNavigation = true;
      this.isStepsClickable = true;
      this.hasNavigation = false;
    },
    selection_2(event) {
      this.select_from = event.path[0].value;
      this.activeSecond += 1;
    },
    selection_3(event) {
      this.select_to = event.path[0].value;
      this.show_first = false;
      this.onSelect = false;
      this.activeSecond += 1;
      if (this.activeSecond == 2) {
        this.activeStep = 2;
      }
      this.isStepsClickableAgrmt = true;
      this.hasNavigation = true;
    },
  },
};
</script>

<style scoped>
@media screen and (max-width: 3280px) {
  #sec {
    display: flex;
  }
  #left {
    position: block;
    min-width: 350px;
    max-width: 350px;
    float: left;
    padding: 3px;
    margin: 10px;
    min-height: 65vh;
    border-radius: 20px;
    box-shadow: 0 0.5em 1em -0.125em rgb(10 10 10 / 10%),
      0 0 0 1px rgb(10 10 10 / 2%);
  }
  #right {
    position: block;
    min-width: 600px;
    padding: 3px;
    margin: 10px;
  }
}
@media only screen and (min-device-width: 320px) and (max-device-width: 1024px) {
  #sec {
    display: block;
  }
  #left {
    position: flex;
  }
  #right {
    position: flex;
  }
}
.selection {
  padding-top: 20px;
  text-align: center;
}
.select_field {
  text-align: center;
}
p {
  padding: 4px;
}
.media-left {
  margin-right: 0rem;
  margin-left: 0rem;
}
.dropdown-item,
.dropdown .dropdown-menu .has-link a {
  color: #4a4a4a;
  display: block;
  font-size: 0.875rem;
  line-height: 1.5;
  width: auto;
  padding: 0.375rem 3rem;
  position: relative;
}
.section_btn {
  padding-bottom: 1%;
}
.main-text {
  font-size: 2em;
  font-weight: 600;
}
.sec-text {
  font-size: 1em;
  font-weight: 400;
  padding-top: 0.4em;
  padding-bottom: 0.4em;
}
.selec {
  font-size: 2em;
  font-weight: 600;
  padding-bottom: 0.4em;
}
button {
  background-color: white;
  border: 1px solid transparent;
  border-color: #dbdbdb;
  border-width: 1px;
  color: #363636;
  cursor: pointer;
  justify-content: center;
  padding-bottom: calc(0.5em - 1px);
  padding-left: 1em;
  padding-right: 1em;
  padding-top: calc(0.5em - 1px);
  font-size: 1rem;
  text-align: center;
  width: 100%;
  font-style: inherit;
  font-weight: inherit;
}
button:hover {
  color: #1990d4;
}
.sides {
  margin: 2px;
  height: 2.5em;
}
</style>