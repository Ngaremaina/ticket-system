import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { MemoryRouter } from 'react-router-dom';
import App from './App';
import { Authentication } from './components/Authentication';

function renderApp(route = '/') {
  return render(
    <Authentication>
      <MemoryRouter initialEntries={[route]}>
        <App />
      </MemoryRouter>
    </Authentication>
  );
}

function jsonResponse(body, ok = true) {
  return Promise.resolve({ ok, json: () => Promise.resolve(body) });
}

test('shows the login page when not authenticated', () => {
  renderApp('/dashboard');
  expect(screen.getByText(/sign in to tickety/i)).toBeInTheDocument();
});

test('logs in and leaves the login page', async () => {
  global.fetch.mockImplementation((url) =>
    url === '/login'
      ? jsonResponse({ id: 2, email: 'fan@example.com', role: 'client' })
      : jsonResponse([])
  );

  renderApp('/');
  await userEvent.type(screen.getByLabelText(/your email/i), 'fan@example.com');
  await userEvent.type(screen.getByLabelText(/your password/i), 'secret123');
  await userEvent.click(screen.getByLabelText(/remember this device/i));
  await userEvent.click(screen.getByRole('button', { name: /login to your account/i }));

  await waitFor(() => expect(screen.queryByText(/sign in to tickety/i)).not.toBeInTheDocument());
  expect(JSON.parse(sessionStorage.getItem('admin')).email).toBe('fan@example.com');
});

test('signs up a new user', async () => {
  global.fetch.mockReturnValue(Promise.resolve({ ok: true, status: 201 }));

  renderApp('/sign up');
  expect(screen.getByText(/sign up to tickety/i)).toBeInTheDocument();
  await userEvent.type(screen.getByLabelText(/your email/i), 'new@example.com');
  await userEvent.type(screen.getByLabelText(/your password/i), 'secret123');
  await userEvent.click(screen.getByLabelText(/remember this device/i));
  await userEvent.click(screen.getByRole('button', { name: /sign up to your account/i }));

  await waitFor(() => expect(global.fetch).toHaveBeenCalledWith('/register', expect.objectContaining({ method: 'POST' })));
  expect(JSON.parse(global.fetch.mock.calls[0][1].body).email).toBe('new@example.com');
});
