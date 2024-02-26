import EventItem from "./EventItem"

export default function DashBoard({events}){

    const displayEvents = events?.map(event => {
        return <EventItem key = {event.id} name = {event.name} description  = {event.description}/>
    })
    return(
        <div>
            {displayEvents}
        </div>
    )
}