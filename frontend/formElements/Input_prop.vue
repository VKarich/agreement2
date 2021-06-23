<template>
  <section>
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
        position="is-bottom"
        size="is-large"
        :label="hint"
        multilined
        :active="active"
        type="is-dark"
        always
      >
        <b-input
          :icon="icon"
          :type="type"
          :id="id"
          v-model="model[fieldmodel][def_key]"
          :placeholder="placeholder"
          :maxlength="maxlength"
          :pattern="pattern"
          :minlength="minlength"
          :validation-message="message"
          :has-counter="false"
          :required="required"
          @change.native="send(fieldmodel, $event)"
        ></b-input>
      </b-tooltip>
    </b-field>
  </section>
</template>

<script>
/* eslint-disable */
import axios from "axios";

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
    "minlength",
    "message",
    "fieldmodel",
    "model",
    "pattern",
    "quantityOfProperty",
    "def_key"
  ],
  data() {
    return {
      active: false,
    };
  },
  methods: {
    send(fieldmodel, event) {
      if (fieldmodel == "propertyUniqueIdentifier") {
        axios.post("/data/kadastr/",
        {
          object_id: event.target.value
        }
        // axios.post("/data/kadastr/",
        //   event.target.value
        ).then((response) => {
          if (response.status == 200) {
            this.model.propertyFloorArea[this.def_key] = response.property_floor_area;
            this.model.propertyLevel[this.def_key] = response.property_level;
            this.model.propertyAddress[this.def_key] = response.property_address;
            if (response.property_land_cat) {
              this.model.propertyLandCat[this.def_key] = response.property_land_cat
            }
          }
        })
        .catch((error) => {
          console.log(error);
        });
      }
    },
    hintExist() {
      if (this.hint) {
        this.active = !this.active;
      } else {
        this.active = false;
      }
    },
  }
};
</script>

<style>
</style>