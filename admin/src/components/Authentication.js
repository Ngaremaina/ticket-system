// authContext.js
import { createContext, useContext, useState, useEffect } from 'react';
import { Navigate } from 'react-router-dom';

const AuthContext = createContext();

export const Authentication = ({ children }) => {
    // const navigate = useNavigate()
  const [admin, setAdmin] = useState(() => {
    // Initialize admin state from sessionStorage, if available
    const storedAdmin = sessionStorage.getItem('admin');
    return storedAdmin ? JSON.parse(storedAdmin) : null;
  });

  const loginUser = async (user) => {
    try {
      const response = await fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
      });

      if (!response.ok) {
        throw new Error('Invalid login credentials');
      }

      const adminData = await response.json();
      setAdmin(adminData);

      // Save admin data to sessionStorage
      sessionStorage.setItem('admin', JSON.stringify(adminData));

      return adminData;
    } catch (error) {
      throw new Error('An error occurred during login');
    }
  };

  const logout = async () => {
    try {

        const response = await fetch('http://127.0.0.1:5000/logout', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
        });

        if (!response.ok) {
          throw new Error('Logout failed');
        }

        setAdmin(null);

        // Remove admin data from sessionStorage
        sessionStorage.removeItem('admin');

        // Navigate to "/"
        return <Navigate to="/" />;
    
    } catch (error) {
      throw new Error('An error occurred during logout');
    }
  };

  // Cleanup localStorage on component unmount
  useEffect(() => {
    return () => sessionStorage.removeItem('admin');
  }, []);

  return (
    <AuthContext.Provider value={{ admin, loginUser, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};