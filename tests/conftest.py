from typing import Any, Generator

import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) -> Generator[Page, Any, None]:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state():
    """
       Фикстура для регистрации нового пользователя и сохранения состояния браузера.
       Выполняется один раз за сессию тестирования.
    """
    state_file = "browser-state.json"

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Переходим на страницу регистрации
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполняем поле email
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("luser.name@gmail.com")

        # Заполняем поле Username
        user_input = page.get_by_test_id('registration-form-username-input').locator('input')
        user_input.fill("luser")

        # Заполняем поле Password
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("lpassword")

        # Нажимаем на кнопку Registration
        login_button = page.get_by_test_id('registration-page-registration-button')
        login_button.click()

        # Сохраняем состояние браузера (куки и localStorage) в файл
        context.storage_state(path=state_file)

        # Закрываем браузер
        browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Generator[Page, Any, None]:
    """
    Фикстура для создания страницы с сохраненным состоянием браузера.
    Использует файл browser-state.json для авторизованной сессии.
    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page
