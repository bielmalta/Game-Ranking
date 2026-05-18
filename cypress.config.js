const { defineConfig } = require('cypress');

module.exports = defineConfig({
  projectId: 'nujq57',
  e2e: {
    baseUrl: 'http://127.0.0.1:8000',
    viewportWidth: 1280,
    viewportHeight: 800,
    defaultCommandTimeout: 8000,
    retries: { runMode: 2, openMode: 0 },
    supportFile: 'cypress/support/e2e.js',
    specPattern: 'cypress/e2e/**/*.cy.js',
  },
});
