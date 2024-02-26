import { useState } from "react"

export default function Signup(){
    const [user, setUser] = useState({
        name:"",
        email:"",
        password:"",
        role:"client"
    })

    function handleChange(event){
        const input = event.target.name;
        const value = event.target.value;
        return setUser(prev =>  {return {...prev,[input]:value}})

    }

    function addUser(user){
        fetch("http://127.0.0.1:5000/register",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(user)

        })
        .then(response => response.json())
        .then(data => console.log(data))
    }

    function handleSubmit(event){
        event.preventDefault()
        addUser(user)
    }
    return(
        <div>
            <form onSubmit={handleSubmit}>
                <input name = "name" type="text" placeholder="name" onChange={handleChange} value={user.name}/>
                <input name ="email" type="text" placeholder="email" onChange={handleChange} value={user.email}/>
                <input name="password" type="text" placeholder="password" onChange={handleChange} value={user.password}/>
            
                <button type="submit">Submit</button>
            </form>
        </div>
    )
}