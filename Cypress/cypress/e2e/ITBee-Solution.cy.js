
describe('ITBee Test Case', () => {
  it('Test Case Basic', () => {
    cy.visit('https://raksul.github.io/recruit-qa-engineer-work-sample/')

    // Fill textbox Email
    cy.get('#form_item_email').type('dung.lq@itbeesolutions.vn')
    // Fill textbox Lastname
    cy.get('#form_item_lastName').type('Dung')
    // Fill textbox FirstName
    cy.get('#form_item_firstName').type('Le Quang')


 //Select item from Drop menu
    cy.get('.ant-select-selection-item').click()
  // cy.contains('.ant-select-item-option-content', 'Search engines').click()
  // cy.contains('.ant-select-item-option-content', 'Recommended by friend').click()
    cy.contains('.ant-select-item-option-content', 'Other').click()

  // Select Checkbox
  cy.get(':nth-child(1) > .ant-checkbox > .ant-checkbox-input').check({force:true})

  cy.get(':nth-child(2) > .ant-checkbox > .ant-checkbox-input').check({force:true})

  // Select Radio
  cy.get('[type="radio"]').check('5')

  // Fill textbox Explantation
  cy.get('#form_item_explanation').type('Nothing...')


  // Click Button Submit

  cy.contains('button', 'Submit').click()

  })
})