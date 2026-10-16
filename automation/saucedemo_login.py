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

    page.wait_for_timeout(2000)

    # ==========================
    # INGRESAR USUARIO
    # ==========================

    page.get_by_role(
        "textbox",
        name="Username"
    ).fill(USERNAME)

    print("✅ Usuario ingresado")

    page.wait_for_timeout(2000)

    # ==========================
    # INGRESAR CONTRASEÑA
    # ==========================

    page.get_by_role(
        "textbox",
        name="Password"
    ).fill(PASSWORD)

    print("✅ Contraseña ingresada")

    page.wait_for_timeout(2000)

    # ==========================
    # HACER LOGIN
    # ==========================

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    print("✅ Botón Login presionado")

    # ==========================
    # ESPERAR INVENTARIO
    # ==========================

    page.wait_for_url(
        "**/inventory.html",
        timeout=10000
    )

    print("✅ Login exitoso")

    print(
        "✅ URL actual:",
        page.url
    )

    # ==========================
    # VER INVENTARIO
    # ==========================

    page.wait_for_timeout(5000)

    # ==========================
    # PAUSA FINAL
    # ==========================

    input(
        "✅ Presiona ENTER para cerrar..."
    )

    # ==========================
    # CERRAR NAVEGADOR
    # ==========================

    browser.close()