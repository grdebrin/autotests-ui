from playwright.sync_api import sync_playwright, expect

from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(AppRoute.LOGIN)

    # unknown = page.locator('unknown')
    # expect(unknown).to_be_visible()

    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    # page.evaluate("""
    #     const title = document.getElementById('authentication-ui-course-title-text');
    #     title.textContent = 'New Text';
    #     """)
