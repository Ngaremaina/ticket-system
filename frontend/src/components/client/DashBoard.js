import {useEffect, useState} from "react"
import { Link } from "react-router-dom"
import Signup from "./Signup"


export default function DashBoard(){

    const [client, setClient] = useState(null)

    useEffect(() => {
        fetchUser()
    },[])

    const fetchUser = async () => {
        const response = await fetch("http://127.0.0.1:5000/current_user")
        const data = await response.json()
        return setClient(data)
    }
    return(
        <div>{client !== null ? (
            <div>Logged in</div>
        ) : (
            <div><Signup/></div> 
        ) }</div>
    )
}