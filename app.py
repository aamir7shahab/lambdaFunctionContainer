import datetime
import dateutil
from datetime import datetime
from datetime import timedelta
import locale
import pytz

# eastern = dateutil.tz.gettz('US/Eastern')


def lambda_handler(event, context):
    # connect_date = event["Details"]["ContactData"]["Attributes"]["eligible_weeks_next_cwe"]
    connect_date = event["Details"]["Parameters"]["cwe"]
    date1 = datetime.strptime(connect_date, "%Y%m%d")
    week = date1.strftime("%a")
    # lang = event["Details"]["ContactData"]["Attributes"]["lang"]
    lang = event["Details"]["Parameters"]["lang"]

    if week == "Sun":
        _frm_date = from_date(lang, 0, connect_date)
        _to_date = To_date(lang, 6, connect_date)
    elif week == "Mon":
        _frm_date = from_date(lang, 1, connect_date)
        _to_date = To_date(lang, 5, connect_date)
    elif week == "Tue":
        _frm_date = from_date(lang, 2, connect_date)
        _to_date = To_date(lang, 4, connect_date)
    elif week == "Wed":
        _frm_date = from_date(lang, 3, connect_date)
        _to_date = To_date(lang, 3, connect_date)
    elif week == "Thu":
        _frm_date = from_date(lang, 4, connect_date)
        _to_date = To_date(lang, 2, connect_date)
    elif week == "Fri":
        _frm_date = from_date(lang, 5, connect_date)
        _to_date = To_date(lang, 1, connect_date)
    elif week == "Sat":
        _frm_date = from_date(lang, 6, connect_date)
        _to_date = To_date(lang, 0, connect_date)
    else:
        print("no date")

    print({"From_Date": _frm_date, "To_Date": _to_date})
    return {"From_Date": _frm_date, "To_Date": _to_date}


def from_date(lang, dt, connect_date):
    if lang == "es":
        locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
        newdate = getdate(connect_date)
        _from_date = (newdate - timedelta(days=dt)).strftime("%B %d")
        return _from_date
    elif lang == "en":
        locale.setlocale(locale.LC_TIME, "en_US.UTF-8")
        newdate = getdate(connect_date)
        _from_date = (newdate - timedelta(days=dt)).strftime("%B %d")
        return _from_date
    else:
        print("no date")


def To_date(lang, dt, connect_date):
    if lang == "es":
        locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
        newdate = getdate(connect_date)
        _to_date = (newdate + timedelta(days=dt)).strftime("%B %d")
        locale.setlocale(locale.LC_ALL, "")
        return _to_date
    elif lang == "en":
        locale.setlocale(locale.LC_TIME, "en_US.UTF-8")
        locale.setlocale(locale.LC_ALL, "")
        newdate = getdate(connect_date)
        _to_date = (newdate + timedelta(days=dt)).strftime("%B %d")
        return _to_date
    else:
        print("no date")


def getdate(inputdate):
    date1 = datetime.strptime(inputdate, "%Y%m%d")
    local = pytz.timezone("EST")
    local_dt = local.localize(date1, is_dst=None)
    return local_dt
