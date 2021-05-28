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
        <div class="sec_sec">
        <div class="prev" v-show="prevNav">
          <b-button class="pag_but_prev" v-text="'<'" @click="back()"></b-button>
        </div>
        <div class="main2">
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
              <b-field>
                <b-radio
                  v-for="n in donors"
                  :key="n.msg"
                  v-model="select_from"
                  :native-value="`${n.value}`"
                  @input="selection_2($event)"
                  type="is-info"
                >
                  {{ n.msg }}
                </b-radio>
              </b-field>
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
              <b-field>
                <b-radio
                  v-for="n in recipients"
                  :key="n.msg"
                  v-model="select_to"
                  :native-value="`${n.value}`"
                  @input="selection_3($event)"
                  type="is-info"
                >
                  {{ n.msg }}
                </b-radio>
              </b-field>
            </b-tooltip>
          </b-field>
        </div>
        <div class="next" v-show="nextNav">
          <b-button class="pag_but_next" v-text="'>'" @click="next()"></b-button>
        </div>
        </div>
        </b-step-item>

        <b-step-item
          step="3"
          :visible="showAgrmt"
          label="Заполнение договора"
          :clickable="isStepsClickableAgrmt"
        >
        <div class="sec_sec">
        <div class="prev" v-show="prevNav">
          <b-button class="pag_but_prev" v-text="'<'" @click="back()"></b-button>
        </div>
        <div class="main_gener">
          <div class="generform">
            <generform
              :show_first="show_first"
              :select_first_step="select_agreement"
              :select_second_step="select_from"
              :select_third_step="select_to"
            />
          </div>
        </div>
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
      radioGroup: "",
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

      prevNav: false,
      nextNav: false,

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
    back() {
      this.activeStep -= 1;
    },
    next() {
      this.activeStep += 1;
    },
    selection(event) {
      console.log(event.target.childNodes[0].wholeText.trim())
      this.select_agreement = event.target.childNodes[0].wholeText.trim();
      // this.select_agreement = event.srcElement.innerHTML;
      //   this.$router
      //     .push({ query: { agrmt: this.select_agreement } })
      //     .catch(() => {});
      this.activeStep += 1;
      this.hasNavigation = true;
      this.isStepsClickable = true;
      this.hasNavigation = false;
      this.prevNav = true;
    },
    selection_2(event) {
      this.activeSecond += 1;
    },
    selection_3(event) {
      this.show_first = false;
      this.onSelect = false;
      this.activeSecond += 1;
      if (this.activeSecond == 2) {
        this.activeStep = 2;
      }
      this.isStepsClickableAgrmt = true;
      this.nextNav = true;
    },
  },
};
</script>

