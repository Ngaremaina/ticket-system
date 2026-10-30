import EventItem from "./EventItem"

export default function EventList({events}){
     // Map through the 'events' array 
    const displayEvents = events?.map(event => {
         // Return an 'EventItem' component for each 'event' object in the array
        return <EventItem key = {event.id} id = {event.id} name = {event.name} description  = {event.description} image = {event.image} venue = {event.venue} date = {event.date} time = {event.time}/>
    })
    return(
        <div className="lg:grid grid-cols-2 xl:grid-cols-4 gap-3">
            {displayEvents}
        </div>
    )
}