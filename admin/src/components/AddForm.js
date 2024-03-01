import { useState } from "react"
import { useNavigate } from "react-router-dom"

export default function AddForm(){
    const navigate = useNavigate()
     
    // Initialize state for form data using the 'useState' hook
    const [form, setForm] = useState({
        name:"",
        description:"",
        image:"",
        max_attendees:0,
        venue:"",
        date:"",
        time:""
    })
    // Function to handle changes in form inputs
    function handleChange(event){
        // Extract the input id and value from the event target
        const input = event.target.id
        const value = event.target.value

        // Update the form state using the spread operator to maintain immutability
        setForm(prev => {return {...prev, [input]: value}})

    }
    // Function to handle form submission
    function handleSubmit(event){
        // Prevent the default form submission behavior
        event.preventDefault();

         // Send a POST request to the '/events' endpoint with the form data
        fetch("/events", {
            method:"POST",
            
            headers:{"Content-Type": "application/json"},
            body:JSON.stringify(form)
        })
        .then(response => {
            // If the response is OK, navigate to the '/dashboard' route
            if (response.ok){
                navigate('/dashboard')
            }
        })

    }
    return(
        <div className = "flex justify-center">
            <div className="w-full lg:max-w-xl p-6 space-y-8 sm:p-8 bg-white rounded-lg shadow-xl dark:bg-gray-800">
                <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
                Add Event
                </h2>
                <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
                <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Event Name</label>
                    <input type="text" name="name" id="name" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required onChange={handleChange} value={form.name}/>
                </div>
                <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Description</label>
                    <textarea type="text" name="description" id="description" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required  onChange={handleChange} value={form.description}></textarea>
                </div>
                <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Image Link</label>
                    <input type="text" name="image" id="image" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required  onChange={handleChange} value={form.image}/>
                </div>
                <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Date</label>
                    <input type="date" name="date" id="date" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required  onChange={handleChange} value={form.date}/>
                </div>
                <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Time</label>
                    <input type="time" name="time" id="time" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required  onChange={handleChange} value={form.time}/>
                </div>
                <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Venue</label>
                    <input type="text" name="venue" id="venue" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required  onChange={handleChange} value={form.venue}/>
                </div>

                <div>
                    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Attendees</label>
                    <input type="number" name="max_attendees" id="max_attendees" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required  onChange={handleChange} value={form.max_attendees}/>
                </div>
                
                
                <button type="submit" className="w-full px-5 py-3 text-base font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 sm:w-auto dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Add Event</button>
                
                </form>
            </div>
             
        </div>
       
        
    )
}