// code demo stripe testcase


import { test, expect } from '@playwright/test';



// viết toàn bộ demo các testcase tại đây

// iframe  - code test case contain iframe
// tim trang web chua iframe de test
// https://stripe-payments-demo.appspot.com/

//TC1
test('Input Iframe - 1', async ({ page }) => {

  
  // Navigate to a specific URL.
  await page.goto('https://stripe-payments-demo.appspot.com/');


 // Input name textbox
 await page.fill('input[name="name"]','Pikachu');

// Input email texbox
 await page.fill('input[name="email"]','Pikachu@gmail.com');

 // Input address texbox
 await page.fill('input[name="address"]','Vietnam');

  // Input city texbox
  await page.fill('input[name="city"]','Hanoi');


   // Input state texbox
 await page.fill('input[name="state"]','Hanoi');


  // Input postal_code texbox
  await page.fill('input[name="postal_code"]','10000');


   // Select  country
 await page.click('select[name="country"]');
   // Click JP
 await page.click('option[value="JP"]');

  // Select Japan

 //await page.click('option[value="JP"]');

// Select by value (e.g., "Japan"):
 //await page.locator('select.country').selectOption('JP');
 
  

  // Input card texbox
   await page.fill('input[class="InputElement is-empty Input Input--empty"]','123456789');

  // Input Date texbox
    await page.fill('input[placeholder="MM / YY"]','02/24');

  // Input CVC texbox
    await page.fill('input[name="cvc"]','137');


  // Clicl Button Pay
    await page.click('button[class="payment-button"]');

});

