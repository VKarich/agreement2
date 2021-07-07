import Vue from 'vue'
import { wrapFunctional } from './utils'

const components = {
  Footer: () => import('../../components/Footer.vue' /* webpackChunkName: "components/footer" */).then(c => wrapFunctional(c.default || c)),
  Generform: () => import('../../components/Generform.vue' /* webpackChunkName: "components/generform" */).then(c => wrapFunctional(c.default || c)),
  Header: () => import('../../components/Header.vue' /* webpackChunkName: "components/header" */).then(c => wrapFunctional(c.default || c)),
  Logo: () => import('../../components/Logo.vue' /* webpackChunkName: "components/logo" */).then(c => wrapFunctional(c.default || c)),
  Nav: () => import('../../components/Nav.vue' /* webpackChunkName: "components/nav" */).then(c => wrapFunctional(c.default || c)),
  Requisites: () => import('../../components/Requisites.vue' /* webpackChunkName: "components/requisites" */).then(c => wrapFunctional(c.default || c)),
  Sides: () => import('../../components/Sides.vue' /* webpackChunkName: "components/sides" */).then(c => wrapFunctional(c.default || c)),
  FormBuilder: () => import('../../components/formBuilder.vue' /* webpackChunkName: "components/form-builder" */).then(c => wrapFunctional(c.default || c))
}

for (const name in components) {
  Vue.component(name, components[name])
  Vue.component('Lazy' + name, components[name])
}
