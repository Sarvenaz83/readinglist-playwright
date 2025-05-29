from playwright.sync_api import sync_playwright
from pages.page_objects import ReadingListPage

def before_all(context):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)  # یا True موقع تحویل
    page = browser.new_page()
    context.browser = browser
    context.page = page
    context.playwright = playwright

def before_scenario(context, scenario):
    context.readinglist = ReadingListPage(context.page)
    context.readinglist.goto()

def after_all(context):
    context.browser.close()
    context.playwright.stop()
