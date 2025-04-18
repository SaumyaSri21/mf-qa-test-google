# This framework is designed using Playwright + Pytest

## Installations

- install python3
- Run `pip install pytest-playwright` to install playwright with pytest framework
- Run `playwright install` to install playwright browsers
- Run `pip install pytest-html` to install html reports

## Test Cases

1. Verify navigate to the url and check title
2. Verify button text change from "I'm feeling lucky" to some random text on hover
3. Verify autocomplete suggestions on inputting search string and search results

> The framework uses Page Object Model pattern

## Files
- `conftest.py` : Contains fixtures (hooks) that run before each test to navigate to url and crete page objects
- `page_classes.py` : Classes that encapsulate page locators and actions
- `test_google.py` : Test files

## Running the test

To execute the tests, run `pytest --html=report.html --self-contained-html --headed` command. After the tests are run `report.html` will be generated.
