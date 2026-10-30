import React from "react";
import { homeFor, useAuth } from "./Authentication";
import { Link } from "react-router-dom"

// Navigation links shown to each role
const NAV_LINKS = {
    admin: [
        { to: "/admin", label: "Events" },
        { to: "/admin/events/new", label: "Add Event" },
    ],
    client: [
        { to: "/events", label: "Events" },
    ],
};

function Header() {
    const { logout, user } = useAuth();
    const links = NAV_LINKS[user.role] || [];

    return(
            <nav className="bg-white dark:bg-gray-900  w-full z-20 top-0 start-0 border-b border-gray-200 dark:border-gray-600">
            <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-2">
                <Link to={homeFor(user)} className="flex items-center space-x-3 rtl:space-x-reverse">
                <img src="https://images.pexels.com/photos/796606/pexels-photo-796606.jpeg" className="h-8" alt="Tickety" />
                <span className="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Tickety</span>
                </Link>
                <div className="flex md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
                    <p className="self-center text-md px-3 font-semibold whitespace-nowrap dark:text-white">{user.email}</p>
                <button type="button" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" onClick={logout} >Sign out</button>
                </div>
                <div className="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-sticky">
                <ul className="flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
                    {links.map(link => (
                        <li key={link.to}>
                        <Link to={link.to} className="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">{link.label}</Link>
                        </li>
                    ))}
                </ul>
                </div>
            </div>
            </nav>
    )
}

export default Header;
