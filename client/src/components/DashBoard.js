import {useEffect, useState} from "react"
import EventList from "./EventList"
import Header from "./Header"
import Reservation from "./Reservation";

export default function DashBoard({tickets}){
    const [events, setEvents] = useState([]);
    

    useEffect(()=> {
        fetch("/events")
        .then(response => response.json())
        .then(data => setEvents(data))

    },[])

    return (
      <div>
        <Header/>
        <EventList events={events}/>
        <Reservation/>

      </div>
    );
}