import { useState } from "react"

export default function Login({loginUser}){
    const [user, setUser] = useState({
        email:"",
        password:"",
    })

    function handleChange(event){
        const input = event.target.name;
        const value = event.target.value;
        return setUser(prev =>  {return {...prev,[input]:value}})

    }

    function handleSubmit(event){
        event.preventDefault()
        loginUser(user)
    }
    return(
        <div>
            <form onSubmit={handleSubmit}>
                <input name ="email" type="text" placeholder="email" onChange={handleChange} value={user.email}/>
                <input name="password" type="text" placeholder="password" onChange={handleChange} value={user.password}/>
            
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}