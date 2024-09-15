import pytest
from playwright.sync_api import Playwright


@pytest.fixture(autouse=True)
def set_test_id_attribute(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-test")
