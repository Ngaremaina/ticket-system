import apiFetch from './api';

test('apiFetch sends cookies and keeps caller options', async () => {
  global.fetch.mockResolvedValue({ ok: true });

  await apiFetch('/events', { method: 'POST' });

  expect(global.fetch).toHaveBeenCalledWith('/events', {
    credentials: 'include',
    method: 'POST',
  });
});
