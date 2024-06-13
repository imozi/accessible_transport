export const useSelectedRow = () =>
  useState<{ select: boolean }>('pageName', () => {
    return {
      select: false,
    };
  });
