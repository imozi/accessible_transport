export const usePageName = () =>
  useState<{ title: string | undefined }>('pageName', () => {
    return {
      title: undefined,
    };
  });
