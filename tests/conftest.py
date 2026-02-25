import pytest
from playwright.sync_api import Page, Playwright

# Фикстура созданная во время урока
@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_button = page.get_by_test_id('registration-page-registration-button')

    email_input.fill('user.name@gmail.com')
    username_input.fill('username')
    password_input.fill('password')
    registration_button.click()

    page.wait_for_load_state("networkidle")

    context.storage_state(path='browser-state.json')

    context.close()
    browser.close()

@pytest.fixture
def chromium_page_with_state(playwright: Playwright, initialize_browser_state: Page):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    yield context.new_page()

    context.close()
    browser.close()
