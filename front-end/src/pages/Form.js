import React, { useContext, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import END_POINTS from "../Auth/EndPoints";
import Criterion from "../components/Criterion";
import Navigation from "../components/Navigation";
import AuthContext from "../context/AuthContext";
import "../css/tutor/forms.css";
import useAxios from "../utils/useAxios";

function Form(props) {
    const { user } = useContext(AuthContext);
    const { teamId } = useParams();
    const [team, setTeam] = useState({});
    const [stages, setStages] = useState([]);
    const api = useAxios();
    const [estimation, setEstimation] = useState({
        id_appraiser: user.user_id,
        customer_role: "Стажёр",
        id_project: 1,
        id_team: teamId,
        id_stage: null,
        id_intern: user.user_id,
        competence1: -1,
        competence2: -1,
        competence3: -1,
        competence4: -1,
    });

    const getStages = async () => {
        try {
            const response = await api.get(END_POINTS.API.GET_STAGE + teamId);
            if (response.status === 200) {
                const data = response.data;
                setStages(data);
                console.log(data);
            } else {
                console.log(response.status);
            }
        } catch (e) {
            console.log(e);
        }
    };

    const getTeam = async () => {
        try {
            const response = await api.get(END_POINTS.API.GET_TEAM + teamId);
            if (response.status === 200) {
                const data = response.data;
                setTeam({ ...data });
                console.log(data);
            } else {
                console.log(response.status);
            }
        } catch (e) {
            console.log(e);
        }
    };

    useEffect(() => {
        getStages();
        getTeam();
    }, []);

    useEffect(() => {
        const role = team.id_tutor === user.user_id ? "Куратор" : "Стажёр";
        setEstimation({
            ...estimation,
            customer_role: role,
            id_stage: stages[0]?.id ?? 1,
        });
    }, [team, stages]);

    const onChange = (name, value) => {
        setEstimation({ ...estimation, [name]: value });
        console.log({ ...estimation, [name]: value });
    };

    const isChecked = (name, value) => {
        return estimation[name] == value;
    };

    const submit = (e) => {
        e.preventDefault();
        try {
            const response = api.post(END_POINTS.API.ESTIMATE, estimation);
            response.then(alert("OK"));
        } catch (e) {
            alert(e);
        }
    };

    if (!team || !stages.length || Object(team).keys?.length === 0) {
        return <div></div>;
    }
    return (
        <div className="forms-main">
            <div className="hint">
                <p>
                    Соблюдение сроков. Вовремя приходит на мероприятия.
                    Соблюдение правил работы, требований. Держит слово
                    <br />
                    <br />
                    Значения шкалы
                    <br />
                    <br />
                    (-1): Сроки не соблюдаются. Требования, правила нарушаются.
                    (0): не выявлен или регулярные задержки, предупреждает о
                    них. (1): качество выражено, в целом человека можно назвать
                    организованным, соблюдающим правила. (2): хорошо
                    проявляется. Умеет планировать свою работу и придерживаться
                    плана. Сложную задачу декомпозирует на отдельные
                    мероприятия. (3) : ----
                </p>
            </div>
            <div className="forms">
                <h2>Форма оценки</h2>
                <p className="info command">
                    Команда: <a href={`../team/${team.id}`}>{team.title}</a>
                </p>
                <p className="info numbers">(2/3/10)</p>
                <form className="mark-form" onSubmit={submit}>
                    <label>
                        <span>Выберите этап:</span>
                        <select
                            className="form-selector"
                            name="form-selector"
                            onChange={(e) =>
                                onChange("id_stage", e.target.value)
                            }
                        >
                            {stages.map((stage) => (
                                <option
                                    value={stage.id}
                                    selected={stage.id == estimation.id_stage}
                                >
                                    {stage.title}
                                </option>
                            ))}
                        </select>
                    </label>
                    <br />
                    <label>
                        <span>Выберите стажёра:</span>
                        <select
                            className="form-selector"
                            onChange={(e) =>
                                onChange("id_intern", e.target.value)
                            }
                            name="form-selector"
                        >
                            {team?.interns?.map((intern) => (
                                <option
                                    value={intern.id.id}
                                    selected={
                                        intern.id.id == estimation.id_intern
                                    }
                                >
                                    {`${intern.id?.surname} ${intern.id?.firstname} ${intern.id?.patronymic}`}
                                </option>
                            ))}
                        </select>
                    </label>

                    <Criterion
                        nameCriterion="Командность"
                        name="competence1"
                        onChange={onChange}
                        isChecked={isChecked}
                    />
                    <Criterion
                        nameCriterion="Обучаемость"
                        name="competence2"
                        onChange={onChange}
                        isChecked={isChecked}
                    />
                    <Criterion
                        nameCriterion="Организованность"
                        name="competence3"
                        onChange={onChange}
                        isChecked={isChecked}
                    />
                    <Criterion
                        nameCriterion="Вовлеченность"
                        name="competence4"
                        onChange={onChange}
                        isChecked={isChecked}
                    />

                    <input type="submit" className="give-a-mark" />
                </form>
            </div>
            <Navigation />
        </div>
    );
}

export default Form;
