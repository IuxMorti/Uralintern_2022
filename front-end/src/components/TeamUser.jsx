import React, { useContext } from 'react';
//import END_POINTS from '../Auth/EndPoints';
import AuthContext from '../context/AuthContext';
import classes from "./css/TeamUser.module.css"


function TeamUser({intern}) {

    const {user} = useContext(AuthContext);
    //const PATH_IMAGE = "../"+ END_POINTS.IMAGE.IMAGE;

    console.log(intern.image);
    return (
    <li className={classes["command-info-person"]}>
                <div>
                    <img
                        src={ intern?.image ?? require("../images/profile.svg")
                        .default}
                        width="79"
                        height="90"
                        alt="imageuser"
                    />
                </div>
                <div className={classes["text"]}>
                <a href={`/user/${intern.id}`}>
                    {user.user_id === intern.id? "Я": `${intern?.surname} ${intern?.firstname} ${intern?.patronymic}`}
                </a>
                </div>
                <div className={classes["text"]}>
                    <a href={intern?.vk ?? ""} >ВК</a>
                    <p><a href={intern?.telegram ?? ""}>ТГ</a></p>
                    <p>{intern.email}</p>
                </div>
                <div className={classes["text"]}>
                    {intern?.educational_institution ?? "Учебное заведение"}
                    <p>{intern?.specialization ?? "Специальность"}</p>
                    <p>{intern?.course ?? "Курс"}</p>
                </div>
            </li>
    );
}

export default TeamUser;