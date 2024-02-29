import { useState } from "react"
import { useNavigate } from "react-router-dom";
import { useAuth } from "./Authentication";

export default function Login(){
    const navigate = useNavigate()
    const {loginUser} = useAuth()

    const [user, setUser] = useState({
        email:"",
        password:"",
    })

    

    function handleChange(event){
        const input = event.target.name;
        const value = event.target.value;
        return setUser(prev =>  {return {...prev,[input]:value}})

    }

    function handleSubmit(event){
        event.preventDefault()
        loginUser(user)
        .then(() => {
            // Navigate to the desired location after successful login
            navigate('/dashboard');
            })
        }


    return(       

        <div className="bg-gray-50 dark:bg-gray-900 max-h-screen">
        <div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-24 grid lg:grid-cols-2 gap-8 lg:gap-16">
            <div className="flex flex-col justify-center">
            <h1 className="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white">Welcome to Tickety</h1>
            <p className="mb-6 text-lg font-normal text-gray-500 lg:text-xl dark:text-gray-400">Tickety is a comprehensive ticketing application designed to streamline the ticket management process for businesses and organizations of all sizes. With Tickety, users can easily create, track, and manage tickets for various purposes, including customer support, IT helpdesk, event management, and more. Tickety empowers businesses to deliver exceptional customer service, improve operational efficiency, and enhance collaboration across teams through its intuitive ticketing solution.</p>
            
            </div>
            <div>
            <div className="w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-white rounded-lg shadow-xl dark:bg-gray-800">
                <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                Sign in to Tickety
                </h2>
                <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="email" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
                    <input type="email" name="email" id="email" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="johndoe@example.com" required onChange={handleChange} value={user.email}/>
                </div>
                <div>
                    <label htmlFor="password" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your password</label>
                    <input type="password" name="password" id="password" placeholder="••••••••" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required  onChange={handleChange} value={user.password}/>
                </div>
                <div className="flex items-start">
                    <div className="flex items-center h-5">
                    <input id="remember" aria-describedby="remember" name="remember" type="checkbox" className="w-4 h-4 border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:bg-gray-700 dark:border-gray-600" required />
                    </div>
                    <div className="ms-3 text-sm">
                    <label htmlFor="remember" className="font-medium text-gray-500 dark:text-gray-400">Remember this device</label>
                    </div>
                    <a href="/forgot password" className="ms-auto text-sm font-medium text-blue-600 hover:underline dark:text-blue-500">Lost Password?</a>
                </div>
                <button type="submit" className="w-full px-5 py-3 text-base font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 sm:w-auto dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Login to your account</button>
                
                </form>
            </div>
            </div>
        </div>
        </div>


    )
}