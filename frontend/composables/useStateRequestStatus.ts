import type { RequestStatus } from '~/types';

type RequestStatusState = {
  requestStatus: globalThis.Ref<RequestStatus[]>;
  fetch: (url: string) => void;
  getStatusId: (id: number) => RequestStatus | undefined;
  getStatusName: (name: string) => RequestStatus | undefined;
};

export const useStateRequestStatus = (): RequestStatusState => {
  const requestStatus = useState<RequestStatus[]>('status');

  const fetch = async (url: string) => {
    await callOnce(async () => {
      requestStatus.value = await $fetch<RequestStatus[]>(url);
    });
  };

  const getStatusId = (id: number) => {
    return requestStatus.value.find((status) => status.id === id);
  };

  const getStatusName = (name: string) => {
    return requestStatus.value.find((status) => status.status === name);
  };

  return {
    requestStatus,
    fetch,
    getStatusId,
    getStatusName
  };
};
