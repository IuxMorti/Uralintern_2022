import React from 'react';
import "./css/Navigation.css"

function NavigationRoles({name, users, role}) {
    return (
        <div className="roles">
            <div className="name-role">
                {name}
            </div>
            <div className="name-role-value">
            <ul>
                {users[role]?.map(team => <li><a href={`/team/${team.id}`}>{team.title}</a></li>)}
            </ul>
            </div>
        </div>
    );
}

export default NavigationRoles;