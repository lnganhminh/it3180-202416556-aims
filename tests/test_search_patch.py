import unittest
from aims.dvd import DigitalVideoDisc as DVD
from aims.search import search_by_title

class SearchPatchTest(unittest.TestCase):
    def test_mixed_case_title_search(self):
        discs = [DVD("The Lion King"), DVD("Interstellar")]
        for query in ("lion", "LION", "LiOn"):
            with self.subTest(query=query):
                self.assertEqual(search_by_title(discs, query), [discs[0]])
