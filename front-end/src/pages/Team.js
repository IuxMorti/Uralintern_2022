import React, { useContext, useEffect, useState } from "react";
import { useParams } from "react-router-dom/cjs/react-router-dom";
import END_POINTS from "../Auth/EndPoints";
import Navigation from "../components/Navigation";
import TeamUsersList from "../components/TeamUsersList";
import ViewTeamTrainee from "../components/ViewTeamTrainee";
import ViewTeamTutor from "../components/ViewTeamTutor";
import AuthContext from "../context/AuthContext";
import useAxios from "../utils/useAxios";

function Team(props) {
    const { user } = useContext(AuthContext);
    const api = useAxios();
    const { teamId } = useParams();
    const [status, SetStatus] = useState(-1);
    const [team, setTeam] = useState({});

    const getTeam = async () => {
        try {
            const response = await api.get(END_POINTS.API.GET_TEAM + teamId);
            SetStatus(response.status);
            if (response.status === 200) {
                setTeam({ ...response.data });
            } else {
                console.log(response.status);
            }
        } catch (e) {
            console.log(e);
        }
    };

    useEffect(() => getTeam(), []);

    if (status !== 200) {
        return <div></div>;
    }

    if (user.user_id == team?.id_tutor?.id.id) {
        console.log("TUTOR");
        return <ViewTeamTutor team={team} />;
    }
    return <ViewTeamTrainee team={team} />;
}

export default Team;
