import { useState } from "react"

export default function EventForm({formEvent}){
    const [event, setEvent] = useState({
        email:"",
        password:"",
    })

    function handleChange(event){
        const input = event.target.name;
        const value = event.target.value;
        return setEvent(prev =>  {return {...prev,[input]:value}})

    }

    function handleSubmit(event){
        event.preventDefault()
        formEvent(event)
    }
    return(
        <div>
            <form onSubmit={handleSubmit}>
                <input name ="email" type="text" placeholder="email" onChange={handleChange} value={event.email}/>
                <input name="password" type="text" placeholder="password" onChange={handleChange} value={event.password}/>
            
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}