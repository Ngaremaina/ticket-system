import { Route, Routes, useNavigate} from "react-router-dom"
import Signup from "./Signup"
import Login from "./Login"

export default function Client(){
    const navigate = useNavigate()
    function addUser(user){
        fetch("http://127.0.0.1:5000/register",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(user)

        })
        .then(response => response.json())
        .then(data => console.log(data))
    }

    function loginUser(){
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
            </Routes>
        </div>
    )
}