import React, { useState, useEffect } from "react";
// import axios from "axios";
 
function Profile(props) {
 
    const [profileData, setProfileData] = useState(null)
     
    useEffect(() => {
        getUsers();
    }, []);
     
    const email = localStorage.getItem('email');
     
    function getUsers() { 
        fetch(`http://127.0.0.1:5000/profile/${email}`,{
            method:"GET",
            headers:{Authorization: 'Bearer ' + props.token}
        })
        .then((response) => {
            console.log(response)
          const res =response.data
          res.access_token && props.setToken(res.access_token)
          setProfileData(({
            profile_name: res.name,
            profile_email: res.email,
            about_me: res.about}))
        }).catch((error) => {
          if (error.response) {
            console.log(error.response)
            console.log(error.response.status)
            console.log(error.response.headers)
            }
        })
    }
     
    // let imgs = [
    //   'https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava1-bg.webp',
    // ];
 
 
  return (
      <div className="">
        
        <p className="">{profileData.profile_email}</p>

        
    </div>
  );
}
 
export default Profile;