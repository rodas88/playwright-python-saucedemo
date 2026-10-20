import pytest

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

from pages.login_page import LoginPage

from utils.config import (
    BASE_URL,
    USERNAME,
    PASSWORD
)

# ==========================
# FIXTURE PAGE
# ==========================

@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        context = browser.new_context()

        page = context.new_page()

        yield page

        context.close()

        browser.close()


# ==========================
# TEST CART
# ==========================

def test_add_product_to_cart(page):

    # ==========================
    # ABRIR SAUCEDEMO
    # ==========================

    page.goto(
        BASE_URL
    )

    print("✅ Página abierta")

    # ==========================
    # LOGIN
    # ==========================

    login_page = LoginPage(page)

    login_page.login(
        USERNAME,
        PASSWORD
    )

    print("✅ Login ejecutado")

    # ==========================
    # VALIDAR INVENTARIO
    # ==========================

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    print("✅ Inventory validado")

    # ==========================
    # AGREGAR BACKPACK
    # ==========================

    page.get_by_role(
        "button",
        name="Add to cart"
    ).first.click()

    print("✅ Producto agregado")

    # ==========================
    # ABRIR CARRITO
    # ==========================

    page.locator(
        ".shopping_cart_link"
    ).click()

    print("✅ Carrito abierto")

    # ==========================
    # VALIDAR PRODUCTO
    # ==========================

    backpack = page.get_by_text(
        "Sauce Labs Backpack"
    )

    expect(
        backpack
    ).to_be_visible()

    print(
        "✅ Backpack encontrado en carrito"
    )