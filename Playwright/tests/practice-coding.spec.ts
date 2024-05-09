// code demo click button


import { test, expect } from '@playwright/test';

//TC1

test('Input text in search box and click on  button searching - 1', async ({ page }) => {
  await page.goto('https://www.google.com');

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(/Google/);

  // input search box

  await page.keyboard.type("Hello"); // types instantly
  await page.keyboard.type("World") ; //delay=100) # types slower, like a user

  // page.fill
  // click vao nut search

  await page.getByRole('button', { name: 'Tìm trên Google' }).click(); 
 
  // page.click 

  // oke, tuy cui bap nhung van xai duoc :)) , code thui quac, smell code :))

  
  // close browser

  //await browser.close();

  // tim cach close browser - nhiem vu ngay mai 
});

// update code version 2

//TC2

test('Input text in search box and click on  button searching - 2', async ({ page }) => {
  await page.goto('https://www.google.com');

  // Expect a title "to contain" a substring.
  await expect(page).toHaveTitle(/Google/);

  // input search box

  //await page.keyboard.type("Hello"); // types instantly
  //await page.keyboard.type("World") ; //delay=100) # types slower, like a user

  // page.fill
  // click vao nut search

  //await page.getByLabel('Tìm kiếm', { exact: true }).fill('Pikachu');

  //await page.fill('input[name="APjFqb"]','Apple M1');

  await page.fill('textarea[class="gLFyf"]','Apple M1');

  

 //await page.getByRole('button', { name: 'Tìm trên Google' }).click(); 
 
  // page.click 

  //await page.getByRole('button', { name: 'Tìm trên Google' }).click(); 
  // oke, tuy cui bap nhung van xai duoc :)) , code thui quac, smell code :))


 // await page.click('input[class="gNO89b"]');

  await page.click('input[value="Tìm trên Google"]');
  // await page.click('text = "Apple M1"'); 
});

// chay song song cac test case

//  Done - chỉ cần run nút tổng là xong. 

// open new page


// test('open new page', async ({ page }) => {

// //const context = await browser.newContext();

// const context = await browser.newContext();

// const page = await context.newPage();




//   // await page.goto('https://playwright.dev/');

//   // // Click the get started link.
//   // await page.getByRole('link', { name: 'Get started' }).click();

//   // // Expects page to have a heading with the name of Installation.
//   // await expect(page.getByRole('heading', { name: 'Installation' })).toBeVisible();

//   await browser.close();
// });

// TC3

test('open new page 2', async ({ page }) => {


 
   const browser = await playwright["chromium"].launch({headless : false});
  //const page = await browser.newPage();
  await page.goto('https://www.facebook.com/');
  var pagePromise = page.context().waitForEvent('page', p => p.url() =='https://www.messenger.com/');
  await page.click('text=Messenger', { modifiers: ['Meta']});
  const newPage = await pagePromise;
  await newPage.bringToFront();
  await browser.close();
  
 
  });
  
//TC4

test('Open new page - 3', async ({ page }) => {

  
  // Navigate to a specific URL.
  await page.goto('https://facebook.com');

  // Click a link or button that opens a new page.
  await page.click('a[target="_blank"]'); // Replace with the appropriate selector.

  // Expect the new page to be open.
 // await expect(page).toHaveTitle('New Page Title'); // Replace with the expected title.
});


//TC5
test('Open new page - 4', async ({ page }) => {

  const { firefox } = require('playwright');  // Or 'firefox' or 'webkit'.

(async () => {
  const browser = await firefox.launch();
  const page = await browser.newPage();
  await page.goto('https://facebook.com');
  // other actions...
  await browser.close();
})();



await page.goto('https://www.facebook.com/');
var pagePromise = page.context().waitForEvent('page', p => p.url() =='https://www.messenger.com/');
await page.click('text=Messenger', { modifiers: ['Meta']});
const newPage = await pagePromise;
await newPage.bringToFront();



});

// viết toàn bộ demo các testcase tại đây

// iframe  - code test case contain iframe
// tim trang web chua iframe de test
// https://stripe-payments-demo.appspot.com/

//TC6
test('Input Iframe - 1', async ({ page }) => {

  
  // Navigate to a specific URL.
  await page.goto('https://facebook.com');

  // Click a link or button that opens a new page.
  await page.click('a[target="_blank"]'); // Replace with the appropriate selector.

  // Expect the new page to be open.
 // await expect(page).toHaveTitle('New Page Title'); // Replace with the expected title.
});

// TC6
// code test case upload file in XHR
// https://uppy.io/examples/