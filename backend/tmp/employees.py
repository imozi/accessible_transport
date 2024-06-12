import random


def create_employees(num_employees):
    schedules = [
        {"start": "7:00", "end": "19:00"},
        {"start": "8:00", "end": "20:00"},
        {"start": "10:00", "end": "22:00"},
        {"start": "20:00", "end": "8:00"},
    ]

    employees = {}

    for i in range(num_employees):
        selected_schedule = random.choice(schedules)

        employee = (selected_schedule['start'], selected_schedule['end'])
        employees[f"E-{i + 1}"] = employee

    return employees


print(create_employees(5))