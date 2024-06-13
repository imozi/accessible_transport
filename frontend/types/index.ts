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


export type ModalProps = {
  props: {
    textTrigger: string;
    title: string;
    description?: string;
    icon?: string;
    isDisable?: boolean;
    variant?: 'default' | 'outline'
  };
};
