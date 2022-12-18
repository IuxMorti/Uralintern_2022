import React from 'react';
import TeamUser from './TeamUser';
import classes from "./css/TeamUsersList.module.css"

function TeamUsersList({interns}) {
    return (
        <ul className={classes["team-ul"]}>
        <li className={classes["command-info-person-head"]}>
            <div className={classes["empty-head"]}></div>
            <div className={classes["text-head"]}>ФИО</div>
            <div className={classes["text-head"]}>Контакты</div>
            <div className={classes["text-head"]}>Образование</div>
        </li>
        {interns?.map(intern => <TeamUser intern={intern?.id}/>) ?? ""}
    </ul>
    );
}

export default TeamUsersList;