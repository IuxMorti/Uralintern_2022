import React from 'react';
import TutorTeamUser from './TutorTeamUser';

function TutorTeamUserList({interns, team_id}) {
    console.log(team_id, "TutorTeamUserList -> TutorTeamUser");
    return (
<div class="command-info">
                <ul class="main-ul">
                    <li class='command-info-person-head'>
                        
                            <div class="empty photo"></div>
                            <div class="text fio">ФИО</div>
                            <div class="text contacts">Контакты</div>
                            <div class="text education">Образование</div>
                            <div class="text forms">Формы</div>
                            <div class="text table">Отчёт</div>
                    </li>
                    {interns.map(intern => <TutorTeamUser intern={intern.id} team_id={team_id}/>)}
                </ul>
            </div>
    );
}

export default TutorTeamUserList;