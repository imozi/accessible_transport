import type { Categories } from '~/types';

type MetroState = {
  categories: globalThis.Ref<Categories[]>;
  fetch: (url: string) => void;
  getStationId: (name: number) => Categories | undefined;
};

export const useStateCategories = (): MetroState => {
  const categories = useState<Categories[]>('categories');

  const fetch = async (url: string) => {
    await callOnce(async () => {
      categories.value = await $fetch<Categories[]>(url);
    });
  };

  const getStationId = (id: number) => {
    return categories.value.find((category) => category.id === id);
  };

  return {
    categories,
    fetch,
    getStationId,
  };
};
