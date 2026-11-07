"""Search helpers return a new list without changing the input."""


def search_by_category(items, category):
    target = category.casefold()
    return [dvd for dvd in items if dvd.category.casefold() == target]


def search_by_title(items, keyword):
    query = keyword.casefold()
    return [dvd for dvd in items if query in dvd.title.casefold()]
