# -*- coding: utf-8 -*-
from __future__ import annotations


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item_quality(item)

    def update_item_quality(self, item: Item):
        item.sell_in -= 1
        
        if item.name == "Sulfuras, Hand of Ragnaros":
            item.quality = 80
            return

        if item.name == "Aged Brie":
            item.quality = item.quality + 1

        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.sell_in < 1:
                item.quality = 0
            elif item.sell_in < 6:
                item.quality = item.quality + 3
            elif item.sell_in < 11:
                item.quality = item.quality + 2
            else:
                item.quality =  item.quality + 1
        
        elif item.name == "Conjured Item":
            item.quality = item.quality - 2

        else:
            item.quality = item.quality - 1
            if item.sell_in < 0:
                item.quality -= 1

        if item.quality < 0:
            item.quality = 0
        elif item.quality > 50:
            item.quality = 50


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)