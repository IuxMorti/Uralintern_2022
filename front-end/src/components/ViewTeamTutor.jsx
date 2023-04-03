import React from 'react';
import Navigation from './Navigation';
import TutorTeamUserList from './TutorTeamUserList';
import classes from "./css/ViewTeamTutor.module.css"

function ViewTeamTutor({team}) {
    

    //console.log(team);
    return (
        <div className={classes["main"]}>
            <Navigation />
            <div className={classes["team"]}>
                <div className={classes["team-info"]}>
                    <h2 className={classes["team-info-h2"]}>{team.title}</h2>
                    <p className={classes["team-info-p"]}>
                        Проект: <span>{team?.id_project?.title ?? "нет данных"}</span>
                    </p>
                    <p className={classes["team-info-p"]}>
                        Куратор:{" "}
                        <a href={"../user/" + team?.id_tutor?.id.id}>
                            {team["id_tutor"]
                                ? team?.id_tutor.id?.surname +
                                  " " +
                                  team?.id_tutor.id?.firstname +
                                  " " +
                                  (team?.id_tutor.id?.patronymic ?? "")
                                : "Нет данных"}
                        </a>
                    </p>
                    <p className={classes["team-info"]}>
                        Командный чат:
                        <span>
                            {" "}
                            {<a href={team?.team_chat}>{team?.team_chat}</a> ??
                                "нет данных"}
                        </span>
                    </p>
                </div>
                <div className={classes["command-info"]}>
                    <TutorTeamUserList interns={team?.interns} team_id={team.id}/>
                </div>
                <div className={classes["buttons"]}>
                <a href={`../form/${team?.id}`}><button className={classes["give-a-mark"]}>Дать оценку</button></a>
                    {/* <button className="get-stages">Этапы для оценивания</button> */}
                </div>           
                {/* <p className="team-numbers">(2/3/10)</p> */}
            </div>
            
        </div>
    );
}

export default ViewTeamTutor;