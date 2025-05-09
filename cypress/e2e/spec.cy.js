describe('Create and connect to an account', () => {
  it('Visits the Oc commerce site', () => {
    cy.visit('/home');

    const randomId = Math.floor(Math.random() * 100000);
    const username = `fakeuser${randomId}`;
    const email = `fake${randomId}@email.com`;
    const password = '1hstesh<23456789';

    cy.contains('SIGNUP').click();
    cy.url().should('include', '/user/signup');

    cy.get('[id^=fname]').type('fakeuser');
    cy.get('[id^=lname]').type('toto');
    cy.get('[id^=username]').type(username);
    cy.get('[id^=email]').type(email);
    cy.get('[id^=pass]').type(password);
    cy.get('[id^=re_pass]').type(password);
    cy.get('form').contains('Register').click();
    cy.url().should('include', '/user/login');

    cy.get('[id^=your_name]').type(username);
    cy.get('[id^=your_pass]').type(password);
    cy.get('form').contains('Log in').click();
    cy.url().should('include', '/home');
    cy.contains('FAVOURITE');
  });
});
