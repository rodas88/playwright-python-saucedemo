from pages.login_page import LoginPage

from utils.config import (
    BASE_URL,
    USERNAME
)


# ==========================
# PASSWORD INCORRECTO
# ==========================

INVALID_PASSWORD = "wrong_password"


# ==========================
# TEST LOGIN NEGATIVO
# ==========================

def test_login_with_invalid_password(page):

    # ==========================
    # ABRIR SAUCEDEMO
    # ==========================

    page.goto(
        BASE_URL
    )

    print("✅ Página abierta")

    # ==========================
    # CREAR PAGE OBJECT
    # ==========================

    login_page = LoginPage(
        page
    )

    # ==========================
    # LOGIN INVALIDO
    # ==========================

    login_page.login(
        USERNAME,
        INVALID_PASSWORD
    )

    print("✅ Login inválido ejecutado")

    # ==========================
    # VALIDAR MENSAJE DE ERROR
    # ==========================

    login_page.validate_login_error()

    print(
        "✅ Mensaje de error validado correctamente"
    )