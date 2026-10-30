import './App.css';
import { Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import RequireRole, { GuestOnly } from './components/RequireRole';
import ClientDashboard from './components/client/Dashboard';
import ClientEventDetails from './components/client/ViewDetails';
import AdminDashboard from './components/admin/Dashboard';
import AdminEventDetails from './components/admin/ViewDetails';
import AddForm from './components/admin/AddForm';
import EditForm from './components/admin/EditForm';

function App() {
  return (
    <div className="max-h-screen">
      <Routes>
        {/* Public routes */}
        <Route element={<GuestOnly />}>
          <Route path="/" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
        </Route>

        {/* Client routes */}
        <Route element={<RequireRole roles={['client']} />}>
          <Route path="/events" element={<ClientDashboard />} />
          <Route path="/events/:name" element={<ClientEventDetails />} />
        </Route>

        {/* Admin routes */}
        <Route path="/admin" element={<RequireRole roles={['admin']} />}>
          <Route index element={<AdminDashboard />} />
          <Route path="events/new" element={<AddForm />} />
          <Route path="events/:name" element={<AdminEventDetails />} />
          <Route path="events/:name/edit" element={<EditForm />} />
        </Route>

        {/* Anything else goes back to the login page (which redirects logged-in users home) */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </div>
  );
}

export default App;
