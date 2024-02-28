import EventItem from "./EventItem"

export default function EventList({events}){
    const displayEvents = events?.map(event => {
        return <EventItem key = {event.id} id = {event.id} name = {event.name} description  = {event.description} image = {event.image}/>
    })
    return(
        <div className="lg:grid grid-cols-2 xl:grid-cols-4 ">
            {displayEvents}
        </div>
    )
}