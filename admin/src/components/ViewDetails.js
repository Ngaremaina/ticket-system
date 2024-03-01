import { useParams } from "react-router-dom"
import { useEffect, useState } from "react"

export default function ViewDetails(){
    const { name } = useParams()
    const [product, setEvents] = useState({})
    //Send a GET request to the events endpoint by name
    useEffect(()=>{
        const fetchingProduct = async () => {
            const response = await fetch(`/events/${name}`)
            const data = await response.json()
            
            return setEvents(data)
        }
        fetchingProduct()
    },[name])

     // Initialize state for ticket data using the 'useState' hook
    const [typeticket, setType] = useState({
        name:"",
        price:0,
    })

    // Function to handle form submission
    function handleSubmit(event){
        // Prevent the default form submission behavior
        event.preventDefault()
        typeticket["event_id"] = product.id

        // Send a POST request to the '/types' endpoint with the ticket data
        fetch("/types", {
            method:"POST",
            headers:{"Content-Type": "application/json"},
            body:JSON.stringify(typeticket)
        })

    }
    // Function to handle changes in user inputs
    function handleChange(event){
        // Extract the input id and value from the event target
        const input = event.target.id
        const value = event.target.value

        // Update the user state using the spread operator to maintain immutability
        return setType(prev => {return {...prev, [input]:value}})
    }

 
    //Display the tickets 
    const displayType = product.type?.map(item => {
        
        return <div className="block w-full p-6 bg-white border border-gray-200 rounded-lg shadow hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700" key={item.id}>
        <h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{item.name}</h5>
        <p className="font-normal text-gray-700 dark:text-gray-400">Kshs. {item.price}</p>
        
      </div>
        
    })

    
    return(
        <section className="bg-gray-50 dark:bg-gray-900">
        <div className="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 grid lg:grid-cols-2 gap-8 lg:gap-16">
            <div className="flex flex-col justify-center">
                <img src={product.image} alt={product.name}/>

            </div>
            <div>
            <div className="w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-white rounded-lg shadow-xl dark:bg-gray-800">
                <h2 className="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{product.name}</h2>
                <p className="font-normal text-gray-700 dark:text-gray-400">{product.description}</p>
                <p className="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">Location: {product.venue}</p>
                <div className="flex gap-2">
                <p className="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">Date: {product.date}</p>
                <p className="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">{product.time}</p>
                
                    
                </div>
                <p className="font-normal text-gray-700 dark:text-gray-400">Maximum number: {product.max_attendees} people</p>
                
                <div className="flex justify-center gap-4">
                    {displayType}
                </div>

                <div className="w-full lg:max-w-xl p-2 space-y-8 sm:p-8 bg-white rounded-lg shadow-xl dark:bg-gray-800">
                <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                Ticket
                </h2>
                <form className="mt-2 space-y-6" onSubmit = {handleSubmit} >
                <div>
                    <label htmlFor="type" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Type</label>
                    <select id = "name" name = "name" value ={typeticket.type} onChange = {handleChange}className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                        <option>Select</option>
                        <option value="VIP">VIP</option>
                        <option value="Regular">Regular</option>
                    </select>
                    
                </div>
                <div>
                    <label htmlFor="price" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Price</label>
                    <input type="number" name="price" id="price" placeholder="0" value = {typeticket.price} onChange = {handleChange} className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required  />
                </div>
            
                <button type="submit" className="w-full px-5 py-3 text-base font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 sm:w-auto dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Add Type</button>
               
                </form>
            </div>
                
               
            </div>
            </div>
        </div>
        </section>
    )
}