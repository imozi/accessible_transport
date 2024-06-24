export interface Passenger {
  id: number;
  first_name: string;
  second_name: string;
  patronymic: string;
  phone: string;
  category: number;
  gender: string;
  description: string | null;
  is_pacemaker: boolean;
}

export interface Employee {
  id: number;
  first_name: string;
  second_name: string;
  patronymic: string;
  full_name: string;
  gender: string;
  phone: string;
  personnel_number: number;
  work_time: string;
  work_day: string;
}

export interface RequestApi {
  id: number;
  passenger: Passenger;
  category: string;
  status: string;
  from_station: string;
  to_station: string;
  employee: Employee[] | null;
  employees_number: number;
  description: null;
  date: Date;
  time_start: string;
  time_end: string;
}

export interface RequestStatus {
  id: number;
  status: string;
}

export interface Categories {
  id: number;
  code: string;
  description: string;
}

export type ModalProps = {
  props: {
    textTrigger: string;
    title: string;
    description?: string;
    icon?: string;
    isDisable?: boolean;
    variant?: 'default' | 'outline';
  };
};

export interface StationPath {
  from_station: Station;
  to_station: Station;
  path: string[];
  transfers: Transfer[];
  route_time: number;
  time_start: string;
  time_end: string;
}

export interface Station {
  id_station: string;
  name_station: string;
}

export interface Transfer {
  station_from: string;
  station_to: string;
  time: number;
}

export interface Analytics {
  id: number;
  full_name: string;
  work_time: string;
  work_day: string;
  lunch_start: string;
  lunch_end: string;
  requests: AnalyticsRequest[];
}

export interface AnalyticsRequest {
  id: number;
  date: string;
  time_start: string;
  time_end: string;
}
