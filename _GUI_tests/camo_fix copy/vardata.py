RUNNING = False
RANDOMIZED = False
SAVE_LOGIN = False
SEARCH_TERM = "google.com"
SPEED = 0.8
FOLLOW_COUNT = 0
DESIRED_FOLLOW_AMOUNT = 99
FOLLOWED = []
WINDOW = None
CURRENTLY_FOLLOWING = 0

EMAIL = "spuffygaming@gmail.com"
PASSWORD = "Bumblebee098!!"  # TODO load from file

THREAD = None


def set_currently_following(amt):
    global CURRENTLY_FOLLOWING
    CURRENTLY_FOLLOWING = amt


def add_currently_following():
    global CURRENTLY_FOLLOWING
    CURRENTLY_FOLLOWING += 1


def get_currently_following():
    return CURRENTLY_FOLLOWING


def set_desired_follow_amount(amt):
    global DESIRED_FOLLOW_AMOUNT
    DESIRED_FOLLOW_AMOUNT = amt


def get_desired_follow_amount():
    return DESIRED_FOLLOW_AMOUNT


def set_savelogin(save):
    global SAVE_LOGIN
    SAVE_LOGIN = save


def get_savelogin():
    return SAVE_LOGIN


def set_randomized(random):
    global RANDOMIZED
    RANDOMIZED = random


def get_randomized():
    return RANDOMIZED


def set_follow_count(follow_count):
    global FOLLOW_COUNT
    FOLLOW_COUNT = follow_count


def get_follow_count():
    return FOLLOW_COUNT


def set_followed(follow_count):
    global FOLLOWED
    FOLLOWED = follow_count


def get_followed():
    return FOLLOWED


def set_speed(speed):
    global SPEED
    SPEED = speed


def get_speed():
    return SPEED


def set_searchterm(searchterm):
    global SEARCH_TERM
    SEARCH_TERM = searchterm


def get_searchterm():
    return SEARCH_TERM


def set_running(running):
    global RUNNING
    RUNNING = running


def get_running():
    return RUNNING


def set_window(window):
    global WINDOW
    WINDOW = window


def get_window():
    return WINDOW


def set_thread(thread):
    global THREAD
    THREAD = thread


def get_thread():
    return THREAD


def set_email(email):
    global EMAIL
    if (len(email) < 2):
        return
    EMAIL = email


def get_email():
    return EMAIL


def set_password(password):
    global PASSWORD
    if (len(password) < 2):
        return
    PASSWORD = password


def get_password():
    return PASSWORD
