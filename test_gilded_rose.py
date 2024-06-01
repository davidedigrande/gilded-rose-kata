import pytest
from main import Item, GildedRose


def test_update_quality_sell_in_date_passed():
    """Once the sell by date has passed, Quality degrades twice as fast"""
    item = Item(name="foo", sell_in=10, quality=24)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.quality == 23

    item = Item(name="foo", sell_in=-1, quality=24)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.quality == 22

def test_update_quality_never_negative():
    """The Quality of an item is never negative"""
    item = Item(name="foo", sell_in=-1, quality=0)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.quality == 0

def test_update_quality_aged_brie_increases():
    """“Aged Brie” actually increases in Quality the older it gets"""
    item = Item(name="Aged Brie", sell_in=10, quality=22)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.quality == 23

def test_update_quality_never_greater_than_fifty():
    """The Quality of an item is never more than 50"""
    item = Item(name="Aged Brie", sell_in=-1, quality=50)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.quality == 50

def test_update_quality_sulfuras_do_not_decrease():
    """“Sulfuras”, being a legendary item, never has to be sold or decreases in Quality"""
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.quality == 80

def test_update_quality_backstage_passes():
    """
    “Backstage passes”, like aged brie, increases in Quality as it’s SellIn value approaches;
    Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but Quality drops to 0 after the concert
    """
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=24)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.quality == 25

    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=24)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.quality == 26

    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=24)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.quality == 27

    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=24)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.quality == 0

def test_update_quality_conjured_items():
    """“Conjured” items degrade in Quality twice as fast as normal items"""
    item = Item(name="Conjured Item", sell_in=10, quality=24)
    gilded_rose = GildedRose(items=[item])
    gilded_rose.update_quality()
    assert item.quality == 22