import type { Employee } from '~/types';

type EmployeeState = {
  removeUser: () => void;
  getUser: () => Employee | boolean;
  setUser: (user: Employee | {}) => void;
};

export const useStateEmployee = (): EmployeeState => {
  const getUser = (): Employee | boolean => {
    const user = localStorage.getItem('user');
    if (user) {
      return JSON.parse(user) as Employee;
    }
    return false;
  };

  const setUser = (user: Employee | {}) => {
    localStorage.setItem('user', JSON.stringify(user));
  };

  const removeUser = () => {
    localStorage.removeItem('user');
  };

  return {
    removeUser,
    getUser,
    setUser,
  };
};
