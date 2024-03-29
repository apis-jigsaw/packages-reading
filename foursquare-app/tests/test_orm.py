import pytest
from src import Category, drop_all_tables, save, test_cursor, test_conn, find_all

@pytest.fixture()
def build_categories():
    drop_all_tables(test_conn, test_cursor)
    category = Category(name = 'Taco Places')
    save(category, test_conn, test_cursor)
    category = Category(name = 'Pizza')
    save(category, test_conn, test_cursor)

    yield

    drop_all_tables(test_conn, test_cursor)

def test_find_all(build_categories):
    categories = find_all(Category, test_cursor)
    assert [category.name for category in categories] == ['Taco Places', 'Pizza']
