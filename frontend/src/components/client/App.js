import { Route, Routes } from "react-router-dom"
import Signup from "./Signup"
import Login from "./Login"

export default function Client(){
    function addUser(user){
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
                <Route path="/sign up" element = {<Signup addUser={addUser}/>} ></Route>
                <Route path="/sign in" element = {<Login/>}></Route>
            </Routes>
        </div>
    )
}