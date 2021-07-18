from poshmark import  *

RUNNING = False
SEARCH_TERM = "!"
SPEED = 0
FOLLOW_COUNT = 0
FOLLOWED = []
WINDOW = None


# USER HAS CLICKED START / STOP
def clicked_start(window):
    global RUNNING
    global SEARCH_TERM
    global SPEED
    global WINDOW

    WINDOW = window

    # If already running
    if (RUNNING):
        WINDOW.pushButton_startstop.setText("Start")
        RUNNING = False
    else:
        search = WINDOW.lineEdit_searchterm.text()
        SPEED = WINDOW.horizontalSlider_speed.value()

        if (len(search) > 0):
            SEARCH_TERM = search
        WINDOW.pushButton_startstop.setText("Stop")
        run_driver()
        begin()
        find_users()
        main_code(SEARCH_TERM, SPEED) # TODO add user picks follow amount
        RUNNING = True

    print(RUNNING, SEARCH_TERM, SPEED, FOLLOW_COUNT, FOLLOWED)


# WHEN THE SLIDER VALUE IS CHANGED
def value_changed(window):
    if (RUNNING):
        window.horizontalSlider_speed.setValue(SPEED)
    window.label_speed.setText(f"{window.horizontalSlider_speed.value()}")


# UPDATE THE FOLLOWED LIST AND COUNTER
def update_followed():
    global FOLLOW_COUNT
    global FOLLOWED

    FOLLOW_COUNT = len(FOLLOWED)
    WINDOW.lcdNumber_followed.display(FOLLOW_COUNT)
    WINDOW.listWidget_followed.clear()
    WINDOW.listWidget_followed.addItems(FOLLOWED)
