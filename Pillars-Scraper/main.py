from inspect import getcomments
from pillars_data import *
from pillars_main import *
from pcompany import *


def run_program():
    # set_companies(load_companys())

    intc = scrape_company("intc")
    # intc = get_companies()[0]
    intcdata = intc.get_data()

    show(intcdata[0])
    show(intcdata[1])
    show(intcdata[2])

    pass


run_program()
