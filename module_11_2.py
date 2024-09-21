from pprint import pprint


class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1


helper = PaginationHelper(['a', 'b', 'c', 'd', 'f', 'g'], 4)

helper.page_count()
helper.item_count()
print(helper.page_item_count(0))


def introspection_info(obj):
    return_dict = dict()
    return_dict['type'] = type(obj)
    return_dict['attributes'] = [i for i in dir(obj)]
    return_dict['method'] = [getattr(obj, i) for i in dir(obj)
                             if "<class 'method'>" in str(type(getattr(obj, i)))]
    return_dict['module'] = helper.__class__
    return return_dict


number_info = introspection_info(helper)
pprint(number_info)