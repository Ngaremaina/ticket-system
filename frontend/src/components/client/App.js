import { Route, Routes, useNavigate} from "react-router-dom"
import Signup from "./Signup"
import Login from "./Login"
import DashBoard from "./DashBoard"


export default function Client(){
    
    return(
        <div>
            <Routes>
                <Route path="/sign up" element = {<Signup />} ></Route>
                <Route path="/sign in" element = {<Login />}></Route>
                <Route path = "/" element = {<DashBoard/>}></Route>
            </Routes>
        </div>
    )
}