import React from "react";
import { useState, useEffect, useContext } from "react";
import { useParams } from "react-router-dom";
import END_POINTS from "../Auth/EndPoints";
import Navigation from "../components/Navigation";
import UserInput from "../components/UserInput";
import AuthContext from "../context/AuthContext";
import useAxios from "../utils/useAxios";
//import "../css/trainee/styles-profile.css";
import FilledForms from "../components/FilledForms";
import classes from "../css/module/user.module.css";
import classNames from "classnames";
import BASE_URL from "../Auth/BaseUrl";

const User = () => {
    let { userId } = useParams();
    let { user } = useContext(AuthContext);
    let [userData, setUser] = useState({});
    let api = useAxios();
    let [status, SetStatus] = useState(-1);
    let [isCheck, setCheck] = useState(true);
    let [userClone, setClone] = useState({});
    const [photo, setPhoto] = useState(
        require("../images/profile.svg").default
    );
    const changeUser = ({ name, value }) => {
        if (!Object.keys(userClone).length) {
            setClone({ ...userData });
        }
        setClone({
            ...userClone,
            [name]: String(value).length !== 0 ? value : null,
        });
        console.log(userClone);
    };

    const getUser = async () => {
        try {
            const response = await api.get(END_POINTS.API.GET_USER + userId);
            SetStatus(response.status);
            if (response.status === 200) {
                const data = response.data;
                setUser({ ...data });
                setClone({ ...data });
            } else {
                console.log(status);
            }
        } catch {
            console.log(status);
        }
    };

    const saveChange = () => {
        edit();
        try {
            api.put(END_POINTS.API.CHANGE_INFO + user.user_id, userClone);
        } catch (e) {
            console.log(e);
        }
    };

    const edit = () => setCheck(!isCheck);

    useEffect(() => {
        getUser();
    }, []);

    const getPhoto = async () => {
        if (!userData || !userData?.image) return;
        try {
            console.log(userData.image);
            const response = await api.get(userData.image);
            setPhoto(URL.createObjectURL(response.data));
        } catch (e) {
            console.log(e);
        }
    };

    useEffect(() => {
        getPhoto();
    }, [userData]);

    if (status === -1) {
        return <div>Ошибка</div>;
    }

    return (
        <div className={classes.main}>
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
                        {/* {userId == user.user_id ? (
                            <FilledForms userId={user.user_id} />
                        ) : (
                            <div></div>
                        )} */}
                    </div>
                    {/* {user.user_id == userId ? (
                        <button className={classes["change-photo"]}>
                            Изменить фото
                        </button>
                    ) : (
                        <div></div>
                    )} */}
                    <div className={classes["fio-email"]}>
                        <p
                            className={classes["fio"]}
                        >{`${userData.surname} ${userData.firstname} ${userData.patronymic}`}</p>
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
                    <UserInput
                        onChange={changeUser}
                        name="educational_institution"
                        value={userClone.educational_institution}
                        readonly={isCheck}
                    />
                    <div>Специальность: </div>
                    <UserInput
                        onChange={changeUser}
                        name="specialization"
                        value={userClone.specialization}
                        readonly={isCheck}
                    />
                    <div>Курс: </div>
                    <UserInput
                        onChange={changeUser}
                        name="course"
                        value={userClone.course}
                        readonly={isCheck}
                    />
                </div>
                <h3 className={classes["contact-h"]}>Контакты: </h3>
                <div
                    className={classNames(
                        "contacts",
                        classes["grid-container"]
                    )}
                >
                    <div>Телефон: </div>
                    <UserInput
                        onChange={changeUser}
                        name="telephone"
                        value={userClone.telephone}
                        readonly={isCheck}
                    />
                    <div>Ссылка в VK: </div>
                    <UserInput
                        onChange={changeUser}
                        name="vk"
                        value={userClone.vk}
                        readonly={isCheck}
                    />
                    <div>Ссылка в Telegram: </div>
                    <UserInput
                        onChange={changeUser}
                        name="telegram"
                        value={userClone.telegram}
                        readonly={isCheck}
                    />

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
            <Navigation />
        </div>
    );
};

export default User;
