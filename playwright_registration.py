from playwright.sync_api import sync_playwright, expect

from config import settings
from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(AppRoute.REGISTRATION)

    email_registration_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_registration_input.fill(settings.test_user.email)

    username_registration_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_registration_input.fill(settings.test_user.username)

    password_registration_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_registration_input.fill(settings.test_user.password)

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()



