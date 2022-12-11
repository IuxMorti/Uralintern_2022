import React, { useContext, useEffect, useState } from 'react';
import END_POINTS from '../Auth/EndPoints';
import AuthContext from '../context/AuthContext';
import useAxios from '../utils/useAxios';
import "../css/trainee/styles-command.css"
import NavigationRoles from './NavigationRoles';


function Navigation(props) {
    let { user } = useContext(AuthContext);
    let [status, SetStatus] = useState(-1);
    const api = useAxios();

    const [teamsDate, setTeams] = useState({});

    const getTeams = async () => {
        try {
            const response = await api.get(END_POINTS.API.GET_TEAMS + user.user_id);
            SetStatus(response.status);
            if (response.status === 200) {
                let data = response.data;
                console.log("GettedTeams");
                setTeams({...data});
                console.log(END_POINTS.API.GET_TEAMS + user.user_id)
                console.log(teamsDate);
                console.log(data)
            } else {
                console.log(status);
            }
        } catch {
            console.log(status);
        }
    };
    useEffect(() => {
        getTeams();
    }, []);

    return (
        <div className="navigation">
        <div className="black">
            <h2>Навигация</h2>
        </div>
        <div className="white"></div>
        {user.role_director? <NavigationRoles role="" name="Руководитель" users={[]}/>: ""}
        {user.role_tutor? <NavigationRoles role="tutor" users={teamsDate} name="Куратор"/>: ""}
        {user.role_intern ? <NavigationRoles role="intern" users={teamsDate} name="Стажёр"/>:""}
        <div className="black-bottom"></div>
    </div>
    );
}

export default Navigation;