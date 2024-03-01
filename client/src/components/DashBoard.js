import {useEffect, useState} from "react"
import EventList from "./EventList"
import Header from "./Header"
import Reservation from "./Reservation";

export default function DashBoard({tickets}){
    const [events, setEvents] = useState([]);
    
    //Send a GET request to the '/events' endpoint to get the events
    useEffect(()=> {
        fetch("/events")
        .then(response => response.json())
        .then(data => setEvents(data))

    },[])

    return (
      <div className="dark:bg-gray-800 dark:border-gray-700">
        <Header/>
        {/* Pass the events as a prop to the EventList*/}
        <EventList events={events}/>
        <Reservation/>

      </div>
    );
}