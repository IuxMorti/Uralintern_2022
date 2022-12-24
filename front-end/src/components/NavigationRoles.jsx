import React from 'react';
//import "./css/Navigation.css"
import classes from "./css/Navigation.module.css"


function NavigationRoles({name, users, role}) {
    return (
        <div className={classes["roles"]}>
            
            <div className={classes["name-role"]}>
                {name}
            </div>
            <div className={classes["name-role-value"]}>
            <ul className={classes["roles-ul"]}>
                {users[role]?.map(team => <li><a className={classes["roles-li-p"]} href={`/team/${team.id}`}>{team.title}</a></li>)}
            </ul>
            </div>
        </div>
    );
}

export default NavigationRoles;