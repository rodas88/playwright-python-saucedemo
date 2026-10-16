from playwright.sync_api import sync_playwright

USERNAME = "Pruinte"
PASSWORD = "Colombia9++"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://alkos.sce.manh.com/login")

    page.get_by_role(
        "textbox",
        name="Username"
    ).fill(USERNAME)

    page.get_by_role(
        "textbox",
        name="Contraseña"
    ).fill(PASSWORD)

    page.get_by_role(
        "button",
        name="Iniciar sesión"
    ).click()

    print("✅ Login realizado")

    # Esperar que aparezca la URL del Home
    page.wait_for_url(
        "**/udc/landing",
        timeout=60000
    )

    print("✅ Home cargado")
    print(page.url)

    input("✅ Presiona ENTER para cerrar el navegador...")

    browser.close()

