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
    # ASSERTION URL
    # ==========================

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    print("✅ URL validada correctamente")

    # ==========================
    # LOCATORS POR TEXTO
    # ==========================

    backpack = page.get_by_text(
        "Sauce Labs Backpack"
    )

    bike_light = page.get_by_text(
        "Sauce Labs Bike Light"
    )

    # ==========================
    # LOCATORS POR ROLE
    # ==========================

    add_to_cart_buttons = page.get_by_role(
        "button",
        name="Add to cart"
    )

    # ==========================
    # ASSERTIONS VISIBILIDAD
    # ==========================

    expect(backpack).to_be_visible()

    print(
        "✅ Backpack visible"
    )

    expect(bike_light).to_be_visible()

    print(
        "✅ Bike Light visible"
    )

    # ==========================
    # ASSERTION CANTIDAD
    # ==========================

    expect(
        add_to_cart_buttons
    ).to_have_count(6)

    print(
        "✅ Existen 6 botones Add to cart"
    )

    # ==========================
    # PAUSA PARA REVISIÓN
    # ==========================

    input(
        "✅ Módulo 2 terminado. Presiona ENTER para cerrar..."
    )

    # ==========================
    # CERRAR NAVEGADOR
    # ==========================

    browser.close()