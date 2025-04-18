from playwright.sync_api import Page


class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator("//textarea[@title]")
        self.autocomplete_input = page.locator("//div[@aria-label='money forward']").first
        self.lucky_button_before = page.get_by_label("I'm Feeling Lucky").filter(visible=True).first
        self.hover_button =  page.locator('//input[@name="btnI"]').filter(visible=True).first
        self.lucky_button_after = page.locator('//input[@value="I\'m Feeling Lucky"]/following-sibling::div').filter(visible=True)


    def get_text_from_luck_button_before(self) -> str:
        return self.lucky_button_before.get_attribute('aria-label')

    def get_text_from_luck_button_after(self) -> str:
        return self.lucky_button_after.get_attribute('aria-label')

    def hover_over(self):
        self.hover_button.hover()

    def input_text_in_search_field(self, text: str):
        self.search_input.fill(text)

    def click_autocomplete_suggestion(self):
        self.autocomplete_input.click()





class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_result_title = page.locator('//*[@data-attrid="title"]')

    def get_search_result_title(self):
        return self.search_result_title

