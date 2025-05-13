class ReadingListPage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")

    def get_books(self):
        return self.page.locator(".book")
    
    def get_book_by_index(self, index):
        return self.page.locator(".book").nth(index)
    
    def get_heart_by_index(self, index):
        return self.get_heart_by_index(index).locator(".star")
    
    def click_favorites_bytton(self):
        self.page.locator("[data-testid='favorites']").click()

    def get_favorites(self):
        return self.page.locator(".book")