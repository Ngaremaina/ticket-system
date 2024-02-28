import { Route, Routes } from "react-router-dom"
import Login from "./Login"
import DashBoard from "./DashBoard"
import { useAuth } from "../Authentication"

export default function Admin(){
    const { admin } = useAuth();
    

    return(
        <Routes>
        {/* Redirect to Dashboard if authenticated */}
        {admin && <Route path="/admin" element={<DashBoard />} />}

        {/* Authenticated routes */}
        {admin && (
          <>
            <Route path="/admin/dashboard" element={<DashBoard />} />
            {/* <Route path="/details/:name" element={<ViewDetails />} /> */}
          </>
        )}

        {/* Unauthenticated route */}
        {!admin && <Route path="/" element={<Login />} />}
        {/* {!admin && <Route path="/sign up" element={<Signup />} />} */}
        

        </Routes>
    )
}