from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utils.config import (
    BASE_URL,
    USERNAME,
    PASSWORD
)


# ==========================
# DATOS DEL CHECKOUT
# ==========================

FIRST_NAME = "Johan"
LAST_NAME = "Guerra"
POSTAL_CODE = "250001"


# ==========================
# TEST CHECKOUT
# ==========================

def test_complete_checkout(page):

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

    expect(page).to_have_url(
        BASE_URL + "inventory.html"
    )

    print("✅ Login validado")

    # ==========================
    # INVENTARIO
    # ==========================

    inventory_page = InventoryPage(
        page
    )

    inventory_page.add_backpack_to_cart()

    print("✅ Backpack agregado")

    inventory_page.open_cart()

    print("✅ Carrito abierto")

    # ==========================
    # CARRITO
    # ==========================

    cart_page = CartPage(
        page
    )

    cart_page.validate_backpack()

    print("✅ Backpack validado en carrito")

    cart_page.start_checkout()

    print("✅ Checkout iniciado")

    # ==========================
    # CHECKOUT
    # ==========================

    checkout_page = CheckoutPage(
        page
    )

    checkout_page.complete_customer_information(
        FIRST_NAME,
        LAST_NAME,
        POSTAL_CODE
    )

    print("✅ Información del comprador completada")

    # ==========================
    # FINALIZAR COMPRA
    # ==========================

    checkout_page.finish_order()

    print("✅ Orden finalizada")

    # ==========================
    # VALIDAR COMPRA
    # ==========================

    checkout_page.validate_order_confirmation()

    print("✅ Compra completada correctamente")