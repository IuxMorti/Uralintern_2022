import React from 'react';
import "../css/tutor/team.css";
import Navigation from './Navigation';
import TeamUsersList from './TeamUsersList';
import TutorTeamUserList from './TutorTeamUserList';


function ViewTeamTutor({team}) {
    console.log(team);
    return (
        <div className="main">
            <div class="team">
                <div class="team-info">
                    <h2>{team.title}</h2>
                    <p>
                        Проект: <span>{team?.id_project ?? "нет данных"}</span>
                    </p>
                    <p>
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
                    <p>
                        Командный чат:
                        <span>
                            {" "}
                            {<a href={team?.team_chat}>{team?.team_chat}</a> ??
                                "нет данных"}
                        </span>
                    </p>
                </div>
                <div class="command-info">
                    <TutorTeamUserList interns={team?.interns} team_id={team.id}/>
                </div>
                <div class="buttons">
                <button class="give-a-mark"><a href={`../form/${team?.id}`}>Дать оценку</a></button>
                    {/* <button class="get-stages">Этапы для оценивания</button> */}
                </div>           
                <p class="team-numbers">(2/3/10)</p>
            </div>
            <Navigation />
        </div>
    );
}

export default ViewTeamTutor;