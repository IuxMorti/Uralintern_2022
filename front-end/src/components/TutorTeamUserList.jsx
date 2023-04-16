import React from 'react';
import TutorTeamUser from './TutorTeamUser';
import classes from "./css/TutorTeamUserList.module.css"
import classNames from 'classnames';

function TutorTeamUserList({interns, team_id}) {
    //console.log(team_id, "TutorTeamUserList -> TutorTeamUser");
    return (
<div className="command-info">
                <ul className={classes["team-ul"]}>
                    <li className={classes['command-info-person-head']}>
                        
                            <div className={classes["photo"]}></div>
                            <div className={classes["fio"]}>ФИО</div>
                            <div className={classes["contacts"]}>Контакты</div>
                            <div className={classes["education"]}>Образование</div>
                            <div className={classNames(classes["text"], 
                                classes["table"])}>Краткий отчёт</div>
                            <div className={classes["link"]}>Полный отчёт</div>
                    </li>
                    {interns.map(intern => <TutorTeamUser intern={intern.id} team_id={team_id}/>)}
                </ul>
            </div>
    );
}

export default TutorTeamUserList;