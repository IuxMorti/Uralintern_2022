import React, { useContext } from 'react';
//import END_POINTS from '../Auth/EndPoints';
import AuthContext from '../context/AuthContext';
import "../css/trainee/styles-command.css";

function TeamUser({intern}) {

    const {user} = useContext(AuthContext);
    //const PATH_IMAGE = "../"+ END_POINTS.IMAGE.IMAGE;

    console.log(intern.image);
    return (
    <li class="command-info-person">
                <div>
                    <a href={`/user/${intern.id}`}>
                    <img
                        src={ intern?.image ?? require("../images/profile.svg")
                        .default}
                        width="97"
                        height="110"
                        alt="imageuser"
                    />
                    </a>
                </div>
                <div class="text">
                    {user.user_id === intern.id? "Я": `${intern?.surname} ${intern?.firstname} ${intern?.patronymic}`}
                </div>
                <div class="text">
                    <a href={intern?.vk ?? ""} >ВК</a>
                    <p><a href={intern?.telegram ?? ""}>ТГ</a></p>
                    <p>{intern.email}</p>
                </div>
                <div class="text">
                    {intern?.educational_institution ?? "Учебное заведение"}
                    <p>{intern?.specialization ?? "Специальность"}</p>
                    <p>{intern?.course ?? "Курс"}</p>
                </div>
            </li>
    );
}

export default TeamUser;