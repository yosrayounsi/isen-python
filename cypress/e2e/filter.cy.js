describe('Filter products by price', () => {
    it('Displays only products below a selected price', () => {
      cy.visit('/home')
      
      cy.get('input[name="max_price"]').type('30') 
      cy.get('form').contains('Filtrer').click()
  
      cy.get('.portfolio-item h6').each(($el) => {
        const priceText = $el.text().replace('$', '').trim()
        const price = parseFloat(priceText)
        expect(price).to.be.at.most(30)
      })
    })
  })
  