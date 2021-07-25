
from pandasgui import show
from backend import *
from chart_factory import *
from pillars_main import *
from pcompany import *


def run_program():
    set_companies(load_companys())

    #intc = scrape_company("intc")
    intc = get_companies()[0]
    intcdata = intc.get_data()

    chart_bar(intcdata, TOTAL_ASSETS, TOTAL_LIABILITIES)
    chart_line(intcdata, TOTAL_ASSETS, TOTAL_LIABILITIES)
    chart_stackedarea(intcdata, TOTAL_ASSETS, TOTAL_LIABILITIES)

    pass


run_program()
