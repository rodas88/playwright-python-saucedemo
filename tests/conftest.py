import pytest

from playwright.sync_api import sync_playwright


# ==========================
# FIXTURE PAGE
# ==========================

@pytest.fixture
def page():

    # ==========================
    # INICIAR PLAYWRIGHT
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
        # ENTREGAR PAGE AL TEST
        # ==========================

        yield page

        # ==========================
        # TEARDOWN
        # ==========================

        context.close()

        browser.close()