import logging
import re
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page
from page_classes import SearchPage, SearchResultsPage

logger = logging.getLogger(__name__)


def test_navigate_and_check_title(search_page: SearchPage):
    expect(search_page.page).to_have_title(re.compile("Google"))
    logger.info('Test passed: Title is Google')

def test_hover_on_button_and_verify_text_change(page: Page, search_page: SearchPage):
    text_before_hover = search_page.get_text_from_luck_button_before()
    assert text_before_hover == 'I\'m Feeling Lucky'
    search_page.hover_over()
    page.wait_for_timeout(5000)
    text_after_hover = search_page.get_text_from_luck_button_after()
    assert text_after_hover != 'I\'m Feeling Lucky'
    logger.info('Test passed: Hover over and text changed')

def test_verify_search_result_autocomplete(search_page: SearchPage, search_results_page: SearchResultsPage):
    search_page.input_text_in_search_field('Money Forwar')
    search_page.click_autocomplete_suggestion()

    # Will need to click on captcha manually
    expect(search_results_page.get_search_result_title()).to_have_text('マネーフォワード')
    logger.info('Test passed: Autocomplete suggestion found')
