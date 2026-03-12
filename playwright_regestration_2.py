from playwright.sync_api import sync_playwright

from config import settings
from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(AppRoute.REGISTRATION)

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_button = page.get_by_test_id('registration-page-registration-button')

    email_input.fill(settings.test_user.email)
    username_input.fill(settings.test_user.username)
    password_input.fill(settings.test_user.password)
    registration_button.click()

    page.wait_for_load_state("networkidle")

    context.storage_state(path='browser-state.json')

    page.wait_for_timeout(5000)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto(AppRoute.DASHBOARD)

    page.wait_for_timeout(5000)








