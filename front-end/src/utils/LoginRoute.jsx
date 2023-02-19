import React from 'react';
import { Route, Redirect } from "react-router-dom";
import { useContext } from "react";
import AuthContext from "../context/AuthContext";

function LoginRoute({children, ...rest}) {
    const {user} = useContext(AuthContext);
    console.log(user);
    return (
        <Route {...rest}>{!user ? <Redirect to={`../login`} /> : <Redirect to={`../user/${user.user_id}`} />}</Route>
    );
}

export default LoginRoute;