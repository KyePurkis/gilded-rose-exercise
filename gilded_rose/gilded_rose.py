from gilded_rose.item import Item

class GildedRose(object):

    def __init__(self, items: list[Item]):
        self.items = items

    def increment_quality(item: Item, value = 1):
        item.quality = min(50, item.quality + value)

    def decrement_quality(item: Item, value):
        item.quality = max(0, item.quality - value)

    def update_quality(self):
        for item in self.items:
            item.sell_in -= 1
            match item.name:
                case "Sulfuras, Hand of Ragnaros":
                    item.sell_in += 1
                case "Conjured Mana Cake":
                    GildedRose.decrement_quality(item, 2)
                    if item.sell_in < 0:
                        GildedRose.decrement_quality(item, 2)
                case "Aged Brie":
                    GildedRose.increment_quality(item)
                    if item.sell_in < 0:
                        GildedRose.increment_quality(item)
                case "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 0:
                        item.quality = 0
                    elif item.sell_in < 5:
                        GildedRose.increment_quality(item, 3)
                    elif item.sell_in < 10:
                        GildedRose.increment_quality(item, 2)
                    else:
                        GildedRose.increment_quality(item)  
                case _:
                    GildedRose.decrement_quality(item, 1)
                    if item.sell_in < 0:
                        GildedRose.decrement_quality(item, 1)
