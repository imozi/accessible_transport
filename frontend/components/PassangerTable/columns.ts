import { RequestsTableDropdown } from "#components";
import type { ColumnDef } from "@tanstack/vue-table";
import { h } from "vue";

interface Request {
  id: number;
  passenger: string;
  category: string;
  status: string;
  from_station: string;
  to_station: string;
  employee: string;
  description: string | null;
  date: string;
  time_start: string;
  time_end: string;
}

export const requests: Request[] = [
  {
    id: 7,
    passenger: "Савина Полина Дмитриевна",
    category: "ОВ",
    status: "Не подтверждена",
    from_station: "Бульвар Рокоссовского",
    to_station: "Красносельская",
    employee: "НьюЙорк С. В.",
    description: "новая заявка",
    date: "2024-06-10",
    time_start: "15:15:00",
    time_end: "15:36:00",
  },
  {
    id: 8,
    passenger: "Логинов Борис Борисович",
    category: "ИС",
    status: "Не подтверждена",
    from_station: "Черкизовская",
    to_station: "Преображенская площадь",
    employee: "Фридман М. А.",
    description: null,
    date: "2024-06-10",
    time_start: "01:11:06",
    time_end: "15:36:00",
  },
  {
    id: 1,
    passenger: "Жукова Ксения Олеговна",
    category: "РДК",
    status: "В рассмотрении",
    from_station: "Бульвар Рокоссовского",
    to_station: "Спортивная",
    employee: "Фридман М. А.",
    description: null,
    date: "2024-06-09",
    time_start: "09:40:00",
    time_end: "10:23:00",
  },
  {
    id: 2,
    passenger: "Осипов Игорь Сергеевич",
    category: "ПЛ",
    status: "Принята",
    from_station: "Водный стадион",
    to_station: "Преображенская площадь",
    employee: "Фридман М. А.",
    description: "новая заявка",
    date: "2024-06-09",
    time_start: "11:40:00",
    time_end: "12:44:00",
  },
  {
    id: 6,
    passenger: "Королев Филипп Анатольевич",
    category: "ИС",
    status: "Не подтверждена",
    from_station: "Сокольники",
    to_station: "Черкизовская",
    employee: "Фридман М. А.",
    description: "update",
    date: "2024-06-09",
    time_start: "13:00:00",
    time_end: "13:12:00",
  },
  {
    id: 3,
    passenger: "Логинов Борис Борисович",
    category: "ИС",
    status: "В рассмотрении",
    from_station: "Кантемировская",
    to_station: "Мякинино",
    employee: "НьюЙорк С. В.",
    description: "заявка",
    date: "2024-06-09",
    time_start: "11:40:00",
    time_end: "13:02:00",
  },
];

export const columns: ColumnDef<Request>[] = [
  {
    accessorKey: "id",
    header: () => h("div", { class: "text-left" }, "ID"),
  },
  {
    accessorKey: "time_start",
    header: () => h("div", { class: "text-left" }, "Время начала"),
    cell: ({ row }) => {
      const time = row.getValue<string>("time_start");
      const shortTime = time.split(":");

      return `${shortTime[0]}:${shortTime[1]}`;
    },
  },
  {
    accessorKey: "time_end",
    header: () => h("div", { class: "text-left" }, "Время окончания"),
    cell: ({ row }) => {
      const time = row.getValue<string>("time_start");
      const shortTime = time.split(":");

      return `${shortTime[0]}:${shortTime[1]}`;
    },
  },
  {
    accessorKey: "from_station",
    header: () => h("div", { class: "text-left" }, "От"),
  },
  {
    accessorKey: "to_station",
    header: () => h("div", { class: "text-left" }, "До"),
  },
  {
    accessorKey: "passenger",
    header: () => h("div", { class: "text-left" }, "ФИО пассажира"),
  },
  {
    accessorKey: "category",
    header: () => h("div", { class: "text-left" }, "Категория"),
  },
  {
    accessorKey: "employee",
    header: () => h("div", { class: "text-left" }, "Сотрудники"),
  },
  {
    accessorKey: "status",
    header: () => h("div", { class: "text-left" }, "Статус"),
    cell: ({ row }) => {
      const status = row.getValue<string>("status");
      const colors = ["text-blue-400", "text-green-600", "text-red-600"];
      let indx: number = 0;

      switch (true) {
        case status === "Принята":
          indx = 1;
      }

      return h("span", { class: colors[indx] }, status);
    },
  },
  {
    id: "actions",
    enableHiding: false,
    cell: ({ row }) => {
      const request = row.original;

      return h(
        "div",
        { class: "relative flex" },
        h(RequestsTableDropdown, { request })
      );
    },
  },
];
