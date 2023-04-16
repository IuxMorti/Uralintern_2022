import React, { useContext, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import END_POINTS from "../Auth/EndPoints";
import AuthContext from "../context/AuthContext";
import useAxios from "../utils/useAxios";
import classes from "../css/module/form.module.css";
import classNames from "classnames";
import Navigation from "../components/Navigation";
import Criterion from "../components/Criterion";
import alertify from "alertifyjs";
import "alertifyjs/build/css/alertify.css";
import { render } from "@testing-library/react";
import {
    DescriptionInvolvement,
    DescriptionCommand,
    DescriptionLearnability,
    DescriptionOrganization,
} from "../components/Descriptions";

function AssessmentPage(props) {
    const estimations = {};
    const descriptions = {
        competence1: <DescriptionInvolvement />,
        competence2: <DescriptionOrganization />,
        competence3: <DescriptionLearnability />,
        competence4: <DescriptionCommand />,
    };
    const [pageState, setPageState] = useState({});
    let team = {};
    let stages = [];
    const api = useAxios();
    const { user } = useContext(AuthContext);

    let { teamId } = useParams();
    teamId = Number(teamId);

    let currentStage = {};
    const estimation = {};

    const [description, setDescription] = useState({
        visible: false,
        name: null,
    });

    const changeDescription = (description) => {
        setDescription(...description);
    };

    const getEstimations = async () => {
        api.get(END_POINTS.API.GET_TEAM + teamId)
            .then(async (res) => {
                team = res.data;
                api.get(END_POINTS.API.GET_STAGE + teamId)
                    .then(async (res) => {
                        stages = res.data;
                        for (let stage of res.data) {
                            await api
                                .get(
                                    END_POINTS.API.GET_ESTIMATION +
                                        `${user.user_id}/${teamId}/${stage.id}`
                                )
                                .then((res) => {
                                    const stageId = stage.id;
                                    estimations[stageId] = {};
                                    for (let estimate of res.data) {
                                        estimations[stageId][
                                            estimate.id_intern
                                        ] = estimate;
                                    }
                                })
                                .catch((err) =>
                                    alertify.error("обновите страницу")
                                );
                        }
                        return { stages, estimations };
                    })
                    .finally(() => {
                        if (stages.length === 0) return;
                        const stage = stages[0];
                        if (
                            !(
                                team?.interns[0]?.id?.id &&
                                team?.interns[0]?.id?.id in
                                    estimations[stage.id]
                            )
                        ) {
                            setPageState({
                                estimation: {
                                    id_appraiser: user.user_id,
                                    customer_role:
                                        team.id_tutor.id.id === user.user_id
                                            ? "Куратор"
                                            : "Стажёр",
                                    id_project: team.id_project.id,
                                    id_team: teamId,
                                    id_stage: stage.id,
                                    id_intern: team?.interns[0]?.id?.id,
                                    competence1: -1,
                                    competence2: -1,
                                    competence3: -1,
                                    competence4: -1,
                                },
                                team: team,
                                currentStage: stage,
                                stages: stages,
                                estimations: estimations,
                            });
                        } else {
                            setPageState({
                                estimation: {
                                    ...estimations[stage.id][
                                        team?.interns[0]?.id?.id
                                    ],
                                },
                                team: team,
                                currentStage: stage,
                                stages: stages,
                                estimations: estimations,
                            });
                        }
                    })
                    .catch((err) => alertify.error("обновите страницу"));
            })
            .catch((err) => alertify.error("обновите страницу"));
    };

    const isChecked = (name, value) => {
        return pageState.estimation[name] == value;
    };

    const changeStage = (id) => {
        for (let i = 0; i < pageState.stages.length; i++) {
            if (pageState.stages[i].id == id) {
                const id_intern = pageState.estimation.id_intern;
                setPageState({
                    ...pageState,
                    currentStage: pageState.stages[i],
                    estimation:
                        id_intern in
                        pageState.estimations[pageState.stages[i].id]
                            ? {
                                  ...pageState.estimations[
                                      pageState.stages[i].id
                                  ][id_intern],
                              }
                            : {
                                  id_appraiser: user.user_id,
                                  customer_role:
                                      pageState.team?.id_tutor?.id?.id ===
                                      user.user_id
                                          ? "Куратор"
                                          : "Стажёр",
                                  id_project: pageState.team.id_project.id,
                                  id_team: teamId,
                                  id_stage: pageState.stages[i].id,
                                  id_intern: pageState.estimation.id_intern,
                                  competence1: -1,
                                  competence2: -1,
                                  competence3: -1,
                                  competence4: -1,
                              },
                });
                break;
            }
        }
    };

    const changeAssessedPerson = (id) => {
        id = Number(id);
        if (id in pageState.estimations[pageState.currentStage.id]) {
            setPageState({
                ...pageState,
                estimation:
                    pageState.estimations[pageState.currentStage.id][id],
            });
        } else {
            setPageState({
                ...pageState,
                estimation: {
                    id_appraiser: user.user_id,
                    customer_role:
                        pageState.team.id_tutor.id.id === user.user_id
                            ? "Куратор"
                            : "Стажёр",
                    id_project: pageState.team.id_project.id,
                    id_team: teamId,
                    id_stage: pageState.currentStage.id,
                    id_intern: id,
                    competence1: -1,
                    competence2: -1,
                    competence3: -1,
                    competence4: -1,
                },
            });
        }
    };

    const changeValue = (name, value) => {
        setPageState({
            ...pageState,
            estimation: { ...pageState.estimation, [name]: value },
        });
    };

    const check = (id) => {
        return id in pageState.estimations[pageState.currentStage.id]
            ? " ✔"
            : "";
    };

    const checkStage = (id) => {
        console.log(pageState.estimations[id]);
        console.log(pageState.team.interns);
        console.log(Object.keys(pageState.estimations[id]));
        console.log(pageState.team.interns.length);
        return Object.keys(pageState.estimations[id]).length ===
            pageState.team.interns.length
            ? " ✔"
            : "";
    };

    const submit = (e) => {
        e.preventDefault();
        api.post(END_POINTS.API.ESTIMATE, pageState.estimation)
            .then((res) => {
                alertify.notify("оценка успешно отправлена", "success");
                pageState.estimations[pageState.currentStage.id][
                    pageState.estimation.id_intern
                ] = pageState.estimation;
                setPageState({ ...pageState });
            })
            .catch(() =>
                alertify.error(
                    "не получилось отправить оценку, повторите попытку"
                )
            );
    };

    useEffect(() => getEstimations(), []);

    if (!("team" in pageState))
        return <div style={{ minHeight: "660px" }}>wait</div>;
    return (
        <div className={classes["forms-main"]}>
            <Navigation />

            <div className={classes["forms"]}>
                <h2 className={classes["forms-h2"]}>Форма оценки</h2>
                <p
                    className={classNames(
                        "info",
                        classes["forms-p"],
                        classes["command"]
                    )}
                >
                    Команда:{" "}
                    <a href={`../team/${pageState.team.id}`}>
                        {pageState.team.title}
                    </a>
                </p>
                <p
                    className={classNames(
                        "info",
                        classes["forms-p"],
                        classes["numbers"]
                    )}
                ></p>
                <form className="mark-form" onSubmit={submit}>
                    <label>
                        <span className={classes["span"]}>Выберите этап:</span>
                        <select
                            className={classes["form-selector"]}
                            name="form-selector"
                            onChange={(e) => changeStage(e.target.value)}
                        >
                            {pageState.stages.map((stage) => (
                                <option
                                    value={stage.id}
                                    selected={
                                        stage.id ==
                                        pageState.estimation.id_stage
                                    }
                                >
                                    {stage.title + checkStage(stage.id)}
                                </option>
                            ))}
                        </select>
                    </label>
                    <br />
                    <label>
                        <span className={classes["span"]}>
                            Выберите стажёра:
                        </span>
                        <select
                            className={classes["form-selector"]}
                            onChange={(e) =>
                                changeAssessedPerson(e.target.value)
                            }
                            name="form-selector"
                        >
                            {pageState.team?.interns?.map((intern) => (
                                <option
                                    value={intern.id.id}
                                    selected={
                                        intern.id.id ===
                                        pageState.estimation.id_intern
                                    }
                                >
                                    {`${intern.id?.surname} ${
                                        intern.id?.firstname
                                    } ${intern.id?.patronymic ?? " "}` +
                                        check(intern.id.id)}
                                </option>
                            ))}
                        </select>
                    </label>

                    <Criterion
                        info={setDescription}
                        nameCriterion="Вовлеченность"
                        name="competence1"
                        onChange={changeValue}
                        isChecked={isChecked}
                    />
                    <Criterion
                        info={setDescription}
                        nameCriterion="Организованность"
                        name="competence2"
                        onChange={changeValue}
                        isChecked={isChecked}
                    />
                    <Criterion
                        info={setDescription}
                        nameCriterion="Обучаемость"
                        name="competence3"
                        onChange={changeValue}
                        isChecked={isChecked}
                    />
                    <Criterion
                        info={setDescription}
                        nameCriterion="Командность"
                        name="competence4"
                        onChange={changeValue}
                        isChecked={isChecked}
                    />

                    <input
                        type="submit"
                        className={classes["give-a-mark"]}
                        value="Отправить"
                    />
                </form>
            </div>
            <div>
                {description.visible ? (
                    descriptions[description.name]
                ) : (
                    <div></div>
                )}
            </div>
        </div>
    );
}

export default AssessmentPage;
