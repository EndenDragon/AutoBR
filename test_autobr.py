import unittest
import autobr
import cv2


def get_screenshot(name):
    return cv2.imread("screenshots/{}.jpeg".format(name), cv2.IMREAD_GRAYSCALE)


class TestStringMethods(unittest.TestCase):
    
    def test_death(self):
        self.assertEqual(autobr.get_state(get_screenshot("death")), "death")

    def test_home(self):
        self.assertEqual(autobr.get_state(get_screenshot("home")), "home")

    def test_in_game(self):
        self.assertEqual(autobr.get_state(get_screenshot("in_game_1")), "in_game")
        self.assertEqual(autobr.get_state(get_screenshot("in_game_2")), "in_game")

    def test_loading(self):
        self.assertEqual(autobr.get_state(get_screenshot("loading")), "loading")

    def test_match_complete(self):
        self.assertEqual(autobr.get_state(get_screenshot("match_complete_1")), "match_complete")
        self.assertEqual(autobr.get_state(get_screenshot("match_complete_2")), "match_complete")

    def test_rewards_received(self):
        self.assertEqual(autobr.get_state(get_screenshot("rewards_received_1")), "rewards_received")
        self.assertEqual(autobr.get_state(get_screenshot("rewards_received_2")), "rewards_received")

    def test_searching(self):
        self.assertEqual(autobr.get_state(get_screenshot("searching")), "searching")

    def test_weapon_selection_deploy(self):
        self.assertEqual(autobr.get_state(get_screenshot("weapon_selection_deploy")), "weapon_selection_deploy")

    def test_weapon_selection(self):
        self.assertEqual(autobr.get_state(get_screenshot("weapon_selection")), "weapon_selection")


if __name__ == '__main__':
    autobr.convert_screen_points()
    unittest.main()
