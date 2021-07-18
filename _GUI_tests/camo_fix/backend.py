from vardata import set_randomized, set_savelogin
from vardata import get_follow_count, get_followed, get_running, get_searchterm, get_speed, get_thread, get_window, set_email, set_follow_count, set_password, set_running, set_searchterm, set_speed, set_thread, set_window
from poshmark import *
from threading import Thread


# USER HAS CLICKED START / STOP
def clicked_start(window):
    set_window(window)

    # If already running
    if (get_running()):
        set_running(False)
        window.pushButton_startstop.setText("Start")
        # THREAD.join()
    else:
        set_running(True)
        search = window.lineEdit_searchterm.text()
        set_speed(window.doubleSpinBox_speed.value())

        if (len(search) > 0):
            set_searchterm(search)

        window.pushButton_startstop.setText("Stop")
        set_email(window.lineEdit_email.text())
        set_password(window.lineEdit_password.text())
        set_savelogin(window.checkBox_savelogin.isChecked())
        set_randomized(window.checkBox_randomizespeed.isChecked())

        set_thread(Thread(target=run_poshmarkbot))
        get_thread().start()

    print(get_running(), get_searchterm(), get_speed(),
          get_follow_count(), get_followed())


def run_poshmarkbot():
    run_driver()
    login_site()
    find_users()
    # TODO add user picks follow amount
    main_code(get_searchterm(), get_speed(),
              get_window().spinBox_followamount.value())

# UPDATE THE FOLLOWED LIST AND COUNTER


def update_followed():
    set_follow_count(len(get_followed()))
    get_window().lcdNumber_followed.display(get_follow_count())
    get_window().listWidget_followed.clear()
    get_window().listWidget_followed.addItems(get_followed())
