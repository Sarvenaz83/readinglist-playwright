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
        return self.get_book_by_index(index).locator(".star")
    
    def click_favorites_bytton(self):
        self.page.locator("[data-testid='favorites']").click()

    def get_favorites(self):
        return self.page.locator(".book")
    
    def is_heart_filled(self,index):
        heart = self.get_heart_by_index(index)
        class_attr = heart.get_attribute("class")
        return "star selected" in class_attr
    
    def is_heart_empty(self, index):
        return not self.is_heart_filled(index)
    
