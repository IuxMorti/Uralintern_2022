import React from 'react';
import "../css/trainee/styles-command.css";
import TeamUser from './TeamUser';

function TeamUsersList({interns}) {
    return (
        <ul class="main-ul">
        <li class="command-info-person-head">
            <div class="empty"></div>
            <div class="text">ФИО</div>
            <div class="text">Контакты</div>
            <div class="text">Образование</div>
        </li>
        {interns?.map(intern => <TeamUser intern={intern?.id}/>) ?? ""}
    </ul>
    );
}

export default TeamUsersList;