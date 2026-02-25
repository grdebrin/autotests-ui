import pytest
from playwright.sync_api import expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):

    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    courses_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon).to_be_visible()

    empty_list_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_list_title).to_be_visible()
    expect(empty_list_title).to_have_text('There is no results')

    empty_list_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_list_description).to_be_visible()
    expect(empty_list_description).to_have_text('Results from the load test pipeline will be displayed here')

