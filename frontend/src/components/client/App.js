import { Route, Routes, useNavigate} from "react-router-dom"
import Signup from "./Signup"
import Login from "./Login"
import DashBoard from "./DashBoard"
import {useEffect, useState} from "react"

export default function Client(){
    const [client, setClient] = useState({})
    const navigate = useNavigate()

    useEffect(() => {
        fetchUser()
    },[])

    const fetchUser = async () => {
        const response = await fetch("http://127.0.0.1:5000/current_user")
        const data = await response.json()
        return setClient(data)
    }


    function addUser(user){
        fetch("http://127.0.0.1:5000/register",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(user)

        })
        .then(response => response.json())
        .then(data => console.log(data))
    }

    function loginUser(user){
        fetch("http://127.0.0.1:5000/login",{
            method:'POST',
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(user)
        })
        .then(response => {
            if (response.status === 200) {
                navigate("/")
            }
            else{
                console.log("invalid")
            }
        })
        .then(data => console.log(data))
    }
    return(
        <div>
            <Routes>
                <Route path="/sign up" element = {<Signup addUser={addUser}/>} ></Route>
                <Route path="/sign in" element = {<Login loginUser={loginUser}/>}></Route>
                <Route path = "/" element = {<DashBoard user = {client} />}></Route>
            </Routes>
        </div>
    )
}