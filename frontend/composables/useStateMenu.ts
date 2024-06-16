export const useStateMenu = () =>
  useState('menu', () => {
    return [
      {
        id: 1,
        name: 'Заявки',
        icon: 'material-symbols:list-alt-outline',
        link: '/requests',
      },
      {
        id: 2,
        name: 'Расписание',
        icon: 'uil:calendar-alt',
        link: '/schedule',
      },
      {
        id: 3,
        name: 'Сотрудники',
        icon: 'ic:outline-business-center',
        link: '/employees',
      },
      {
        id: 4,
        name: 'Пассажиры',
        icon: 'eva:people-outline',
        link: '/passengers',
      },
      {
        id: 5,
        name: 'Аналитика',
        icon: 'grommet-icons:analytics',
        link: '/analytics',
      },
    ];
  });
