import React, { useContext, useEffect, useState } from 'react';
import END_POINTS from '../Auth/EndPoints';
import AuthContext from '../context/AuthContext';
import useAxios from '../utils/useAxios';
import NavigationRoles from './NavigationRoles';
import classes from "./css/Navigation.module.css"

function Navigation(props) {
    let { user } = useContext(AuthContext);
    const api = useAxios();

    const [teamsDate, setTeams] = useState({});

    const getTeams = async () => {

            api.get(END_POINTS.API.GET_TEAMS + user.user_id)
            .then(res => {
                console.log("GettedTeams");
                setTeams({...res.data})
            })
            .catch(err => console.log(err));
    };
    useEffect(() => {
        getTeams();
    }, []);
    return (
        <div className={classes["navigation"]}>
        <label className={classes["back"]} onClick={() => window.history.back(1)}>
        <img src={require("../images/arrowleft_icon.svg").default} width="15" alt=""  />
        вернуться
        </label>
        {user.role_director? <NavigationRoles role="" name="Руководитель" users={[]}/>: ""}
        {user.role_tutor? <NavigationRoles role="tutor" users={teamsDate} name="Я-Куратор"/>: ""}
        {user.role_intern ? <NavigationRoles role="intern" users={teamsDate} name="Я-Стажёр"/>:""}

    </div>
    );
}

export default Navigation;