import React, { useState, useEffect, useContext } from "react";
import AuthContext from "../context/AuthContext";
import useAxios from "../utils/useAxios";
import jwt_decode from "jwt-decode";

const HomePage = () => {
    let [notes, setNotes] = useState([]);
    let { authTokens, logoutUser } = useContext(AuthContext);
    let a = jwt_decode(authTokens.access);
    let api = useAxios();

    useEffect(() => {}, []);
    console.log(a.user_id);
    return (
        <div>
            <p>You are logged to the home page!</p>
        </div>
    );
};

export default HomePage;
