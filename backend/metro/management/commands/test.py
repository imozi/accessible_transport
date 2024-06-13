from django.core.management import BaseCommand

from employee.models import Employee
from metro.shortest_path import get_shortest_path
from requests.models import Request, RequestStatus


class Command(BaseCommand):
    def handle(self, *args, **options):

        from datetime import datetime, timedelta
        import random

        schedules = Employee.objects.all()
        requests = Request.objects.all()

        def time_to_datetime(time_str):
            return datetime.strptime(time_str, '%H:%M').time() if isinstance(time_str, str) else time_str

        def add_minutes_to_time(time_obj, minutes):
            return (datetime.combine(datetime.today(), time_obj) + timedelta(minutes=minutes)).time()

        def is_within_schedule(start_time, end_time, day, schedule_start, schedule_end, schedule_day):
            if schedule_start < schedule_end:
                return (schedule_start <= start_time < schedule_end and
                        schedule_start < end_time <= schedule_end and
                        day == schedule_day)
            else:
                next_day = day + timedelta(days=1)  # Следующий день
                return ((schedule_start <= start_time or start_time < schedule_end) and
                        (schedule_start < end_time or end_time <= schedule_end) and
                        (day == schedule_day or next_day == schedule_day))

        def time_with_timedelta(time, delta):
            return (datetime.combine(datetime.today(), time) + delta).time()

        # Распределение сотрудников и их перерывов на обед
        distribution = {employee: [] for employee in schedules}
        lunch_breaks = {}

        for employee in schedules:
            work_times = employee.work_time.split('-')
            schedule_start = time_to_datetime(work_times[0])
            schedule_end = time_to_datetime(work_times[1])

            # Преобразование времени в datetime
            today = datetime.today()
            schedule_start_dt = datetime.combine(today, schedule_start)
            if schedule_start < schedule_end:
                schedule_end_dt = datetime.combine(today, schedule_end)
            else:
                schedule_end_dt = datetime.combine(today + timedelta(days=1), schedule_end)

            # Рассчитать возможное время начала обеда
            min_lunch_start_dt = schedule_start_dt + timedelta(minutes=210)  # 3.5 часа = 210 минут
            max_lunch_end_dt = schedule_end_dt - timedelta(minutes=60)  # 1 час до конца рабочего дня

            # Генерируем случайное время начала обеда
            if min_lunch_start_dt < max_lunch_end_dt:
                lunch_start_dt = min_lunch_start_dt + (max_lunch_end_dt - min_lunch_start_dt) * random.random()
                lunch_end_dt = lunch_start_dt + timedelta(minutes=60)  # Перерыв на обед длится 1 час
                lunch_start = lunch_start_dt.time()
                lunch_end = lunch_end_dt.time()
                lunch_breaks[employee] = (lunch_start, lunch_end)
                # Добавляем обед в список заявок
                distribution[employee].append({
                    'id': 'Обед',
                    'date': employee.work_day,
                    'time_start': lunch_start,
                    'time_end': lunch_end
                })

        unassigned_requests = []

        for request in requests:
            request_start = request.time_start
            request_end = request.time_end
            request_date = request.date

            available_employees = []
            for employee in schedules:
                work_times = employee.work_time.split('-')
                schedule_start = time_to_datetime(work_times[0])
                schedule_end = time_to_datetime(work_times[1])
                work_day = employee.work_day

                if is_within_schedule(request_start, request_end, request_date, schedule_start, schedule_end, work_day):
                    lunch_start, lunch_end = lunch_breaks.get(employee, (None, None))

                    # Проверка на пересечение с обеденным перерывом
                    if lunch_start and not (
                            lunch_start <= request_start < lunch_end or lunch_start < request_end <= lunch_end):
                        if all(time_with_timedelta(r['time_end'], timedelta(
                                minutes=7)) <= request_start or request_end <= time_with_timedelta(r['time_start'],
                                                                                                    timedelta(
                                                                                                            minutes=-7))
                               for r in distribution[employee]):
                            available_employees.append(employee)

            if available_employees:
                available_employees = sorted(available_employees, key=lambda e: len(distribution[e]))
                employee = available_employees[0]
                distribution[employee].append({
                    'id': request.id,
                    'date': request_date,
                    'time_start': request_start,
                    'time_end': request_end
                })
                # request.employee = employee  # Назначение сотрудника
                # request.status = RequestStatus.objects.get(pk=2)
                # request.save()  # Сохранение изменений в базе данных
            else:
                unassigned_requests.append(request)

        for employee, assigned_requests in distribution.items():
            assigned_requests_sorted = sorted(assigned_requests, key=lambda r: r['time_start'])
            print(
                f"\n{employee} (дата работы: {employee.work_day}, рабочее время: {employee.work_time})"
            )
            for request in assigned_requests_sorted:
                if request['id'] == 'Обед':
                    start_time_str = request['time_start'].strftime('%H:%M')
                    end_time_str = request['time_end'].strftime('%H:%M')
                    # print(f"  Обед с {start_time_str} до {end_time_str}")
                else:
                    print(
                        f"  Заявка ID {request['id']}, дата {request['date']} с {request['time_start']} до {request['time_end']}"
                    )

        print(f"\nНе распределено: {len(unassigned_requests)} заявка")
        for request in unassigned_requests:
            print(
                f"  Заявка ID {request.id}, дата {request.date} с {request.time_start} до {request.time_end}"
            )
