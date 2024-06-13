import random
import datetime


def time_generate():
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)

    if 0 < hours < 5 or (hours == 0 and minutes > 30) or (hours == 5 and minutes < 30):
        return time_generate()

    return f'{hours:02d}:{minutes:02d}'


def create_requests(num_requests):
    requests = []
    count = 0

    while count != num_requests:
        time = time_generate()
        dt = datetime.datetime.strptime(time, "%H:%M")
        end_time = (dt + datetime.timedelta(minutes=random.randint(30, 90)))
        requests.append(
            {"id": count + 1, "start": time, "end": f'{end_time.strftime("%H:%M")}', "time_over": f'{end_time - dt}'})
        count += 1
    requests.sort(key=lambda x: datetime.datetime.strptime(x['start'], '%H:%M').time())
    return requests


#
#
requests = create_requests(50)
for i in requests:
    print(i)
