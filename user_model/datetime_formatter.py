from datetime import datetime

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
    dt_start = datetime.strptime(q_start, '%d.%m.%Y %H:%M')
    dt_end = datetime.strptime(q_end, '%d.%m.%Y %H:%M')
    dt_start_s = (dt_start - epoch).total_seconds()
    dt_end_s = (dt_end - epoch).total_seconds()
    delta = dt_end_s - dt_start_s
    if delta > verify_delta:
        return False
    return True
