import type { Passenger } from "~/types";

export const passengers: Passenger[] = [
  {
    id: 1,
    first_name: 'Иван',
    second_name: 'Иванов',
    patronymic: 'Иванович',
    phone: '9142336605',
    category: 1,
    gender: 'mele',
    description: null,
    is_pacemaker: false,
  },

  {
    id: 2,
    first_name: 'Мария',
    second_name: 'Петрова',
    patronymic: 'Сергеевна',
    phone: '9142336605',
    category: 3,
    gender: 'famele',
    description: 'Часто летающий пассажир',
    is_pacemaker: false,
  },

  {
    id: 3,
    first_name: 'Анна',
    second_name: 'Сидорова',
    patronymic: 'Александровна',
    phone: '9142336605',
    category: 5,
    gender: 'famele',
    description: 'VIP-пассажир',
    is_pacemaker: true,
  },

  {
    id: 4,
    first_name: 'Петр',
    second_name: 'Борисов',
    patronymic: 'Петрович',
    phone: '9142336605',
    category: 2,
    gender: 'mele',
    description: 'Путешествует с животным',
    is_pacemaker: false,
  },

  {
    id: 5,
    first_name: 'Александр',
    second_name: 'Дубов',
    patronymic: 'Александрович',
    phone: '9142336605',
    category: 3,
    gender: 'mele',
    description: 'Требует помощи при движении на колясике',
    is_pacemaker: false,
  },

  {
    id: 6,
    first_name: 'Елена',
    second_name: 'Тарасова',
    patronymic: 'Евгеньевна',
    phone: '9142336605',
    category: 9,
    gender: 'famele',
    description: 'Знаменитый пассажир',
    is_pacemaker: false,
  },

  {
    id: 7,
    first_name: 'Ольга',
    second_name: 'Иванова',
    patronymic: 'Петровна',
    phone: '9142336605',
    category: 7,
    gender: 'famele',
    description: 'Путешествует с ребенком',
    is_pacemaker: false,
  },

  {
    id: 8,
    first_name: 'Иван',
    second_name: 'Петров',
    patronymic: 'Иванович',
    phone: '9142336605',
    category: 4,
    gender: 'mele',
    description: 'Требует специального питания',
    is_pacemaker: true,
  },

  {
    id: 9,
    first_name: 'Анастасия',
    second_name: 'Сидорова',
    patronymic: 'Александровна',
    phone: '9142336605',
    category: 10,
    gender: 'famele',
    description: 'Путешествует с большой группой',
    is_pacemaker: false,
  },

  {
    id: 10,
    first_name: 'Николай',
    second_name: 'Кузнецов',
    patronymic: 'Николаевич',
    phone: '9142336605',
    category: 6,
    gender: 'famele',
    description: 'Испытывает страх перед полетом',
    is_pacemaker: false,
  },
];

export const categories = [
  {
    id: 6,
    code: 'ДИ',
    description: 'Ребенок инвалид (зачастую передвижение в инвалидной коляске)',
  },
  {
    id: 3,
    code: 'ИЗ',
    description: 'Инвалид по зрению с остаточным зрением (слабовидящий,\r\nсопровождение по метрополитену)',
  },
  {
    id: 2,
    code: 'ИЗТ',
    description: 'Инвалид по зрению (тотальный, сопровождение по метрополитену)',
  },
  {
    id: 1,
    code: 'ИК',
    description: 'none',
  },
  {
    id: 5,
    code: 'ИО',
    description: 'Инвалид опорник (необходима поддержка при передвижении\r\nи/или на лестницах/эскалаторах)',
  },
  {
    id: 4,
    code: 'ИС',
    description: 'Инвалид по слуху (в основном помощь в ориентировании)',
  },
  {
    id: 12,
    code: 'ИУ',
    description: 'Люди с ментальной инвалидностью',
  },
  {
    id: 11,
    code: 'ОВ',
    description: 'Временно маломобильные (после операции, переломы и прочее)',
  },
  {
    id: 10,
    code: 'ОГД',
    description: 'Организованные группы детей (сопровождение по метрополитену)',
  },
  {
    id: 7,
    code: 'ПЛ',
    description: 'Пожилой человек (необходима поддержка при передвижении и/или\r\nна лестницах/эскалаторах)',
  },
  {
    id: 8,
    code: 'РД',
    description: 'Родители с детьми (сопровождение ребенка)',
  },
  {
    id: 9,
    code: 'РДК',
    description: 'Родители с детскими колясками (помощь с детской коляской)',
  },
];

export const genders = [
  {
    id: 1,
    name: 'Мужской',
    value: 'mele',
  },
  {
    id: 2,
    name: 'Женский',
    value: 'famele',
  },
];
