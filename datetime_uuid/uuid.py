from datetime import datetime
from random import randint
from uuid import uuid4


def get_uuid(use_date_stamp=True):
    if not use_date_stamp:
        return str(uuid4())
    date_string = datetime.strftime(datetime.utcnow(), '%Y%m%d-%H%M-%S%f')
    # 281474976710655 = 2**(4*12) - 1
    uuid_string = '{0}-{1}-{2:012x}'.format(
        date_string[:18], date_string[18:], randint(0, 281474976710655))
    return uuid_string
