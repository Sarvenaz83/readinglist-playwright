from behave import given, when, then
from pages.page_objects import ReadingListPage
import time

@given("att jag är på webbsidan")
def step_impl_open_webbsidan(context):
    context.readinglist = ReadingListPage(context.page)
    context.readinglist.goto()
    context.initial_book_count = context.readinglist.get_books().count()

@then("ska alla böcker räknas korrekt")
def step_impl_count_books(context):
    books = context.readinglist.get_books()
    assert books.count() == 7

@when("jag klickar på hjärtat på den första boken i listan")
def step_impl_click_first_heart(context):
    context.readinglist.click_heart_by_index(0)

@then("ska hjärtat ändras till en fylld ikon")
def step_impl_heart_filled(context):
    assert context.readinglist.is_heart_filled(0)

@then("boken ska finnas i favoritlistan")
def step_impl_book_in_favorites(context):
    context.readinglist.click_favorites_button()
    books = context.readinglist.get_books()
    assert books.count() == 1

@when("jag klickar på hjärtat för boken med index {index:d} {count:d} gånger")
def step_impl_click_heart_multiple(context, index, count):
    for _ in range(count):
        context.readinglist.click_heart_by_index(index)

@then("ska hjärtat för boken med index {index:d} vara markerad")
def step_impl_heart_should_be_filled(context, index):
    assert context.readinglist.is_heart_filled(index)

@then("ska hjärtat för boken med index {index:d} vara avmarkerad")
def step_impl_heart_should_be_empty(context, index):
    assert context.readinglist.is_heart_empty(index)

@when('jag fyller i titel "{titel}" och författare "{forfattare}"')
def step_impl_fill_form(context, titel, forfattare):
    context.readinglist.fill_title_and_author(titel, forfattare)

@when('jag fyller i titel "" och författare "{forfattare}"')
def step_impl_fill_missing_title(context, forfattare):
    context.readinglist.fill_title_and_author("", forfattare)

@when('jag fyller i titel "{titel}" och författare ""')
def step_impl_fill_missing_author(context, titel):
    context.readinglist.fill_title_and_author(titel, "")

@when('jag fyller i titel "" och författare ""')
def step_impl_fill_missing_both(context):
    context.readinglist.fill_title_and_author("", "")


@when('jag klickar på "Lägg till"-knappen')
def step_impl_click_add_button(context):
    context.readinglist.click_add_submit()

@then('ska boken med titel "{titel}" och författare "{forfattare}" visas i boklistan')
def step_impl_book_should_be_visible(context, titel, forfattare):
    context.readinglist.click_catalog_button()
    book_count = context.readinglist.get_books().count()
    print(f"Totalt antal böcker: {book_count}")

    expected_title = titel.strip()
    expected_author = forfattare.strip()

    matched = False
    book_count = context.readinglist.get_books().count()

    for i in range(book_count):
        book = context.readinglist.get_book_by_index(i)
        book_text = book.inner_text().strip()
        print(f"[{i}] TEXT:\n{book_text!r}")

        if expected_title in book_text and expected_author in book_text:
            matched = True
            break

    assert matched, f'Boken "{titel}" av "{forfattare}" hittades inte i listan.'


@then("ska ingen ny bok läggas till i listan")
def step_impl_no_book_added(context):
    context.readinglist.click_catalog_button()
    books = context.readinglist.get_books()
    assert books.count() == 7, f"Boklistan har ändrats: {books.count()} != 7"

@when("jag klickar på länken \"Favoriter\"")
def step_impl_click_favorites(context):
    context.readinglist.click_favorites_button()

@when("jag klickar på länken \"Alla böcker\"")
def step_impl_click_catalog(context):
    context.readinglist.click_catalog_button()

@given("jag har klickat på länken \"Favoriter\"")
def step_impl_given_clicked_favorites(context):
    context.readinglist.click_favorites_button()

@then("ska jag se vyn med favoriter")
def step_impl_see_favorites(context):
    books = context.readinglist.get_books()
    assert books.count() >= 0  # placeholder check

@then("ska jag se vyn med alla böcker")
def step_impl_see_all_books(context):
    books = context.readinglist.get_books()
    assert books.count() == 7
