describe('Smoke: páginas principais carregam', () => {
  it('home / mostra navbar e seções', () => {
    cy.visit('/');
    cy.contains('a.nav-brand', 'Game Ranking').should('be.visible');
    cy.contains('.nav-link', 'Início').should('be.visible');
    cy.contains('.nav-link', 'Buscar').should('be.visible');
    cy.contains('.nav-link', 'Top 20').should('be.visible');
    cy.contains('h1', 'Descubra').should('be.visible');
  });

  it('/buscar/ exibe a barra de busca', () => {
    cy.visit('/buscar/');
    cy.contains('h1', 'Buscar jogos').should('be.visible');
    cy.get('input[name="q"]').should('be.visible');
    cy.contains('button', 'Buscar').should('be.visible');
  });

  it('/ranking/ carrega a página de Top 20', () => {
    cy.visit('/ranking/');
    cy.contains(/top\s*20/i).should('exist');
  });

  it('navegação pela navbar leva às páginas certas', () => {
    cy.visit('/');
    cy.contains('.nav-link', 'Buscar').click();
    cy.url().should('include', '/buscar/');
    cy.contains('.nav-link', 'Top 20').click();
    cy.url().should('include', '/ranking/');
    cy.contains('.nav-link', 'Início').click();
    cy.url().should('match', /\/$/);
  });

  it('usuário não autenticado vê os botões de Entrar e Cadastrar', () => {
    cy.visit('/');
    cy.contains('.nav-link', 'Entrar').should('be.visible');
    cy.contains('a', 'Cadastrar').should('be.visible');
  });
});
