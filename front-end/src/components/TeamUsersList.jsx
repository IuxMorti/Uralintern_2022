import React from 'react';
import TeamUser from './TeamUser';
import classes from "./css/TeamUsersList.module.css"

function TeamUsersList({interns}) {
    return (
        <ul className={classes["team-ul"]}>
        <li className={classes["command-info-person-head"]}>
            <div className={classes["empty-head"]}></div>
            <div className={classes["text-head-fio"]}>ФИО</div>
            <div className={classes["text-head"]}>Контакты</div>
            <div className={classes["text-head"]}>Образование</div>
        </li>
        <div style={{marginLeft:"95px"}}>
        {interns?.map(intern => <TeamUser intern={intern?.id}/>) ?? ""}
        </div>
    </ul>
    );
}

export default TeamUsersList;