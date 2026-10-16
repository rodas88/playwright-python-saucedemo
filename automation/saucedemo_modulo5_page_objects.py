from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

from login_page import LoginPage

# ==========================
# CREDENCIALES SAUCEDEMO
# ==========================

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# ==========================
# INICIO DE PLAYWRIGHT
# ==========================

with sync_playwright() as p:

    # ==========================
    # ABRIR NAVEGADOR
    # ==========================

    browser = p.chromium.launch(
        headless=False
    )

    # ==========================
    # CREAR CONTEXTO
    # ==========================

    context = browser.new_context()

    # ==========================
    # CREAR PAGINA
    # ==========================

    page = context.new_page()

    # ==========================
    # ABRIR SAUCEDEMO
    # ==========================

    page.goto(
        "https://www.saucedemo.com/"
    )

    print("✅ Página abierta")

    # ==========================
    # CREAR PAGE OBJECT
    # ==========================

    login_page = LoginPage(page)

    print("✅ Page Object creado")

    # ==========================
    # LOGIN
    # ==========================

    login_page.login(
        USERNAME,
        PASSWORD
    )

    print("✅ Login ejecutado desde Page Object")

    # ==========================
    # ASSERTION URL
    # ==========================

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    print("✅ Login validado")

    # ==========================
    # PAUSA PARA REVISIÓN
    # ==========================

    input(
        "✅ Módulo 5 terminado. Presiona ENTER para cerrar..."
    )

    # ==========================
    # CERRAR NAVEGADOR
    # ==========================

    browser.close()