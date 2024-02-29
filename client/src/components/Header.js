import React, { } from "react";
import { useAuth } from "./Authentication";
import {Link} from "react-router-dom"
 
function Header() {
    const { logout, admin } = useAuth();
    
    
     
    return(
        
            <nav className="bg-white dark:bg-gray-900  w-full z-20 top-0 start-0 border-b border-gray-200 dark:border-gray-600">
            <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-2">
                <Link to="/dashboard" className="flex items-center space-x-3 rtl:space-x-reverse">
                <img src="https://images.pexels.com/photos/796606/pexels-photo-796606.jpeg" className="h-8" alt="Tickety" />
                <span className="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Tickety</span>
                </Link>
                <div className="flex md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
                    <p className="self-center text-md px-3 font-semibold whitespace-nowrap dark:text-white">{admin.email}</p>
                <button type="button" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" onClick={logout} >Sign out</button>
               
                </div>
                
            </div>
            </nav>


            


    )
}
 
export default Header;