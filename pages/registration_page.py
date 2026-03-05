from components.authentication.registration_form_component import RegistrationFormComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from elements.button import Button
from pages.base_page import BasePage
from playwright.sync_api import Page

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.dashboard_toolbar = DashboardToolbarViewComponent(page)

        self.registration_button = Button(page,'registration-page-registration-button', 'Registration')

    def click_registration_button(self):
        self.registration_button.click()

