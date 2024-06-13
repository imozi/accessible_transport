import json
import random
from datetime import datetime, timedelta


def generate_requests_json(hourly_requests, date):
    data = []

    for hour, num_requests in hourly_requests.items():
        start_time = datetime.strptime(f"{hour}:00:00", '%H:%M:%S')
        # end_time = start_time + timedelta(hours=1)

        for pk in range(len(data) + 1, len(data) + num_requests + 1):
            passenger_id = random.randint(1, 300)
            category = random.randint(1, 10)
            status = 1
            # description = None
            from_station = random.randint(1, 420)

            # Ensure to_station is different from from_station
            to_station = random.randint(1, 420)
            while to_station == from_station:
                to_station = random.randint(1, 420)

            # Generate random time within the hour
            time_start = start_time + timedelta(minutes=random.randint(0, 59))
            random_time_delta = timedelta(minutes=random.randint(15, 90))
            time_end = (time_start + random_time_delta).strftime('%H:%M:%S')

            request = {
                "model": "requests.request",
                "pk": pk,
                "fields": {
                    "passenger": passenger_id,
                    "category": category,
                    "status": status,
                    "description": None,
                    "from_station": from_station,
                    "to_station": to_station,
                    "date": date,
                    "time_start": time_start.strftime('%H:%M:%S'),
                    "time_end": time_end,
                    "employee": None
                }
            }
            data.append(request)

    with open('backend/requests_gen.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# Example usage:
hourly_requests = {
    6: 15,
    7: 23,
    8: 23,
    9: 24,
    10: 19,
    11: 16,
    12: 18,
    13: 16,
    14: 24,
    15: 29,
    16: 24,
    17: 18,
    18: 18,
    19: 8,
    20: 20,
    21: 6,
    22: 3,
    23: 2,
    00: 1,
    # Add more hours and the number of requests needed
}
generate_requests_json(hourly_requests, "2024-06-12")
