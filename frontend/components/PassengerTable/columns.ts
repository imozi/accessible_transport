import { PassengerTableDropdown, UiCheckbox } from '#components';
import type { ColumnDef } from '@tanstack/vue-table';
import { h } from 'vue';
import type { Passenger } from '~/types';

export const passengers: Passenger[] = [
  {
    id: 1,
    first_name: 'Иван',
    second_name: 'Иванов',
    patronymic: 'Иванович',
    category: 'ИК',
    gender: 'М',
    description: null,
    is_pacemaker: false,
  },

  {
    id: 2,
    first_name: 'Мария',
    second_name: 'Петрова',
    patronymic: 'Сергеевна',
    category: 'ИК',
    gender: 'Ж',
    description: 'Часто летающий пассажир',
    is_pacemaker: false,
  },

  {
    id: 3,
    first_name: 'Анна',
    second_name: 'Сидорова',
    patronymic: 'Александровна',
    category: 'ОВ',
    gender: 'Ж',
    description: 'VIP-пассажир',
    is_pacemaker: true,
  },

  {
    id: 4,
    first_name: 'Петр',
    second_name: 'Борисов',
    patronymic: 'Петрович',
    category: 'ИК',
    gender: 'М',
    description: 'Путешествует с животным',
    is_pacemaker: false,
  },

  {
    id: 5,
    first_name: 'Александр',
    second_name: 'Дубов',
    patronymic: 'Александрович',
    category: 'ИС',
    gender: 'М',
    description: 'Требует помощи при движении на колясике',
    is_pacemaker: false,
  },

  {
    id: 6,
    first_name: 'Елена',
    second_name: 'Тарасова',
    patronymic: 'Евгеньевна',
    category: 'ПЛ',
    gender: 'Ж',
    description: 'Знаменитый пассажир',
    is_pacemaker: false,
  },

  {
    id: 7,
    first_name: 'Ольга',
    second_name: 'Иванова',
    patronymic: 'Петровна',
    category: 'ИК',
    gender: 'Ж',
    description: 'Путешествует с ребенком',
    is_pacemaker: false,
  },

  {
    id: 8,
    first_name: 'Иван',
    second_name: 'Петров',
    patronymic: 'Иванович',
    category: 'ИК',
    gender: 'М',
    description: 'Требует специального питания',
    is_pacemaker: true,
  },

  {
    id: 9,
    first_name: 'Анастасия',
    second_name: 'Сидорова',
    patronymic: 'Александровна',
    category: 'РДК',
    gender: 'Ж',
    description: 'Путешествует с большой группой',
    is_pacemaker: false,
  },

  {
    id: 10,
    first_name: 'Николай',
    second_name: 'Кузнецов',
    patronymic: 'Николаевич',
    category: 'ИК',
    gender: 'М',
    description: 'Испытывает страх перед полетом',
    is_pacemaker: false,
  },
];

export const columns: ColumnDef<Passenger>[] = [
  {
    id: 'select',
    enableHiding: false,
    cell: ({ row }) =>
      h(UiCheckbox, {
        checked: row.getIsSelected(),
        'onUpdate:checked': (value: boolean) => row.toggleSelected(!!value),
        ariaLabel: 'Select row',
      }),
  },
  {
    accessorKey: 'id',
    header: () => h('div', { class: 'text-left' }, 'ID'),
  },
  {
    accessorKey: 'first_name',
    header: () => h('div', { class: 'text-left' }, 'Имя'),
  },
  {
    accessorKey: 'second_name',
    header: () => h('div', { class: 'text-left' }, 'Фамилия'),
  },
  {
    accessorKey: 'patronymic',
    header: () => h('div', { class: 'text-left' }, 'Отчество'),
  },
  {
    accessorKey: 'category',
    header: () => h('div', { class: 'text-left' }, 'Категория'),
  },
  {
    accessorKey: 'gender',
    header: () => h('div', { class: 'text-left' }, 'Пол'),
    cell: ({ row }) => {
      const gender = row.getValue<string>('gender');
      const color = gender == 'М' ? 'text-blue-400' : 'text-red-400';

      return h('span', { class: color }, gender);
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
    id: 'actions',
    header: () => h('div', { class: 'text-left' }, 'Действия'),
    cell: ({ row }) => {
      const passenger = row.original;

      return h('div', { class: 'relative flex' }, h(PassengerTableDropdown, { passenger }));
    },
  },
];
