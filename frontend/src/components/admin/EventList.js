import EventItem from "./EventItem"

export default function EventList({events}){

   // Map through the 'events' array 
    const displayEvents = events?.map(event => {
        // Return an 'EventItem' component for each 'event' object in the array
        return <EventItem key = {event.id} id = {event.id} name = {event.name} description  = {event.description} image = {event.image} venue = {event.venue} date = {event.date} time = {event.time}/>
    })
    return(
            

<div class="relative overflow-x-auto">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
                <th scope="col" class="px-6 py-3">
                    ID
                </th>
                <th scope="col" class="px-6 py-3">
                    Event name
                </th>
                <th scope="col" class="px-6 py-3">
                    description
                </th>
                <th scope="col" class="px-6 py-3">
                    image
                </th>
                <th scope="col" class="px-6 py-3">
                    venue
                </th>
                <th scope="col" class="px-6 py-3">
                    date
                </th>
                <th scope="col" class="px-6 py-3">
                    time
                </th>
                <th scope="col" class="px-6 py-3">
                    details
                </th>
                <th scope="col" class="px-6 py-3">
                    edit
                </th>
                <th scope="col" class="px-6 py-3">
                    delete
                </th>
            </tr>
        </thead>
        <tbody>
            {displayEvents}
           
        </tbody>
    </table>
</div>

        
    )
}