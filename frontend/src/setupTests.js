// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import '@testing-library/jest-dom';
import { TextDecoder, TextEncoder } from 'util';

// react-router v7 relies on TextEncoder, which jsdom does not provide
Object.assign(global, { TextDecoder, TextEncoder });

beforeEach(() => {
  // By default every API call behaves like a logged out session
  global.fetch = jest.fn(() =>
    Promise.resolve({ ok: false, status: 401, json: () => Promise.resolve({ error: 'Unauthorized' }) })
  );
  sessionStorage.clear();
});
