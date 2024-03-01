import {useEffect, useState} from "react"
import EventList from "./EventList"
import Header from "./Header";

export default function DashBoard({EDITMODE}){
  // Initialize state for events data using the 'useState' hook
    const [events, setEvents] = useState([]);

    // Send a GET request to the '/events' endpoint with the form data
    useEffect(()=> {
        fetch("/events")
        .then(response => response.json())
        .then(data => setEvents(data))

    },[])
  
    return (
      <div>
        <Header/>
        {/* Pass the events state as props */}
        <EventList events={events} />
      </div>
    );
}