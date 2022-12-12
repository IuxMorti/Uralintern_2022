import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom/cjs/react-router-dom";
import END_POINTS from "../Auth/EndPoints";
import Navigation from "../components/Navigation";
import TeamUsersList from "../components/TeamUsersList";
import "../css/trainee/styles-command.css";
import useAxios from "../utils/useAxios";

function Team(props) {
    const api = useAxios();
    const { teamId } = useParams();
    const [status, SetStatus] = useState(-1);
    const [team, setTeam] = useState({});

    const getTeam = async () => {
        try {
            const response = await api.get(END_POINTS.API.GET_TEAM + teamId);
            SetStatus(response.status);
            if (response.status === 200) {
                console.log("GetUser");
                setTeam({ ...response.data });
            } else {
                console.log(status);
            }
        } catch {
            console.log(status);
        }
    };

    useEffect(() => {
        getTeam();
    }, []);

    return (
        <div className="main">
            <div class="team">
                <div class="team-info">
                    <h2>{team.title}</h2>
                    <p>
                        Проект: <span>{team?.id_project ?? "нет данных"}</span>
                    </p>
                    <p>
                        Куратор: <span>{team?.id_tutor ?? "нет данных"}</span>
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
                    <TeamUsersList interns={team?.interns} />
                    <button class="give-a-mark">Дать оценку</button>
                    <p class="team-numbers">(2/3/10)</p>
                    <button class="get-report">Отчёт</button>
                </div>
            </div>
            <Navigation />
        </div>
    );
}

export default Team;
