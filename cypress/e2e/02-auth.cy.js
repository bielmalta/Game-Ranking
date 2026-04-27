describe('Autenticação: cadastro, login, logout', () => {
  it('cadastra um novo usuário e faz login automaticamente', () => {
    cy.createTestUser().then((user) => {
      cy.url().should('match', /\/$/);
      cy.contains('.nav-user', user.username).should('be.visible');
      cy.contains('ul.messages', 'Conta criada com sucesso').should('be.visible');
    });
  });

  it('mostra erro com credenciais inválidas no login', () => {
    cy.fixture('users').then((users) => {
      cy.visit('/accounts/login/');
      cy.get('#id_username').type(users.invalid.username);
      cy.get('#id_password').type(users.invalid.password);
      cy.get('form').submit();
      cy.url().should('include', '/accounts/login/');
      cy.contains(/usu[aá]rio ou senha incorretos/i).should('be.visible');
    });
  });

  it('faz login com credenciais válidas e mostra navbar autenticada', () => {
    cy.createTestUser().then((user) => {
      cy.visit('/accounts/logout/');
      cy.url().should('include', '/accounts/login/');
      cy.loginAs(user.username, user.password);
      cy.contains('.nav-user', user.username).should('be.visible');
      cy.contains('a', 'Sair').should('be.visible');
    });
  });

  it('faz logout e volta para a tela de login', () => {
    cy.createTestUser().then((user) => {
      cy.contains('a', 'Sair').click();
      cy.url().should('include', '/accounts/login/');
      cy.contains('ul.messages', 'Você saiu').should('be.visible');
      cy.contains('.nav-link', 'Entrar').should('be.visible');
      cy.contains('.nav-user', user.username).should('not.exist');
    });
  });

  it('respeita o parâmetro ?next= e volta para a página original após login', () => {
    cy.createTestUser().then((user) => {
      cy.visit('/accounts/logout/');
      cy.visit('/accounts/login/?next=/ranking/');
      cy.get('#id_username').type(user.username);
      cy.get('#id_password').type(user.password);
      cy.get('form').submit();
      cy.url().should('include', '/ranking/');
    });
  });

  it('rota protegida (perfil) redireciona para login quando deslogado', () => {
    cy.visit('/accounts/profile/', { failOnStatusCode: false });
    cy.url().should('include', '/accounts/login/');
    cy.url().should('include', 'next=');
  });
});
