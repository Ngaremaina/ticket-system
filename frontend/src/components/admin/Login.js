import { useState } from "react"

export default function Login({loginAdmin}){
    const [admin, setadmin] = useState({
        email:"",
        password:"",
    })

    function handleChange(event){
        const input = event.target.name;
        const value = event.target.value;
        return setadmin(prev =>  {return {...prev,[input]:value}})

    }

    function handleSubmit(event){
        event.preventDefault()
        loginadmin(admin)
    }
    return(
        <div>
            <form onSubmit={handleSubmit}>
                <input name ="email" type="text" placeholder="email" onChange={handleChange} value={admin.email}/>
                <input name="password" type="text" placeholder="password" onChange={handleChange} value={admin.password}/>
            
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}