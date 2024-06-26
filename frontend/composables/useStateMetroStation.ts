import type { Station } from '~/types';

type MetroState = {
  stations: globalThis.Ref<Station[]>;
  fetch: (url: string) => void;
  getStationId: (name: string) => Station | undefined;
};

export const useStateMetroStation = (): MetroState => {
  const stations = useState<Station[]>('stations');

  const fetch = async (url: string) => {
    await callOnce(async () => {
      stations.value = await $fetch<Station[]>(url);
    });
  };

  const getStationId = (name: string) => {
    return stations.value.find((station) => station.name_station === name);
  };

  return {
    stations,
    fetch,
    getStationId,
  };
};
