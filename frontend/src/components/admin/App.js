import { Route, Routes } from "react-router-dom"
import Login from "./Login"
import { useEffect, useState } from "react"
import DashBoard from "./DashBoard"
export default function Admin(){
    const [events, setEvents] = useState([])

    useEffect(() => {
        fetchEvents()
    },[])

    const fetchEvents = async () =>{
        const response = await fetch();
        const data = await response.json()
        return setEvents(data)
    }
    function loginAdmin(user){
        fetch("",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(user)

        })
        .then(response => response.json())
        .then(data => console.log(data))
    }
    return(
        <div>
            <Routes>
                <Route path="/admin/login" element = {<Login/>}></Route>
                <Route path="/admin/dashboard" element = {<DashBoard events = {events} />}></Route>
            </Routes>
        </div>
    )
}