<template>
  <section>
    <footer class="footer">
      <div class="content has-text-left">
        ©Deely 2021
      </div>
      <div class="content has-text-right" id="fa">
          <a href="mailto:hello@deelly.app">hello@deelly.app</a>
          <a href="http://t.me/deellyapp" target="_blank">@deellyapp</a>
      </div>
    </footer>
  </section>
</template>

<style scoped>
.content {
  display: inline;
}
.has-text-right {
  float: right;
}
.has-text-left {
  font-weight:bold;
}
a {
  color: rgb(252, 252, 252);
}
a:hover {
  color: rgb(241, 170, 15);
}
</style>
<style lang='scss'>
@import "~bulma/sass/utilities/_all";
// Set your colors
$primary: #1990d4;
$primary-light: findLightColor($primary);
$primary-dark: findDarkColor($primary);
$primary-invert: findColorInvert($primary);
$twitter: #4099FF;
$twitter-invert: findColorInvert($twitter);
$dark: #141414;
$footer-background-color: $dark;
$footer-color: $white;
$footer-padding: 1.5rem;

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

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>