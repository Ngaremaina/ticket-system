// Base URL of the Flask API. Empty in development so requests go through the CRA proxy;
// set REACT_APP_API_URL at build time when the API is deployed on another domain.
const API_URL = (process.env.REACT_APP_API_URL || "").replace(/\/$/, "");

// fetch() wrapper that prefixes the API URL and always sends the session cookie
export default function apiFetch(path, options = {}) {
  return fetch(`${API_URL}${path}`, { credentials: "include", ...options });
}
