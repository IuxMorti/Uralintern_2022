import React, { useContext } from 'react';
import AuthContext from '../context/AuthContext';
import Navigation from './Navigation';
import TeamUsersList from './TeamUsersList';
import classes from "./css/ViewTeamTrainee.module.css"


function ViewTeamTrainee({team}) {
    const {user} = useContext(AuthContext);
    return (
        <div className={classes["main"]}>
            <div className={classes["team"]}>
                <div className={classes["team-info"]}>
                    <h2 className={classes["team-info-h2"]}>{team.title}</h2>
                    <p className={classes["team-info-p"]}>
                        Проект: <span>{team?.id_project ?? "нет данных"}</span>
                    </p>
                    <p className={classes["team-info-p"]}>
                        Куратор:{" "}
                        <a href={"../user/" + team?.id_tutor?.id.id}>
                            {team["id_tutor"]
                                ? team?.id_tutor.id?.surname +
                                  " " +
                                  team?.id_tutor.id?.firstname +
                                  " " +
                                  team?.id_tutor.id?.patronymic
                                : "Нет данных"}
                        </a>
                    </p>
                    <p className={classes["team-info-p"]}>
                        Командный чат:
                        <span>
                            {" "}
                            {<a href={team?.team_chat}>{team?.team_chat}</a> ??
                                "нет данных"}
                        </span>
                    </p>
                </div>
                <div className={classes["command-info"]}>
                    <TeamUsersList interns={team?.interns}/>
                    <a href={`../form/${team?.id}`}><button className={classes["give-a-mark"]}>Дать оценку</button></a>
                    {/* <p className="team-numbers">(2/3/10)</p> */}
                    <a href={`../report/${team?.id}/${user.user_id}`}><button className={classes["get-report"]}>Отчёт</button></a>
                </div>
            </div>
            <Navigation />
        </div>
    );
}

export default ViewTeamTrainee;