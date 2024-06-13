import { PassengerTableDropdown, UiCheckbox } from '#components';
import type { ColumnDef } from '@tanstack/vue-table';
import { h } from 'vue';
import { categories } from '~/data';
import type { Passenger } from '~/types';

const selected = useSelectedRow();

export const columns: ColumnDef<Passenger>[] = [
  {
    id: 'select',
    enableHiding: false,
    cell: ({ row }) =>
      h(UiCheckbox, {
        checked: row.getIsSelected(),
        disabled: selected.value.select && !row.getIsSelected(),
        'onUpdate:checked': (value: boolean) => {
          return row.toggleSelected(!!value);
        },
        ariaLabel: 'Выбранно строк',
      }),
  },
  {
    accessorKey: 'id',
    header: () => h('div', { class: 'text-left' }, 'ID'),
  },
  {
    accessorKey: 'gender',
    header: () => h('div', { class: 'text-left' }, 'Пол'),
    cell: ({ row }) => {
      const gender = row.getValue<string>('gender');
      const color = gender == 'mele' ? 'text-blue-400' : 'text-red-400';

      return h('span', { class: color }, gender === 'mele' ? 'М' : 'Ж');
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
    accessorKey: 'category',
    header: () => h('div', { class: 'text-left' }, 'Категория'),
    cell: ({ row }) => {
      const category = row.getValue<string>('category');
      const { code } = categories.find((e) => e.id === +category)!;

      return code;
    },
  },
  {
    accessorKey: 'is_pacemaker',
    header: () => h('div', { class: 'text-left' }, 'ЭКС'),
    cell: ({ row }) => {
      const is_pacemaker = row.getValue<string>('is_pacemaker');

      return is_pacemaker ? 'Да' : 'Нет';
    },
  },
  {
    accessorKey: 'phone',
    header: () => h('div', { class: 'text-left' }, 'Телефон'),
  },
  {
    id: 'actions',
    header: () => h('div', { class: 'text-left' }, 'Действия'),
    cell: ({ row }) => {
      const passenger = row.original;

      return h('div', { class: 'relative flex' }, h(PassengerTableDropdown, { passenger }));
    },
  },
];
