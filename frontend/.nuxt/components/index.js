import { wrapFunctional } from './utils'

export { default as Footer } from '../../components/Footer.vue'
export { default as Generform } from '../../components/Generform.vue'
export { default as Header } from '../../components/Header.vue'
export { default as Logo } from '../../components/Logo.vue'
export { default as Nav } from '../../components/Nav.vue'
export { default as FormBuilder } from '../../components/formBuilder.vue'

export const LazyFooter = import('../../components/Footer.vue' /* webpackChunkName: "components/footer" */).then(c => wrapFunctional(c.default || c))
export const LazyGenerform = import('../../components/Generform.vue' /* webpackChunkName: "components/generform" */).then(c => wrapFunctional(c.default || c))
export const LazyHeader = import('../../components/Header.vue' /* webpackChunkName: "components/header" */).then(c => wrapFunctional(c.default || c))
export const LazyLogo = import('../../components/Logo.vue' /* webpackChunkName: "components/logo" */).then(c => wrapFunctional(c.default || c))
export const LazyNav = import('../../components/Nav.vue' /* webpackChunkName: "components/nav" */).then(c => wrapFunctional(c.default || c))
export const LazyFormBuilder = import('../../components/formBuilder.vue' /* webpackChunkName: "components/form-builder" */).then(c => wrapFunctional(c.default || c))
