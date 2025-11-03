from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    context = browser.new_context()
    # Открываем новую страницу в рамках контекста
    page = context.new_page()

    # Переходим на страницу входа
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

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser_courses-state.json")


with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser_courses-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        page.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        #Проверка текста заголовка "Courses"
        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_have_text('Courses')

        #Проверка наличие и видимость пустого блока
        icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon).to_be_visible()

        # Проверка текста "There is no results"
        courses_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_title).to_have_text('There is no results')


        # Проверка текста "Results from the load test pipeline will be displayed here"
        courses_title = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(courses_title).to_have_text('Results from the load test pipeline will be displayed here')


