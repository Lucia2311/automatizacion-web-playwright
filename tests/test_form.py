import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/automation-practice-form")
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").press("CapsLock")
    page.get_by_role("textbox", name="First Name").fill("L")
    page.get_by_role("textbox", name="First Name").press("CapsLock")
    page.get_by_role("textbox", name="First Name").fill("Lucia")
    page.get_by_role("textbox", name="First Name").press("Tab")
    page.get_by_role("textbox", name="Last Name").press("CapsLock")
    page.get_by_role("textbox", name="Last Name").fill("G")
    page.get_by_role("textbox", name="Last Name").press("CapsLock")
    page.get_by_role("textbox", name="Last Name").fill("Gonzalez")
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("teste@test.com")
    page.get_by_role("radio", name="Female").check()
    page.get_by_role("textbox", name="Mobile Number").click()
    page.get_by_role("textbox", name="Mobile Number").fill("0998982988")
    page.locator("#dateOfBirthInput").click()
    page.get_by_role("combobox").nth(1).select_option("2004")
    page.get_by_role("gridcell", name="Choose Wednesday, October 6th,").click()
    page.get_by_role("checkbox", name="Music").check()
    page.get_by_role("textbox", name="Current Address").click()
    page.get_by_role("textbox", name="Current Address").press("CapsLock")
    page.get_by_role("textbox", name="Current Address").fill("A")
    page.get_by_role("textbox", name="Current Address").press("CapsLock")
    page.get_by_role("textbox", name="Current Address").fill("Asuncion, Paraguay")
    
    # --- CORRECCIÓN DE ESTADO Y CIUDAD ---
    # 1. Hacemos clic en el campo Estado para abrir el menú desplegable
    page.locator("#state").click()
    # 2. Seleccionamos Uttar Pradesh de forma segura
    page.get_by_text("Uttar Pradesh", exact=True).click()
    
    # 3. Hacemos clic en el campo Ciudad para abrir su menú
    page.locator("#city").click()
    # 4. Seleccionamos Merrut
    page.get_by_text("Merrut", exact=True).click()
    # ------------------------------------

    page.get_by_role("button", name="Submit").click()
    page.get_by_role("button", name="Close").dblclick()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)