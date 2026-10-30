import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { MemoryRouter } from 'react-router-dom';
import App from './App';
import { Authentication } from './components/Authentication';

const ADMIN = { id: 1, email: 'admin@example.com', role: 'admin' };
const CLIENT = { id: 2, email: 'fan@example.com', role: 'client' };
const EVENTS = [
  { id: 1, name: 'Concert', description: 'Live music', venue: 'Nairobi', date: '2026-12-01', time: '18:00', image: 'x.png', type: [] },
];

function json(body, ok = true) {
  return Promise.resolve({ ok, status: ok ? 200 : 401, json: () => Promise.resolve(body) });
}

// Mock the API: `account` is the user /login accepts. Pass loggedIn=false to start
// without a server session (so /current_user only reports the user after /login).
function mockApi(account, loggedIn = true) {
  let session = loggedIn ? account : null;
  global.fetch.mockImplementation((url) => {
    if (url === '/current_user') return session ? json(session) : json({ error: 'Unauthorized' }, false);
    if (url === '/login') {
      session = account;
      return account ? json(account) : json({ message: 'Unauthorized' }, false);
    }
    if (url === '/events') return json(EVENTS);
    if (url.startsWith('/users/')) return json({ ...session, ticket: [] });
    return json({});
  });
}

function renderApp(route, user = null) {
  if (user) sessionStorage.setItem('user', JSON.stringify(user));
  return render(
    <Authentication>
      <MemoryRouter initialEntries={[route]}>
        <App />
      </MemoryRouter>
    </Authentication>
  );
}

async function login(email) {
  await userEvent.type(screen.getByLabelText(/your email/i), email);
  await userEvent.type(screen.getByLabelText(/your password/i), 'secret123');
  await userEvent.click(screen.getByLabelText(/remember this device/i));
  await userEvent.click(screen.getByRole('button', { name: /login to your account/i }));
}

describe('guests', () => {
  test.each(['/admin', '/admin/events/new', '/events', '/nowhere'])('are sent to login from %s', (route) => {
    mockApi(null);
    renderApp(route);
    expect(screen.getByText(/sign in to tickety/i)).toBeInTheDocument();
  });

  test('can open the sign up page', () => {
    mockApi(null);
    renderApp('/signup');
    expect(screen.getByText(/sign up to tickety/i)).toBeInTheDocument();
  });

  test('see an error for bad credentials', async () => {
    mockApi(null);
    renderApp('/');
    await login('nobody@example.com');
    expect(await screen.findByRole('alert')).toHaveTextContent(/invalid email or password/i);
  });
});

describe('admins', () => {
  test('land on the admin dashboard after login', async () => {
    mockApi(ADMIN, false);
    renderApp('/');
    await login(ADMIN.email);

    expect(await screen.findByRole('columnheader', { name: /event name/i })).toBeInTheDocument();
    expect(screen.getByRole('link', { name: /add event/i })).toHaveAttribute('href', '/admin/events/new');
    expect(await screen.findByText('Concert')).toBeInTheDocument();
  });

  test('are redirected away from client pages', async () => {
    mockApi(ADMIN);
    renderApp('/events', ADMIN);
    expect(await screen.findByRole('columnheader', { name: /event name/i })).toBeInTheDocument();
  });

  test('can open the add event form', () => {
    mockApi(ADMIN);
    renderApp('/admin/events/new', ADMIN);
    expect(screen.getByRole('heading', { name: /add event/i })).toBeInTheDocument();
  });
});

describe('clients', () => {
  test('land on the events page after login', async () => {
    mockApi(CLIENT, false);
    renderApp('/');
    await login(CLIENT.email);

    expect(await screen.findByText(/my reservations/i)).toBeInTheDocument();
    expect(screen.queryByRole('link', { name: /add event/i })).not.toBeInTheDocument();
    expect(await screen.findByRole('link', { name: /read more/i })).toHaveAttribute('href', '/events/Concert');
  });

  test.each(['/admin', '/admin/events/new', '/admin/events/Concert/edit'])('are redirected away from %s', async (route) => {
    mockApi(CLIENT);
    renderApp(route, CLIENT);
    expect(await screen.findByText(/my reservations/i)).toBeInTheDocument();
    expect(screen.queryByRole('heading', { name: /add event|update event/i })).not.toBeInTheDocument();
  });
});

test('an expired server session logs the user out', async () => {
  mockApi(null);
  renderApp('/admin', ADMIN);
  expect(await screen.findByText(/sign in to tickety/i)).toBeInTheDocument();
  expect(sessionStorage.getItem('user')).toBeNull();
});

test('signing out returns to the login page', async () => {
  mockApi(CLIENT);
  renderApp('/events', CLIENT);
  await userEvent.click(await screen.findByRole('button', { name: /sign out/i }));
  expect(await screen.findByText(/sign in to tickety/i)).toBeInTheDocument();
});
