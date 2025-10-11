// https://docs.expo.dev/guides/using-eslint/
const {defineConfig} = require('eslint/config');
const expoConfig = require('eslint-config-expo/flat');

module.exports = defineConfig([
  expoConfig,
  {
    ignores : [ 'dist/*' ],
    rules : {
      // reintroduce after testing
      "no-unused-vars" : "warn",
      "no-console" : "warn",
      "no-undef" : "warn",
      "import/no-unresolved" : "warn"
    }
  },
]);
