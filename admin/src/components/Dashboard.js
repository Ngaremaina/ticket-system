import {useEffect, useState} from "react"
import EventList from "./EventList"
import Header from "./Header";

export default function DashBoard({EDITMODE}){
    const [events, setEvents] = useState([]);

    useEffect(()=> {
        fetch("http://127.0.0.1:5000/events")
        .then(response => response.json())
        .then(data => setEvents(data))

    },[])
  
    return (
      <div>
        <Header/>
        <EventList events={events}  EDITMODE = {EDITMODE}/>
      </div>
    );
}