import {useEffect, useState} from "react"
import { useAuth } from "./Authentication"
export default function Reservation(){
    const [tickets, setTickets] = useState([])
    const {admin} = useAuth();
    // const [ticketCount, setTicketCount] = useState(0);
    


    useEffect(()=>{
         fetch(`http://127.0.0.1:5000/users/${admin.id}`)
         .then(response => response.json())
         .then(data => setTickets(data.ticket))
        
    },[admin.id])


  

    const displayTicket = tickets?.map(item => {
        
        return <div className="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700" key={item.id}>
            <img className="rounded-t-lg h-3/6 w-full" src={item.image} alt = {item.name}/>
        <div className="p-5">
            <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{item.name}</h5>
            <p className="mb-3 font-normal text-gray-700 dark:text-gray-400">{item.type_name} for {item.persons} person @ Kshs.{item.price}</p>
            <p className="mb-3 font-normal text-gray-700 dark:text-gray-400">Date: {item.date} AT {item.time} HRS</p>
            <p className="mb-3 font-normal text-gray-700 dark:text-gray-400">Location: {item.venue}</p>
        </div>
    </div>

        
     })

    return(
        <div>
            <h3 className="mb-3 mt-3 text-center text-4xl font-bold uppercase tracking-tight text-gray-900 dark:text-white">My Reservations</h3>
            <div className="lg:grid grid-cols-2 xl:grid-cols-4 gap-3">
                {displayTicket}
            </div>
        </div>
        
    )

}