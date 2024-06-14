import { RequestsTableDropdown } from '#components';
import type { ColumnDef } from '@tanstack/vue-table';
import { DateFormatter } from '@internationalized/date';
import { h } from 'vue';
import type { Employee, Passenger, RequestApi } from '~/types';

export const columns: ColumnDef<RequestApi>[] = [
  {
    accessorKey: 'id',
    header: () => h('div', { class: 'text-left' }, 'ID'),
  },
  {
    accessorKey: 'date',
    header: () => h('div', { class: 'text-left' }, 'Дата'),
    cell: ({ row }) => {
      const date = row.getValue<string>('date');
      const formatDate = new DateFormatter('ru-Ru', {
        dateStyle: 'short',
      }).format(new Date(date));

      return formatDate;
    },
  },
  {
    accessorKey: 'time_start',
    header: () => h('div', { class: 'text-left' }, 'Время начала'),
    cell: ({ row }) => {
      const time = row.getValue<string>('time_start');
      const shortTime = time.split(':');

      return `${shortTime[0]}:${shortTime[1]}`;
    },
  },
  {
    accessorKey: 'time_end',
    header: () => h('div', { class: 'text-left' }, 'Время окончания'),
    cell: ({ row }) => {
      const time = row.getValue<string>('time_end');
      const shortTime = time.split(':');

      return `${shortTime[0]}:${shortTime[1]}`;
    },
  },
  {
    accessorKey: 'from_station',
    header: () => h('div', { class: 'text-left' }, 'От'),
  },
  {
    accessorKey: 'to_station',
    header: () => h('div', { class: 'text-left' }, 'До'),
  },
  {
    accessorKey: 'passenger',
    header: () => h('div', { class: 'text-left' }, 'ФИО пассажира'),
    cell: ({ row }) => {
      const passenger = row.getValue<Passenger>('passenger');
      return `${passenger.second_name} ${passenger.first_name} ${passenger.patronymic}`;
    },
  },
  {
    accessorKey: 'category',
    header: () => h('div', { class: 'text-left' }, 'Категория'),
  },
  {
    accessorKey: 'is_pacemaker',
    header: () => h('div', { class: 'text-left' }, 'ЭКС'),
    cell: ({ row }) => {
      const passenger = row.getValue<Passenger>('passenger');

      return passenger.is_pacemaker ? 'Да' : 'Нет';
    },
  },
  {
    accessorKey: 'employee',
    header: () => h('div', { class: 'text-left' }, 'Сотрудники'),
    cell: ({ row }) => {
      const employee = row.getValue<Employee>('employee');

      if (employee) {
        return employee.full_name;
      }

      return 'Не назначен';
    },
  },
  {
    accessorKey: 'status',
    header: () => h('div', { class: 'text-left' }, 'Статус'),
    cell: ({ row }) => {
      const status = row.getValue<string>('status');
      const colors = ['text-blue-400', 'text-green-600', 'text-red-600', ''];
      let indx: number = 0;

      switch (true) {
        case status === 'Новая':
          indx = 0;
          return h('span', { class: colors[indx] }, status);
        case status === 'Принята':
          indx = 1;
          return h('span', { class: colors[indx] }, status);
        case status === 'Отмена':
          indx = 2;
          return h('span', { class: colors[indx] }, status);
        default:
          indx = 3;
          return h('span', { class: colors[indx] }, status);
      }
    },
  },
  {
    id: 'actions',
    header: () => h('div', { class: 'text-left' }, 'Действия'),
    cell: ({ row }) => {
      const request = row.original;

      return h('div', { class: 'relative flex' }, h(RequestsTableDropdown, { request }));
    },
  },
];
