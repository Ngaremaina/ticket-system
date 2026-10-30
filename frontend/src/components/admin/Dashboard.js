import apiFetch from "../../api";
import {useEffect, useState} from "react"
import EventList from "./EventList"

export default function Dashboard(){
  // Initialize state for events data using the 'useState' hook
    const [events, setEvents] = useState([]);

    // Send a GET request to the '/events' endpoint with the form data
    function loadEvents(){
        apiFetch("/events")
        .then(response => response.json())
        .then(data => setEvents(data))
    }

    useEffect(loadEvents, [])
  
    return (
      <div>
        {/* Pass the events as props to the EventList*/}
        <EventList events={events} onDelete={loadEvents} />
      </div>
    );
}