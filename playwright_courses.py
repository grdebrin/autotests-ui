from playwright.sync_api import sync_playwright, expect

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


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto(AppRoute.COURSES)

    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    courses_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    empty_list_title = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_list_title).to_be_visible()
    expect(empty_list_title).to_have_text('There is no results')

    empty_list_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_list_description).to_be_visible()
    expect(empty_list_description).to_have_text('Results from the load test pipeline will be displayed here')


