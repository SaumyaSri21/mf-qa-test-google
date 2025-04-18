import logging

import pytest
from playwright.sync_api import Page
from page_classes import SearchPage, SearchResultsPage


@pytest.fixture(scope="function")
def search_page(page: Page) -> SearchPage:
    page.goto("https://www.google.com")
    return SearchPage(page)

@pytest.fixture(scope="function")
def search_results_page(page: Page) -> SearchResultsPage:
    return SearchResultsPage(page)

# Configure logging for all tests
@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )