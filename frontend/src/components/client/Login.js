import { useState } from "react"
import { useNavigate } from "react-router-dom";

export default function Login(){
    const navigate = useNavigate()

    const [user, setUser] = useState({
        email:"",
        password:"",
    })

    function handleChange(event){
        const input = event.target.name;
        const value = event.target.value;
        return setUser(prev =>  {return {...prev,[input]:value}})

    }


    function loginUser(user){
        fetch("http://127.0.0.1:5000/login",{
            method:'POST',
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(user)
        })
        .then(response => {
            if (response.status === 200) {
                navigate("/")
            }
            else{
                console.log("invalid")
            }
        })
        .then(data => console.log(data))
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