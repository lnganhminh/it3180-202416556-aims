import unittest
from aims.dvd import DigitalVideoDisc as DVD
from aims.search import search_by_title

class UnicodeSearchTest(unittest.TestCase):
    def test_unicode_casefold_preserves_input(self):
        items = [DVD("Straße"), DVD("Interstellar")]
        before = list(items)
        self.assertEqual(search_by_title(items, "STRASSE"), [items[0]])
        self.assertEqual(items, before)
    def test_empty_keyword_returns_a_separate_list(self):
        items = [DVD("Interstellar")]
        found = search_by_title(items, "")
        self.assertEqual(found, items)
        self.assertIsNot(found, items)
