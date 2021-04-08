
class Items:
    def __init__(self, id_item, name, value, description, status):
        self.item_name = name
        self.id_item = id_item
        self.value = value
        self.description = description
        self.status = status

    def __str__(self):
        return "Item name: {}, ID_ITEM: {}, Value: {}, Description: {}, Status: {}".format(
            self.item_name, self.id_item, self.value, self.description, self.status
        )
   