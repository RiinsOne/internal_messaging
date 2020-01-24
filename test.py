from datetime import datetime
# 2020-1-22 00:01
# 2020-01-01 00:01

# 01.01.2020 00:01

def dt_formatter(local_dt):
    local_dt.strip()
    temp_dt = local_dt.split()  # ['01.01.2020', '22:01']
    date_part = ''.join(temp_dt[0:1])  # '01.01.2020'
    time_part = ''.join(temp_dt[1:2])  # '22:01'

    divider_date_char = date_part[2]
    splitted_date_part = date_part.split(divider_date_char)

    day = splitted_date_part[0:1]
    month = splitted_date_part[1:2]
    year = splitted_date_part[2:3]
    dj_date = '-'.join(year+month+day)
    if time_part:
        return(f'{dj_date} {time_part}')
    return dj_date



# 22.01.2020 00:01
# 23.01.2020 23:59

# def dt_to_second(local_dt):
#     local_dt.strip()
#     temp_dt = local_dt.split()
#     date_part = ''.join(temp_dt[0:1])
#     time_part = ''.join(temp_dt[1:2])

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

# q_start = '22.01.2020 00:01'
# q_end = '24.01.2020 00:01'
# print(q_delta(q_start, q_end))

# epoch = datetime.utcfromtimestamp(0)
# dt_start = datetime.strptime(q_start, '%d.%m.%Y %H:%M')
# dt_end = datetime.strptime(q_end, '%d.%m.%Y %H:%M')
# print(dt_start, dt_end)
#
# dt_start_s = (dt_start - epoch).total_seconds()
# dt_end_s = (dt_end - epoch).total_seconds()
# print(dt_start_s, dt_end_s)
#
# q_delta = dt_end_s - dt_start_s
# verify_delta = 172800.0
# print(q_delta)
# print(verify_delta)
#
# if q_delta > verify_delta:
#     print('Change date range period!')
# else:
#     print(verify_delta - q_delta)


text1 = '10230193 19301.1231/123.131/231'
text2 = 'asm m102i301 2k3 ,31231313'
print(text1.upper().isupper())
print(text2.upper().isupper())
