class MainPage:

    def __init__(self, page):
        self.page = page

        self.python_locator = page.locator(
            '//*[@id="docusaurus_skipToContent_fallback"]/main/section[1]/div/div/div[1]/div/p[3]/a[3]')

    def click_on_python_link(self):
        self.python_locator.click()
