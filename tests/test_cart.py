from playwright.sync_api import expect

from pages.login_page import LoginPage

from utils.config import (
    BASE_URL,
    USERNAME,
    PASSWORD
)

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
        BASE_URL + "inventory.html"
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