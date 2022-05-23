const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: true,
  css: {
    loaderOptions: {
      sass: {
        additionalData: `
        @import '@/assets/styles/_global.scss';
        @import '@/assets/styles/_shared.scss';
        @import '@/assets/styles/_colors.scss';
        @import "@/../public/main.css";
        `,
      },
    },
  },
});
