export interface Passenger {
  id: number;
  first_name: string;
  second_name: string;
  patronymic: string;
  category: string;
  gender: string;
  description: string | null;
  is_pacemaker: boolean;
}
