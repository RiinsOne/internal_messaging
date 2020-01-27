from datetime import datetime, timedelta
from random import randint, randrange, choice


def dt_formatter(local_dt):
    local_dt.strip()
    temp_dt = local_dt.split()
    date_part = ''.join(temp_dt[0:1])
    time_part = ''.join(temp_dt[1:2])

    divider_date_char = date_part[2]
    splitted_date_part = date_part.split(divider_date_char)

    day = splitted_date_part[0:1]
    month = splitted_date_part[1:2]
    year = splitted_date_part[2:3]
    dj_date = '-'.join(year+month+day)
    if time_part:
        return(f'{dj_date} {time_part}')
    return dj_date


def q_delta(q_start, q_end):
    epoch = datetime.utcfromtimestamp(0)
    verify_delta = 172800.0
    dt_start = datetime.strptime(q_start.strip(), '%d.%m.%Y %H:%M')
    dt_end = datetime.strptime(q_end.strip(), '%d.%m.%Y %H:%M')
    dt_start_s = (dt_start - epoch).total_seconds()
    dt_end_s = (dt_end - epoch).total_seconds()
    delta = dt_end_s - dt_start_s
    if delta > verify_delta:
        return False
    return True


def randtime(start_hour, end_hour):
    result = ''
    r1 = randint(start_hour, end_hour)
    if len(str(r1)) == 1:
        result += '0' + str(r1) + ':'
    else:
        result += str(r1) + ':'

    r2 = randrange(0, 60, 5)
    if len(str(r2)) == 1:
        result += '0' + str(r2)
    else:
        result += str(r2)
    return result


def randdate():
    dates = []
    for i in range(1, 8, 1):
        date = datetime.now() - timedelta(days=i)
        dates.append(date.strftime('%d.%m.%Y'))
    return choice(dates)
