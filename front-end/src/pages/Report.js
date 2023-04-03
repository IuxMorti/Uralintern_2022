import React, { useContext, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import END_POINTS from "../Auth/EndPoints";
import Graph from "../components/Graph";
import Navigation from "../components/Navigation";
import useAxios from "../utils/useAxios";
import classes from "../css/module/report.module.css";
import AuthContext from "../context/AuthContext";

function Report() {
    const { user } = useContext(AuthContext);
    const { userId, teamId } = useParams();
    const [estimations, setEstimations] = useState({});
    const api = useAxios();
    const getEstimations = async () => {
        try {
            const response = await api.get(
                END_POINTS.API.GET_ESTIMATIONS + userId + "/" + teamId
            );
            const data = response.data;
            setEstimations(data);
        } catch (e) {
            setEstimations({
                total_estimation: {
                    competence1: -1,
                    competence2: -1,
                    competence3: -1,
                    competence4: -1,
                },

                self_estimation: {
                    competence1: -1,
                    competence2: -1,
                    competence3: -1,
                    competence4: -1,
                },

                team_estimation: {
                    competence1: -1,
                    competence2: -1,
                    competence3: -1,
                    competence4: -1,
                },
            });
        }
    };

    useEffect(() => {
        getEstimations();
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    function getValue(name) {
        const result = [];
        result.push(estimations[name]?.competence1?.toFixed(2));
        result.push(estimations[name]?.competence2?.toFixed(2));
        result.push(estimations[name]?.competence3?.toFixed(2));
        result.push(estimations[name]?.competence4?.toFixed(2));
        return result;
    }

    if (Object.keys(estimations).length === 0) {
        return <div></div>;
    }

    return (
        <div className={classes["main"]}>
            <Navigation />
            <div className={classes["report-info"]}>
                <h1 className={classes["report-info-h1"]}>Отчёты</h1>
                <h2 className={classes["report-info-h2"]}>Общая</h2>
                <Graph legend="Общая" values={getValue("total_estimation")} />
                <h2 className={classes["report-info-h2"]}>Самооценка</h2>
                <Graph
                    legend="Самооценка"
                    values={getValue("self_estimation")}
                />
                <h2 className={classes["report-info-h2"]}>Оценка команды</h2>
                <Graph
                    legend="Оценка команды"
                    values={getValue("team_estimation")}
                />
            </div>
        </div>
    );
}

export default Report;
