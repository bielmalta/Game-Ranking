describe('Lista de jogos jogados', () => {
  it('botão de jogado não aparece para usuário deslogado', () => {
    cy.visit('/');
    cy.get('.game-card, .top-card').first().click();
    cy.get('[data-testid="toggle-played"]').should('not.exist');
  });

  it('marcar e desmarcar um jogo como jogado reflete no perfil', () => {
    cy.createTestUser();
    cy.visit('/');
    cy.get('.game-card, .top-card').first().click();

    cy.url().then((gameUrl) => {
      cy.contains('h1', /.+/).invoke('text').then((titulo) => {
        const tituloLimpo = titulo.trim();

        cy.get('[data-testid="toggle-played"]')
          .should('contain', 'Marcar como jogado')
          .click();

        cy.url().should('eq', gameUrl);
        cy.get('[data-testid="toggle-played"]').should(
          'contain',
          'Remover dos jogos jogados',
        );

        cy.visit('/accounts/profile/');
        cy.get('[data-testid="played-section"]')
          .should('contain', 'Jogos jogados')
          .and('contain', tituloLimpo);

        cy.visit(gameUrl);
        cy.get('[data-testid="toggle-played"]').click();
        cy.get('[data-testid="toggle-played"]').should(
          'contain',
          'Marcar como jogado',
        );

        cy.visit('/accounts/profile/');
        cy.get('[data-testid="played-section"]').should(
          'contain',
          'Você ainda não marcou nenhum jogo como jogado.',
        );
      });
    });
  });
});
