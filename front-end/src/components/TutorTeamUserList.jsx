import React from 'react';
import TutorTeamUser from './TutorTeamUser';
import classes from "./css/TutorTeamUserList.module.css"
import classNames from 'classnames';

function TutorTeamUserList({interns, team_id}) {
    console.log(team_id, "TutorTeamUserList -> TutorTeamUser");
    return (
<div class="command-info">
                <ul class={classes["team-ul"]}>
                    <li class={classes['command-info-person-head']}>
                        
                            <div class={classes["photo"]}></div>
                            <div class={classes["fio"]}>ФИО</div>
                            <div class={classes["contacts"]}>Контакты</div>
                            <div class={classes["education"]}>Образование</div>
                            {/* <div class="text forms">Формы</div> */}
                            <div class={classNames(classes["text"], 
                                classes["table"])}>Отчёт</div>
                    </li>
                    {interns.map(intern => <TutorTeamUser intern={intern.id} team_id={team_id}/>)}
                </ul>
            </div>
    );
}

export default TutorTeamUserList;