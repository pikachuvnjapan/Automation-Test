import re
from playwright.sync_api import Playwright, sync_playwright, expect


# Câu lệnh record testcase đối với python
# playwright.exe codegen stripe-payments-demo.appspot.com
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://stripe-payments-demo.appspot.com/")
    page.get_by_placeholder("Jenny Rosen").click()
    page.get_by_placeholder("Jenny Rosen").fill("Le Quang Dung")
    page.get_by_placeholder("jenny@example.com").click()
    page.get_by_placeholder("jenny@example.com").fill("pikachu@gmail.com")
    page.get_by_placeholder("Berry Street Suite 550").click()
    page.get_by_placeholder("Berry Street Suite 550").fill("Hanoi")
    page.get_by_placeholder("San Francisco").click()
    page.get_by_placeholder("San Francisco").fill("Hanoi")
    page.get_by_placeholder("CA").fill("Hanoi")
    page.get_by_placeholder("94103").click()
    page.get_by_placeholder("94103").fill("10000")
    page.get_by_label("Country Australia Austria").select_option("JP")
    page.frame_locator("iframe[name=\"__privateStripeFrame8183\"]").get_by_placeholder("Card number").click()
    page.frame_locator("iframe[name=\"__privateStripeFrame8183\"]").get_by_placeholder("Card number").fill("42")
    page.frame_locator("iframe[name=\"__privateStripeFrame8183\"]").get_by_placeholder("MM / YY").click()
    page.frame_locator("iframe[name=\"__privateStripeFrame8183\"]").get_by_placeholder("MM / YY").fill("02 / 24")
    page.frame_locator("iframe[name=\"__privateStripeFrame8183\"]").get_by_placeholder("CVC").click()
    page.frame_locator("iframe[name=\"__privateStripeFrame8183\"]").get_by_placeholder("CVC").fill("132")
    page.get_by_role("button", name="Pay €").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
