import {Link} from "react-router-dom"

export default function EventItem({id, name, description, image, venue, time, date, }){
    function handleDelete(){
        fetch(`/events/${id}`,{
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            }
        })
    }
    
    return(       

        <tr className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
            <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                {id}
            </th>
            <td className="px-6 py-4">
                {name}
            </td>
            <td className="px-6 py-4">
                {description}
            </td>
            <td className="px-6 py-4">
                {image}
            </td>
            <td className="px-6 py-4">
                {venue}
            </td>
           
            <td className="px-6 py-4">
                {date}
            </td>
            <td className="px-6 py-4">
                {time}
            </td>
            <td className="px-6 py-4">
                <Link to={`/events/${name}`}>View</Link>
            </td>
            <td className="px-6 py-4">
                <Link to={`/edit/${name}`}>Edit</Link>
            </td>
            <td className="px-6 py-4">
                <button onClick={handleDelete}>Delete</button>
            </td>

            
        </tr>


)
}