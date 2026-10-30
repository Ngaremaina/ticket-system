import { Navigate, Outlet, useLocation } from "react-router-dom";
import { homeFor, useAuth } from "./Authentication";
import Header from "./Header";

// Layout route that only renders its children for users with one of the given roles.
// Guests are sent to the login page; other roles are sent to their own home page.
export default function RequireRole({ roles }) {
    const { user } = useAuth();
    const location = useLocation();

    if (!user) {
        return <Navigate to="/" replace state={{ from: location }} />;
    }

    if (!roles.includes(user.role)) {
        return <Navigate to={homeFor(user)} replace />;
    }

    return (
        <div className="dark:bg-gray-800 dark:border-gray-700">
            <Header />
            <Outlet />
        </div>
    );
}

// Public pages (login / sign up) redirect logged-in users to their home page
export function GuestOnly() {
    const { user } = useAuth();
    return user ? <Navigate to={homeFor(user)} replace /> : <Outlet />;
}
