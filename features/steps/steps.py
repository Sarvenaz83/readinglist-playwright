from behave import given, when, then
from playwright.sync_api import sync_playwright, expect
from pages.page_objects import ReadingListPage
import time


browser = None
page = None
context = None

@given("att jag är på webbsidan")
def step_impl_open_webbsidan(context):
    context.readinglist.goto()

        
@then("ska alla böcker räknas korrekt")
def set_impl_count_books(context):
    books = context.readinglist.get_books()
    count = books.count()
    assert count > 0, "Inga böcker hittades"

@when("jag klickar på hjärtat på den första boken i listan")
def step_impl_click_heart(context):
    page= context.page
    page.wait_for_selector(".book")
    first_heart_icon = page.locator(".book").first.locator(".star")
    first_heart_icon.wait_for(state="visible")
    first_heart_icon.click()

@then("ska hjärtat ändras till en fylld ikon")
def step_impl_check_heart_fikked(context):
    page = context.page
    heart_icon = page.locator(".book").first.locator(".star")
    icon_text = heart_icon.inner_text()
    assert "❤️" in icon_text, "Ikonen är inte markerad som favorit"

@then("boken ska finnas i favoritlistan")
def step_impl_check_in_favorites(context):
    page = context.page
    fav_button = page.locator("[data-testid='favorites']")
    fav_button.wait_for(state="visible")
    fav_button.click()
    page.wait_for_selector(".book")

    favorite_books = page.locator(".book")
    assert favorite_books.count() > 0, "Inga böcker i favoritlistan"

@when('jag klickar på hjärtat för boken med index {index:d} {antal:d} gånger')
def step_impl_click_multiple(context, index, antal):
    heart_icon = context.readinglist.get_heart_by_index(index)
    for _ in range(antal):
        heart_icon.wait_for(state="visible")
        heart_icon.click()
        # Väntar på UI-uppdatering mellan klick
        time.sleep(0.3) 


@then('ska hjärtat för boken med index {index:d} vara {status}')
def step_impl_check_status(context, index, status):

    if status == "markerad":
        assert context.readinglist.is_heart_filled(index), "Förväntade markerad (❤️) men var inte det"
    elif status == "avmarkerad":
        assert context.readinglist.is_heart_empty(index), "Förväntade avmarkerad (🤍) men var fortfarande markerad"
    else:
        raise ValueError(f"Okänd status: {status}")

    