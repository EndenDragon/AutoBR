import cv2
import imutils
import numpy as np

screen_points = {
    "home": ["home_join_btn.png"],
    "weapon_selection": ["weapon_selection_header_txt.png", "weapon_selection_random_btn.png"],
    "weapon_selection_deploy": ["weapon_selection_deploy_btn.png", "weapon_selection_deploy_header_txt.png"],
    "searching": ["searching_cancel_btn.png", "searching_header_txt.png", "searching_label_txt.png"],
    "loading": ["loading_load_txt.png"],
    "in_game": ["in_game_1_chat_btn.png", "in_game_1_menu_btn.png"],
    "death": ["death_return_btn.png"],
    "rewards_received": ["rewards_received_1_close_btn.png", "rewards_received_1_header_txt.png"],
    "match_complete": ["match_complete_1_drop_reward.png", "match_complete_1_next_btn.png"],
}
state_order = ["weapon_selection", "weapon_selection_deploy", "searching", "home", "loading", "in_game", "death", "rewards_received", "match_complete"]


class ScreenPoint:
    def __init__(self, filename):
        self.filename = filename
        self.image = cv2.imread("screen_points/" + filename)
        self.image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.resized = {}
        for scale in np.linspace(0.2, 1.0, 20)[::-1]:
            self.resized[scale] = imutils.resize(self.image_gray, width = int(self.image_gray.shape[1] * scale))


# Convert screen points to image
def convert_screen_points():
    for state, filenames in screen_points.items():
        for i in range(len(filenames)):
            filename = filenames[i]
            filenames[i] = ScreenPoint(filename)


def get_screenshot():
    return cv2.imread("screenshots/weapon_selection_deploy.jpeg", cv2.IMREAD_GRAYSCALE)


def find_image(image, screenpoint):
    template = screenpoint.image_gray
    loc = False
    threshold = 0.9
    w, h = template.shape[::-1]
    for scale in np.linspace(0.2, 1.0, 20)[::-1]:
        resized = screenpoint.resized[scale]
        w, h = resized.shape[::-1]
        res = cv2.matchTemplate(image, resized, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        if len(list(zip(*loc[::-1]))) > 0:
            break
    return loc


def get_state(image):
    for state in state_order:
        screenpoints = screen_points[state]
        result = True
        for screenpoint in screenpoints:
            find = find_image(image, screenpoint)
            result = result and find and find[0].size > 0 and find[1].size > 0
            if not result:
                break
        if result:
            return state
    return None


if __name__ == "__main__":
    convert_screen_points()
    screenshot = get_screenshot()
    state = get_state(screenshot)
    print(state)
