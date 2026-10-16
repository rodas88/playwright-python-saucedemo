from playwright.sync_api import sync_playwright

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
    # ESPERAR PÁGINA INVENTARIO
    # ==========================

    page.wait_for_url(
        "**/inventory.html",
        timeout=10000
    )

    print("✅ Inventario cargado")

    # ==========================
    # LOCATORS POR TEXTO
    # ==========================

    backpack = page.get_by_text(
        "Sauce Labs Backpack",
    )

    bike_light = page.get_by_text(
        "Sauce Labs Bike Light",
    )

    # ==========================
    # LOCATORS POR ROLE
    # ==========================

    add_to_cart_buttons = page.get_by_role(
        "button",
        name="Add to cart"
    )

    # ==========================
    # VALIDACIONES COUNT()
    # ==========================

    print(
        "Backpack encontrados:",
        backpack.count()
    )

    print(
        "Bike Light encontrados:",
        bike_light.count()
    )

    print(
        "Botones Add to cart encontrados:",
        add_to_cart_buttons.count()
    )

    # ==========================
    # LOCATOR OBJECTS
    # ==========================

    print(
        "Tipo locator Backpack creado correctamente"
    )

    print(
        "Tipo locator Bike Light creado correctamente"
    )

    print(
        "Tipo locator Add To Cart creado correctamente"
    )

    # ==========================
    # PAUSA PARA REVISIÓN
    # ==========================

    input(
        "✅ Módulo 1 terminado. Presiona ENTER para cerrar..."
    )

    # ==========================
    # CERRAR NAVEGADOR
    # ==========================

    browser.close()