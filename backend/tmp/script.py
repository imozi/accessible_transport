from datetime import datetime, timedelta
from employees import create_employees
from request import create_requests

schedules = create_employees(2)

requests = create_requests(4)


def time_to_datetime(time_str):
    return datetime.strptime(time_str, '%H:%M')


def is_within_schedule(start_time, end_time, schedule_start, schedule_end):
    if schedule_start < schedule_end:
        return schedule_start <= start_time < schedule_end and schedule_start < end_time <= schedule_end
    else:
        return (schedule_start <= start_time or start_time < schedule_end or schedule_start <= end_time
                or end_time <= schedule_end)


distribution = {key: [] for key in schedules}
unassigned_requests = []

for request in requests:
    request_start = time_to_datetime(request['start'])
    request_end = time_to_datetime(request['end'])

    available_employees = []
    for employee, (schedule_start, schedule_end) in schedules.items():
        schedule_start = time_to_datetime(schedule_start)
        schedule_end = time_to_datetime(schedule_end)

        if is_within_schedule(request_start, request_end, schedule_start, schedule_end):
            available_employees.append(employee)

    if available_employees:
        available_employees = [
            e for e in available_employees
            if
            not distribution[e] or time_to_datetime(distribution[e][-1]['end']) + timedelta(minutes=15) <= request_start
        ]

        if available_employees:
            employee = min(available_employees, key=lambda e: len(distribution[e]))
            distribution[employee].append(request)
        else:
            unassigned_requests.append(request)
    else:
        unassigned_requests.append(request)

for employee, tasks in distribution.items():
    schedule_start, schedule_end = schedules[employee]
    print(f"{employee} (рабочее время: {schedule_start} - {schedule_end}): {len(tasks)} задач")
    for task in tasks:
        print(f"  Заявка ID {task['id']} с {task['start']} до {task['end']} - время выполнения {task['time_over']}")

print(f"\nНе распределено: {len(unassigned_requests)} задач")
for task in unassigned_requests:
    print(f"  Заявка ID {task['id']} с {task['start']} до {task['end']}")
