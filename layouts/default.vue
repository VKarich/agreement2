<template>
  <div class="master">
    <div id="main">
    <Nav />
    <Nuxt />
    </div>
    <Footer />
  </div>
</template>

<style>
html {
  font-family:
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
}
.master {
  display: flex;
  height: 100vh;
  flex-direction: column;
  background-color: rgb(253, 253, 253);
}
#main {
  flex: 1 0 auto;
}
/* .master {
  min-height: 100vh;
  background-color: rgb(253, 253, 253);
} */
/* #main {
  min-height: 100vmax;
} */
</style>
