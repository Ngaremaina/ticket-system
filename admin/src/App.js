import './App.css';
import { Routes, Route } from'react-router-dom';
import Login from './components/Login';
import DashBoard from './components/Dashboard';
import { useAuth } from './components/Authentication';
import EventForm from './components/Form';
import AddForm from './components/AddForm';
import ViewDetails from './components/ViewDetails';

function App() {
  const { admin } = useAuth();
 


  return (
    <div className="App">
       <Routes>
        {/* Redirect to Dashboard if authenticated */}
        {admin && <Route path="/admin" element={<DashBoard />} />}

        {/* Authenticated routes */}
        {admin && (
          <>
            
            <Route path="/dashboard" element={<DashBoard />} />
            <Route path="/edit/:name" element={<EventForm />} />
            <Route path='/add event' element ={<AddForm />}/>
            <Route path='/events/:name' element ={<ViewDetails />}/>
          </>
        )}

        {/* Unauthenticated route */}
        {!admin && <Route path="/*" element={<Login />} />}
        {/* {!admin && <Route path="/sign up" element={<Signup />} />} */}
        

        </Routes>
    </div>
  );
}

export default App;
