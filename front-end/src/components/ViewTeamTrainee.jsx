import React from 'react';
import Navigation from './Navigation';
import TeamUsersList from './TeamUsersList';

function ViewTeamTrainee({team}) {
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
                    <TeamUsersList interns={team?.interns}/>
                    <button class="give-a-mark"><a href={`../form/${team?.id}`}>Дать оценку</a></button>
                    {/* <p class="team-numbers">(2/3/10)</p> */}
                    <button class="get-report">Отчёт</button>
                </div>
            </div>
            <Navigation />
        </div>
    );
}

export default ViewTeamTrainee;