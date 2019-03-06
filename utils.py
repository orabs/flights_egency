import datetime


def is_available_date(reserved_date, required_date):
    dformat_reserved_date = (datetime.datetime.strptime(reserved_date[0], "%d-%m-%Y"),datetime.datetime.strptime(reserved_date[1], "%d-%m-%Y"))
    dformat_required_date = (datetime.datetime.strptime(required_date[0], "%d-%m-%Y"),datetime.datetime.strptime(required_date[1], "%d-%m-%Y"))
    if dformat_required_date[0] > dformat_reserved_date[1] or dformat_required_date[1] < dformat_reserved_date[0]:
        return True
    return False
