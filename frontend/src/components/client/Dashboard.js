import apiFetch from "../../api";
import {useEffect, useState} from "react"
import EventList from "./EventList"
import Reservation from "./Reservation";

export default function Dashboard(){
    const [events, setEvents] = useState([]);
    
    //Send a GET request to the '/events' endpoint to get the events
    useEffect(()=> {
        apiFetch("/events")
        .then(response => response.json())
        .then(data => setEvents(data))

    },[])

    return (
      <div>
        {/* Pass the events as a prop to the EventList*/}
        <EventList events={events}/>
        <Reservation/>

      </div>
    );
}