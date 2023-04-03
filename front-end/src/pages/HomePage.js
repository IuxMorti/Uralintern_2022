import React, { useState, useEffect, useContext } from "react";
import AuthContext from "../context/AuthContext";
import useAxios from "../utils/useAxios";
import jwt_decode from "jwt-decode";
import Navigation from "../components/Navigation";

const HomePage = () => {
    let [notes, setNotes] = useState([]);
    let { authTokens, logoutUser } = useContext(AuthContext);
    let a = jwt_decode(authTokens.access);
    let api = useAxios();

    useEffect(() => {}, []);
    return (
        <div>
            <Navigation />
            <p style={{ minHeight: "200px" }}></p>
        </div>
    );
};

export default HomePage;
