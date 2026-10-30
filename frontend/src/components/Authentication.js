import apiFetch from "../api";
import { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

// Landing page for each role after login
export const ROLE_HOME = {
  admin: '/admin',
  client: '/events',
};

export const homeFor = (user) => (user && ROLE_HOME[user.role]) || '/';

function storeUser(user) {
  if (user) {
    sessionStorage.setItem('user', JSON.stringify(user));
  } else {
    sessionStorage.removeItem('user');
  }
}

export const Authentication = ({ children }) => {
  // Initialize user state from sessionStorage, if available
  const [user, setUser] = useState(() => {
    const storedUser = sessionStorage.getItem('user');
    return storedUser ? JSON.parse(storedUser) : null;
  });

  // The server session is the source of truth: re-sync on load in case it expired
  useEffect(() => {
    apiFetch('/current_user')
      .then(response => (response.ok ? response.json() : null))
      .then(currentUser => {
        setUser(currentUser);
        storeUser(currentUser);
      })
      .catch(() => {});
  }, []);

  const loginUser = async (credentials) => {
    const response = await apiFetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(credentials),
    });

    if (!response.ok) {
      throw new Error('Invalid login credentials');
    }

    const userData = await response.json();
    setUser(userData);
    storeUser(userData);

    return userData;
  };

  const logout = async () => {
    try {
      await apiFetch('/logout', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });
    } finally {
      // Clear local state even if the request fails; route guards redirect to login
      setUser(null);
      storeUser(null);
    }
  };

  return (
    <AuthContext.Provider value={{ user, loginUser, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};
