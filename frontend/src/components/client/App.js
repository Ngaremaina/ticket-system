import { Route, Routes} from "react-router-dom"
import Signup from "./Signup"
import DashBoard from "./DashBoard"
import ViewDetails from "./ViewDetails"
import { useAuth } from "../Authentication"
import Login from "./Login"

export default function Client(){
    const { admin } = useAuth();
    
    return(
        <Routes>
        {/* Redirect to Dashboard if authenticated */}
        {admin && <Route path="/" element={<DashBoard />} />}

        {/* Authenticated routes */}
        {admin && (
          <>
            <Route path="/dashboard" element={<DashBoard />} />
            <Route path="/details/:name" element={<ViewDetails />} />
          </>
        )}

        {/* Unauthenticated route */}
        {!admin && <Route path="/*" element={<Login />} />}
        {!admin && <Route path="/sign up" element={<Signup />} />}
        

        </Routes>
    )
}