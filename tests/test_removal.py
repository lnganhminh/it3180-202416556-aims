import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc as DVD

class RemovalTest(unittest.TestCase):
    def test_missing_disc_keeps_cart_unchanged(self):
        cart = Cart()
        original = DVD("Interstellar", cost=18.95)
        cart.items.append(original)
        self.assertFalse(cart.remove_digital_video_disc(DVD("Unknown")))
        self.assertEqual(cart.items, [original])

    def test_remove_only_one_of_two_equal_discs(self):
        cart = Cart()
        disc = DVD("The Lion King", cost=19.95)
        cart.items.extend([disc, disc])
        self.assertTrue(cart.remove_digital_video_disc(disc))
        self.assertEqual(cart.items, [disc])
        self.assertAlmostEqual(cart.total_cost(), 19.95)
