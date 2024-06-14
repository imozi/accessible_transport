import { EmployeeTableDropdown } from '#components';
import type { ColumnDef } from '@tanstack/vue-table';
import { DateFormatter } from '@internationalized/date';
import { h } from 'vue';
import type { Employee } from '~/types';

export const columns: ColumnDef<Employee>[] = [
  {
    accessorKey: 'id',
    header: () => h('div', { class: 'text-left' }, 'ID'),
  },
  {
    accessorKey: 'gender',
    header: () => h('div', { class: 'text-left' }, 'Пол'),
    cell: ({ row }) => {
      const gender = row.getValue<string>('gender');
      const color = gender == 'male' ? 'text-blue-400' : 'text-red-400';

      return h('span', { class: color }, gender === 'male' ? 'М' : 'Ж');
    },
  },
  {
    accessorKey: 'second_name',
    header: () => h('div', { class: 'text-left' }, 'Фамилия'),
  },
  {
    accessorKey: 'first_name',
    header: () => h('div', { class: 'text-left' }, 'Имя'),
  },
  {
    accessorKey: 'patronymic',
    header: () => h('div', { class: 'text-left' }, 'Отчество'),
  },
  {
    accessorKey: 'personnel_number',
    header: () => h('div', { class: 'text-left' }, 'Табельный номер'),
  },
  {
    accessorKey: 'phone',
    header: () => h('div', { class: 'text-left' }, 'Телефон'),
  },
  {
    accessorKey: 'work_day',
    header: () => h('div', { class: 'text-left' }, 'День работы'),
    cell: ({ row }) => {
      const date = row.getValue<string>('work_day');
      const formatDate = new DateFormatter('ru-Ru', {
        dateStyle: 'short',
      }).format(new Date(date));

      return formatDate;
    },
  },
  {
    accessorKey: 'work_time',
    header: () => h('div', { class: 'text-left' }, 'Время работы'),
  },
  {
    id: 'actions',
    header: () => h('div', { class: 'text-left' }, 'Действия'),
    cell: ({ row }) => {
      const employee = row.original;

      return h('div', { class: 'relative flex' }, h(EmployeeTableDropdown, { employee }));
    },
  },
];
