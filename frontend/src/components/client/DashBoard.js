import {useEffect, useState} from "react"
import { Link, useNavigate } from "react-router-dom"
import Signup from "./Signup"


export default function DashBoard(){
    const navigate = useNavigate()

    const [client, setClient] = useState(null)

    useEffect(() => {
        
        const fetchUser = async () => {
            const response = await fetch("http://127.0.0.1:5000/current_user")
            const data = await response.json()
            return setClient(data)
        }
        fetchUser()
    },[])

    

    function handleLogout(){
        fetch("http://127.0.0.1:5000/logout",{
            method:"POST",
            headers:{"Content-Type":"application/json"},

        })
        .then(response => response.json())
        .then(data => console.log(data))
    }
    return(
        <div>{client ? (
            <div>Logged in
                <p>ID: {client.id}</p>
                <button onClick={handleLogout}>Logout</button>
            </div>
            
        ) : (
            navigate("/sign in")
        ) }</div>
    )
}