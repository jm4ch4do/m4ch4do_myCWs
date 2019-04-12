# ----- Problem: PaginationHelper (5ku)
# ----- URL: https://www.codewars.com/kata/515bb423de843ea99400000a


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return len(self.collection) // self.items_per_page + 1

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        full_pages = len(self.collection) // self.items_per_page
        items_last_page = len(self.collection) % self.items_per_page

        if page_index < full_pages:
            return self.items_per_page

        if page_index == full_pages:
            return items_last_page if items_last_page != 0 else -1

        return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        return item_index // self.items_per_page if 0 <= item_index < len(self.collection) else -1


# ------------------ TEST --------------------
helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
a = helper.page_count()  # should == 2
a = helper.item_count()  # should == 6
a = helper.page_item_count(0)  # should == 4
a = helper.page_item_count(1)  # last page - should == 2
a = helper.page_item_count(2)  # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
a = helper.page_index(5)  # should == 1 (zero based index)
a = helper.page_index(2)  # should == 0
a = helper.page_index(20)  # should == -1
a = helper.page_index(-10)  # should == -1 because negative indexes are invalid
