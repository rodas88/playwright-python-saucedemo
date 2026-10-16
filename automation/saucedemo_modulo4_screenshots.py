from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

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
    # CREAR PÁGINA
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
    # LOGIN
    # ==========================

    page.get_by_role(
        "textbox",
        name="Username"
    ).fill(USERNAME)

    page.get_by_role(
        "textbox",
        name="Password"
    ).fill(PASSWORD)

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    print("✅ Login realizado")

    # ==========================
    # WAIT URL
    # ==========================

    page.wait_for_url(
        "**/inventory.html"
    )

    print("✅ Inventory cargado")

    # ==========================
    # LOCATOR
    # ==========================

    backpack = page.get_by_text(
        "Sauce Labs Backpack"
    )

    # ==========================
    # ASSERTION
    # ==========================

    expect(backpack).to_be_visible()

    print("✅ Backpack visible")

    # ==========================
    # SCREENSHOT PÁGINA
    # ==========================

    page.screenshot(
        path="inventory_page.png"
    )

    print("✅ Screenshot página guardado")

    # ==========================
    # SCREENSHOT ELEMENTO
    # ==========================

    backpack.screenshot(
        path="backpack.png"
    )

    print("✅ Screenshot Backpack guardado")

    # ==========================
    # PAUSA PARA REVISIÓN
    # ==========================

    input(
        "✅ Módulo 4 terminado. Presiona ENTER para cerrar..."
    )

    # ==========================
    # CERRAR NAVEGADOR
    # ==========================

    browser.close()