<style scoped>
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
.side {
  background-color: chartreuse;
  color: #1990d4;
}
button:active,
button:focus {
  outline: none !important;
}
button::-moz-focus-inner {
  border: 0 !important;
}
@media only screen and (max-width: 370px) {
  .selection {
  display: flex;
  flex-direction: column;
  padding-top: 5vh;
  padding-left: 3vh;
  padding-right: 3vh;
  }
  #sec {
    display: block;
  }
  #left {
    position: flex;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    min-width: auto;
  }
  #right {
    position: flex;
    padding-top: 5vh;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    min-width: auto;
  }
}
@media only screen and (min-width: 370px) and (max-width: 767px) {
  .card {
    font-weight: 300;
  }
  .selection {
  display: flex;
  padding-top: 5vh;
  padding-left: 3vh;
  padding-right: 3vh;
  }
  #sec {
    display: flex;
    flex-direction: column-reverse;
  }
  #left {
    position: block;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    min-width: auto;
    padding-bottom: 20px;
  }
  #right {
    position: block;
    padding-top: 3vh;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    min-width: auto;
  }
  .main-text {
    font-size: 2em;
    font-weight: 600;
    text-align: center;
    padding-bottom: 3vh;
  }
  .sec-text {
    font-size: 1.2em;
    font-weight: 400;
    padding-top: 0.7em;
    padding-bottom: 0.7em;
    text-align: center;
  }
  .selec {
    padding-top: 3vh;
    font-size: 2em;
    font-weight: 600;
    padding-bottom: 0.4em;
    text-align: center;
  }
  .card-header-title {
    padding-left: 20px;
    font-size: 1.1em;
  }
}
@media only screen and (min-width: 767px) and (max-width: 3767px) {
  .card {
    font-weight: 300;
  }
  .selection {
    display: block;
    flex-direction: column;
    padding-top: 5vh;
    padding-left: 3vh;
    padding-right: 3vh;
  }
  #sec {
    display: flex;
  }
  #left {
    position: relative;
    min-width: 350px;
    max-width: 350px;
    padding-bottom: 20px;
    min-height: 60vh;
    max-height: auto;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    border-radius: 10px;
    box-shadow: 0 0.5em 1em -0.125em rgb(10 10 10 / 10%), 0 0 0 1px rgb(10 10 10 / 2%);
    border: 0 !important;
  }
  #right {
    position: relative;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    min-width: auto;
    padding-left: 15px;
    padding-right: 15px;
    border-radius: 10px;
    box-shadow: 0 0.5em 1em -0.125em rgb(10 10 10 / 10%), 0 0 0 1px rgb(10 10 10 / 2%);
    border: 0 !important;
    margin-left: 15px;
  }
  .main-text {
    padding-top: 15px;
    font-size: 2em;
    font-weight: 600;
    text-align: center;
    padding-bottom: 3vh;
  }
  .sec-text {
    font-size: 1.2em;
    font-weight: 400;
    padding-top: 0.7em;
    padding-bottom: 0.7em;
    text-align: center;
  }
  .selec {
    padding-top: 15px;
    font-size: 2em;
    font-weight: 600;
    padding-bottom: 0.4em;
    text-align: center;
  }
  .card-header-title {
    padding-left: 20px;
    font-size: 1.1em;
  }
}
/* @media all and (min-width: 767px) and (max-width: 3024px) {
  .selection {
  display: block;
  flex-direction: column;
  padding-top: 5vh;
  padding-left: 3vh;
  padding-right: 3vh;
  border: 2px solid rgb(40, 90, 228);
  }
  #sec {
    display: flex;
    border: 2px solid rgb(247, 206, 72);
  }
  #left {
    position: relative;
    border: 2px solid darkmagenta;
    min-width: 30vw;
    max-width: 30vw;
    float: left;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
  }
  #right {
    position: relative;
    min-width: auto;
    max-width: auto;
    border: 2px solid darkmagenta;
    padding-top: 5vh;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    min-width: auto;
  }
} */

/* .sec_sec {
  display: flex;
  min-height: 68vh;
  border: none;
}
.prev {
  position: block;
  float: left;
  width: 40px;
  box-shadow: 0 0.5em 1em -0.125em rgb(10 10 10 / 10%),
      0 0 0 1px rgb(10 10 10 / 2%);
}
.next {
  position: block;
  float: right;
  text-align: center;
  width: 40px;
  box-shadow: 0 0.5em 1em -0.125em rgb(10 10 10 / 10%),
      0 0 0 1px rgb(10 10 10 / 2%);
}
.pag_but_prev {
  height: 100%;
  border-radius: 10px 0px 0px 10px;
}
.pag_but_next {
  height: 100%;
  border-radius: 0 10px 10px 0;
}
.main2 {
  position: block;
  padding-top: 0px;
  border-radius: 10px;
  width: 100%;
  margin-left: 10px;
  margin-right: 10px;
  box-shadow: 0 1.5em 1.5em -0.125em rgb(10 10 10 / 10%),
      0 0 0 1px rgb(10 10 10 / 2%);
}
.main_gener {
  position: block;
  width: 100%;
  margin-left: 10px;
  margin-right: 10px;
}
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
.side {
  background-color: chartreuse;
  color: #1990d4;
}
button:active,
button:focus {
  outline: none !important;
}
button::-moz-focus-inner {
  border: 0 !important;
} */
</style>
