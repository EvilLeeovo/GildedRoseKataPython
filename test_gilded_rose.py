# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]

    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

    def test_get_item_names_method_exists(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        names = gilded_rose.get_item_names()  # AttributeError raised here
        self.assertEqual(["foo"], names)

    def test_conjured_items_quality_degrades_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # Correct expectation: Conjured items should lose 2 quality points
        self.assertNotEqual(4, items[0].quality,
                            "Conjured items should degrade twice as fast, but this is designed to fail.")

    def test_quality_never_negative(self):
        items = [Item("Elixir of the Mongoose", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # Correct expectation: Quality should not drop below 0
        self.assertLess(items[0].quality, 0, "Quality should never be negative, but this is designed to fail.")

    def test_backstage_passes_quality_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # Correct expectation: Backstage passes should have quality 0 after the concert
        self.assertNotEqual(0, items[0].quality,
                            "Backstage passes should drop to 0 quality after the concert, but this is designed to fail.")

    def test_aged_brie_quality_exceeds_50(self):
        items = [Item("Aged Brie", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        # Correct expectation: Quality should not exceed 50
        self.assertGreater(items[0].quality, 50,
                           "Aged Brie quality should not exceed 50, but this is designed to fail.")

    def test_sulfuras_quality_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertNotEqual(80, items[0].quality, "Sulfuras quality should not change, but this is designed to fail.")
        self.assertNotEqual(5, items[0].sell_in, "Sulfuras sell-in should not change, but this is designed to fail.")


if __name__ == '__main__':
    unittest.main()
