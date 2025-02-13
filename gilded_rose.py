# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemUpdater(ABC):
    def __init__(self, item):
        self.item = item
    
    @abstractmethod
    def update(self):
        pass
    
    def decrease_quality(self, amount=1):
        if self.item.quality > 0:
            self.item.quality = max(0, self.item.quality - amount)

    def increase_quality(self, amount=1):
        if self.item.quality < 50:
            self.item.quality = min(50, self.item.quality + amount)

    def decrease_sell_in(self):
        self.item.sell_in -= 1

class RegularItemUpdater(ItemUpdater):
    def update(self):
        self.decrease_quality(1)
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.decrease_quality(1)

class AgedBrieUpdater(ItemUpdater):
    def update(self):
        if self.item.sell_in <= 0:
            self.item.quality = 0
        elif self.item.sell_in <= 5:
            self.increase_quality(3)
        elif self.item.sell_in <= 10:
            self.increase_quality(2)
        else:
            self.increase_quality(1)
        self.decrease_sell_in()

class SulfurasUpdater(ItemUpdater):
    def update(self):
        pass

class BackstagePassUpdater(ItemUpdater):
    def update(self):
        pass

class ConjuredUpdater(ItemUpdater):
    def update(self):
        pass

class ItemUpdaterFactory:
    @staticmethod
    def get_updater(item):
        if item.name == "Aged Brie":
            return AgedBrieUpdater(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdater(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdater(item)
        elif item.name.startswith("Conjured"):
            return ConjuredUpdater(item)
        else:
            return RegularItemUpdater(item)
    
class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = ItemUpdaterFactory.get_updater(item)
            updater.update()
            