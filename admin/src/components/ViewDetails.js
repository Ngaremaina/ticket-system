import { useParams } from "react-router-dom"
import { useEffect, useState } from "react"

export default function ViewDetails(){
    const { name } = useParams()
    const [event, setEvents] = useState({})

    useEffect(()=>{
        const fetchingProduct = async () => {
            const response = await fetch(`http://127.0.0.1:5000/events/${name}`)
            const data = await response.json()
            return setEvents(data)
        }
        fetchingProduct()
    },[name])
    

    const displayType = event.type?.map(item => {
        
        return <div className="block w-full p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700" key={item.id}>
        <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{item.name}</h5>
        <p className="font-normal text-gray-700 dark:text-gray-400">Kshs. {item.price}</p>
      </div>
        
    })

    
    return(
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
                
                <div className="flex justify-center gap-4">
                    {displayType}
                </div>
                
               
            </div>
            </div>
        </div>
        </section>
    )
}