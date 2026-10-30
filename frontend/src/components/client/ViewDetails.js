import apiFetch from "../../api";
import { useNavigate, useParams } from "react-router-dom"
import { useEffect, useState } from "react"
import { useAuth } from "../Authentication";

export default function ViewDetails(){
    const { name } = useParams()
    const {user} = useAuth()
    const [event, setEvents] = useState({})
    const [tickets, setTickets] = useState([])
    const navigate = useNavigate()
    
    //Send a GET request to the '/events' and '/users' endpoints by 'name' and 'id' respectively
    useEffect(()=>{
        const fetchingProduct = async () => {
            const response = await apiFetch(`/events/${encodeURIComponent(name)}`)
            const data = await response.json()
            return setEvents(data)
        }
        const fetchingTickets = async () => {
            const response = await apiFetch(`/users/${user.id}`)
            const data = await response.json()
            return setTickets(data.ticket)
        }
        fetchingProduct()
        fetchingTickets()
    },[name, user.id])

    //Count the number of tickets booked from the logged in user
    const count = tickets?.length   

    //Map the tickets
    const displayType = event.type?.map(item => {

        //Function to handle Ticket Reservation
        const handleReservation = () => {
            //Initialize ticket object to get the ticket details
            const ticket ={
                "name": event.name,
                "description": event.description,
                "venue": event.venue,
                "date": event.date,
                "time": event.time,
                "image": event.image,
                "persons":1,
                "type_name":item.name,
                "price":item.price,
                "auth_id":user.id
            }
            //Check if the tickets are less than 5
            if (count < 5){

                //Send a POST request to the '/tickets' endpoint with the ticket data
                apiFetch("/tickets",{
                    method:"POST",
                    headers:{"Content-Type": "application/json"},
                    body:JSON.stringify(ticket)
            })
            .then(async response => {
                //Navigate to the dashboard if response is OK
                if (response.ok){
                    navigate('/events')
                }
                //Otherwise show the reason from the API (e.g. ticket limit reached)
                else{
                    const data = await response.json()
                    alert(data.error || "Could not book the ticket")
                }
            })

            }
            //Display an alert if tickets are more than 5
            else{
                alert("You have reached the maximum number of tickets")
            }            
          };
        
        return <div className="cursor-pointer block w-full p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700" onClick={handleReservation} key={item.id}>
        <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{item.name}</h5>
        <p className="font-normal text-gray-700 dark:text-gray-400">Kshs. {item.price}</p>
      </div>
        
    })

    
    return(
        <div>
             <section className="bg-gray-50 dark:bg-gray-900">
        <div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16">
            <div className="flex flex-col justify-center">
                <img src={event.image} alt={event.name}/>
                
            </div>
            <div>
            <div className="w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-white rounded-lg shadow-xl dark:bg-gray-800">
                <h2 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{event.name}</h2>
                <p className="font-normal text-gray-700 dark:text-gray-400">{event.description}</p>
                <p className="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">Location: {event.venue}</p>
                <div className="flex gap-2">
                <p className="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">Date: {event.date}</p>
                <p className="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">{event.time}</p>
                
                    
                </div>
                <h3 className="mb-2 text-xl tracking-tight text-gray-900 dark:text-white">Click to book your ticket</h3>
                
                <div className="flex justify-center gap-4">
                    
                    {displayType}
                </div>

            </div>
            </div>
        </div>
        </section>

        </div>
       
    )
}