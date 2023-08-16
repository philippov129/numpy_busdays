'''
Is simple example demonstrate 
how numpy library worked with date 
and define buisness days
now 2018-08-16 use only numpy.is_busday 
'''

import numpy as np
from  datetime import date


# Get data for numpy use datetime or manual enter
def get_date():
    manual_enter_date = input("Enter Date (YYYY/MM/DD):")
    if not manual_enter_date:
       date_is_now  = date.today()
    else:
        date_is_now = manual_enter_date   
    return date_is_now


# Numpy library search is busday or not
def busday_searcher():
    today_date = get_date()
    is_busday = np.is_busday(today_date)

    if is_busday:
        return f"Date:{today_date} is busday :("
    else:
        return f"Date:{today_date} is weekend :)"    


# Output result is define buisness day
print(busday_searcher())