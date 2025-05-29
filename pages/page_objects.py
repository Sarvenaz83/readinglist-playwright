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
    
    def click_heart_by_index(self, index):
        self.get_heart_by_index(index).click()

    def click_favorites_button(self):
        self.page.locator("[data-testid='favorites']").click()

    def click_catalog_button(self):
        self.page.get_by_test_id("catalog").click()

    def fill_title_and_author(self, title, author):
        self.open_add_book_form()
        self.page.get_by_test_id("add-input-title").fill(title)
        self.page.get_by_test_id("add-input-author").fill(author)
        self.page.wait_for_timeout(500)

    def click_add_submit(self):
        submit_btn = self.page.get_by_test_id("add-submit")
        if submit_btn.is_enabled():
            submit_btn.click()
            self.page.wait_for_timeout(2000)
        else:
            print("❌ Ditt formulär är ogiltigt - 'Lägg till'-knappen är inaktiv.")


    def open_add_book_form(self):
        self.page.get_by_test_id("add-book").click()

    def get_favorites(self):
        return self.page.locator(".book")
    
    def is_heart_filled(self,index):
        heart = self.get_heart_by_index(index)
        class_attr = heart.get_attribute("class")
        return "star selected" in class_attr
    
    def is_heart_empty(self, index):
        return not self.is_heart_filled(index)
    
    
    
