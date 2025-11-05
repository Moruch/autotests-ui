from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    """
    Тест проверяет отображение пустого списка курсов.
    Использует фикстуру chromium_page_with_state для доступа к авторизованной сессии.
    """
    page = chromium_page_with_state

    # Переходим на страницу курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверка текста заголовка "Courses"
    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_have_text('Courses')

    # Проверка наличие и видимость пустого блока
    icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    # Проверка текста "There is no results"
    empty_title = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_title).to_have_text('There is no results')

    # Проверка текста "Results from the load test pipeline will be displayed here"
    empty_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_description).to_have_text('Results from the load test pipeline will be displayed here')
