import React from "react";
import { useState, useEffect, useContext } from "react";
import { useParams } from "react-router-dom";
import END_POINTS from "../Auth/EndPoints";
import Navigation from "../components/Navigation";
import UserInput from "../components/UserInput";
import AuthContext from "../context/AuthContext";
import useAxios from "../utils/useAxios";
import FilledForms from "../components/FilledForms";
import classes from "../css/module/user.module.css";
import classNames from "classnames";
import BASE_URL from "../Auth/BaseUrl";
import alertify from "alertifyjs";
import "alertifyjs/build/css/alertify.css";

const User = () => {
    let { userId } = useParams();
    let { user } = useContext(AuthContext);
    let [userData, setUser] = useState({});
    let api = useAxios();
    let [status, SetStatus] = useState(-1);
    let [isCheck, setCheck] = useState(true);
    let [userClone, setClone] = useState({});
    const changeUser = ({ name, value }) => {
        if (!Object.keys(userClone).length) {
            setClone({ ...userData });
        }
        setClone({
            ...userClone,
            [name]: String(value).length !== 0 ? value : null,
        });
        //console.log(userClone);
    };

    const getUser = async () => {
        api.get(END_POINTS.API.GET_USER + userId)
            .then((res) => {
                const data = res.data;
                setUser({
                    ...data,
                });
                setClone({
                    ...data,
                });
            })
            .catch((err) => console.log(err));
    };

    const saveChange = async () => {
        edit();

        api.put(END_POINTS.API.CHANGE_INFO + user.user_id, userClone)
            .then((res) => {
                setUser({ ...userClone });
                alertify.notify("Данные успешно изменены.", "success");
            })
            .catch((err) => {
                if (err.response) {
                    const answer = [];
                    for (let field in err.response.data) {
                        if (field === "telephone")
                            answer.push(`некорректный ввод в поле "Телефон"`);
                        if (field === "vk")
                            answer.push(
                                `некорректный ввод в поле "VK": ссылка должна начинаться с http(s)\\\\:`
                            );
                        if (field === "telegram")
                            answer.push(
                                `некорректный ввод в поле "telegram": ссылка должна начинаться с http(s)\\\\:`
                            );
                        if (field === "educational_institution")
                            answer.push(
                                `некорректный ввод в поле "Учебное заведение"`
                            );
                        if (field === "specialization")
                            answer.push(
                                `некорректный ввод в поле "Специальность"`
                            );
                        if (field === "course")
                            answer.push(`введено слишком большое число`);
                        setClone({ ...userData });
                    }

                    alertify.error(answer.join("\n"), 5);
                } else if (err.request) {
                    alertify.error("you killing me?", 5);
                } else {
                    alertify.error("i don't know", 5);
                }
            });
    };

    const edit = () => setCheck(!isCheck);

    useEffect(() => {
        getUser();
    }, []);

    const updatePhoto = async (photos) => {
        if (!photos) return;
        const formData = new FormData();
        formData.append("image", photos[0], photos[0].name);
        await api
            .put(END_POINTS.API.CHANGE_IMAGE + user.user_id, formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            })
            .then(() => {
                getUser();
                alertify.notify("фото успешно изменено.", "success");
            })
            .catch((err) => alertify.error(err));
    };

    const deletePhoto = async () => {
        await alertify.confirm(
            "uralintern",
            "вы точно хотите удалить фото?",
            () => {
                api.put(END_POINTS.API.CHANGE_IMAGE + user.user_id, {
                    image: null,
                })
                    .then(() => {
                        getUser();
                        alertify.notify("фото успешно удалено.", "success");
                    })
                    .catch((err) => alertify.error(err));
            },
            () => {}
        );
    };

    if (Object.keys(userData).length === 0) {
        return <div style={{ minHeight: "660px" }}>error</div>;
    }
    return (
        <div className={classes.main}>
            <Navigation />
            <div className={classes["profile-info"]}>
                <div className="main-profile">
                    <h2 className={classes["profile-info-h2"]}>Профиль</h2>
                    <div className={classes["img-and-filled-forms"]}>
                        <img
                            className={classes["photo-student"]}
                            src={
                                userData?.image
                                    ? BASE_URL + userData.image
                                    : require("../images/profile.svg").default
                            }
                            width="135"
                            height="135"
                            alt="imageuser"
                        />
                        {userId == user.user_id ? (
                            <FilledForms userId={user.user_id} />
                        ) : (
                            <div></div>
                        )}
                    </div>
                    {user.user_id != userId ? (
                        <div></div>
                    ) : (
                        <div>
                            <label
                                className={classes["input__file-button"]}
                                htmlFor="input__file"
                            >
                                <input
                                    type="file"
                                    accept="image/*"
                                    onChange={(e) =>
                                        updatePhoto(e.target.files)
                                    }
                                    id="input__file"
                                    className={`input ${classes["input__file"]}`}
                                />
                                <span
                                    className={
                                        classes["input__file-button-text"]
                                    }
                                >
                                    Изменить фото
                                </span>
                            </label>

                            <button
                                onClick={() => deletePhoto()}
                                className={classes["change-photo"]}
                            >
                                Удалить фото
                            </button>
                        </div>
                    )}
                    <div className={classes["fio-email"]}>
                        <p className={classes["fio"]}>{`${userData.surname} ${
                            userData.firstname
                        } ${userData.patronymic ?? ""}`}</p>
                        <p className={classes["email"]}>
                            {userData.email ?? "email"}
                        </p>
                    </div>
                </div>
                <h3 className={classes["education-h"]}>Образование: </h3>
                <div
                    className={classNames(
                        "education",
                        classes["grid-container"]
                    )}
                >
                    <div>Учебное заведение:</div>
                    {!isCheck ? (
                        <UserInput
                            onChange={changeUser}
                            name="educational_institution"
                            value={userClone.educational_institution}
                            readonly={isCheck}
                        />
                    ) : (
                        <span className={classes["info"]}>
                            {userClone.educational_institution ?? "нет данных"}
                        </span>
                    )}

                    <div>Специальность: </div>

                    {!isCheck ? (
                        <UserInput
                            onChange={changeUser}
                            name="specialization"
                            value={userClone.specialization}
                            readonly={isCheck}
                        />
                    ) : (
                        <span className={classes["info"]}>
                            {userClone.specialization ?? "нет данных"}
                        </span>
                    )}

                    <div>Курс: </div>
                    {!isCheck ? (
                        <UserInput
                            onChange={changeUser}
                            name="course"
                            type="number"
                            min={1}
                            max={6}
                            value={userClone.course}
                            readonly={isCheck}
                        />
                    ) : (
                        <span className={classes["info"]}>
                            {userClone.course ?? "нет данных"}
                        </span>
                    )}
                </div>
                <h3 className={classes["contact-h"]}>Контакты: </h3>
                <div
                    className={classNames(
                        "contacts",
                        classes["grid-container"]
                    )}
                >
                    <div>Телефон: </div>

                    {!isCheck ? (
                        <UserInput
                            onChange={changeUser}
                            name="telephone"
                            type="tel"
                            value={userClone.telephone}
                            readonly={isCheck}
                            placeholder="+79..."
                        />
                    ) : (
                        <span className={classes["info"]}>
                            {userClone.telephone ?? "нет данных"}
                        </span>
                    )}

                    <div>Ссылка в VK: </div>

                    {!isCheck ? (
                        <UserInput
                            onChange={changeUser}
                            name="vk"
                            type="url"
                            value={userClone.vk}
                            readonly={isCheck}
                            placeholder="http(s)://.."
                        />
                    ) : (
                        <a
                            href={userClone.vk}
                            target="_blank"
                            rel="noreferrer"
                            className={classes["info"]}
                        >
                            {userClone.vk ?? "нет данных"}
                        </a>
                    )}

                    <div>Ссылка в Telegram: </div>

                    {!isCheck ? (
                        <UserInput
                            onChange={changeUser}
                            name="telegram"
                            type="url"
                            value={userClone.telegram}
                            readonly={isCheck}
                            placeholder="http(s)://.."
                        />
                    ) : (
                        <a
                            target="_blank"
                            rel="noreferrer"
                            href={userClone.telegram}
                            className={classes["info"]}
                        >
                            {userClone.telegram ?? "нет данных"}
                        </a>
                    )}

                    {user.user_id != userId ? (
                        <div style={{ "margin-bottom": "110px" }}></div>
                    ) : isCheck ? (
                        <button
                            onClick={edit}
                            className={classes["change-info"]}
                        >
                            Редактировать информацию
                        </button>
                    ) : (
                        <button
                            onClick={saveChange}
                            className={classes["change-info"]}
                        >
                            Сохранить информацию
                        </button>
                    )}
                </div>
            </div>
        </div>
    );
};

export default User;
