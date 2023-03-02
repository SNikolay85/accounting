from datetime import datetime as dt
from passwordPy import create

from application.salary import calculate_salary
from application.db import people as p

def current_date_time():
    print('Current date and time:', dt.now())

if __name__ == '__main__':
    calculate_salary()
    p.get_employees()
    current_date_time()

    password = create(chars=True, length=10, counts=1)
    print(password)