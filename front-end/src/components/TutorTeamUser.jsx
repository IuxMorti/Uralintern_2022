import React from 'react';
import TeamTableForm from './TeamTableForm';
import classes from "./css/TutorTeamUserList.module.css"
import BASE_URL from '../Auth/BaseUrl';


function TutorTeamUser({intern, team_id}) {
    //console.log(team_id);
    if(!intern){
        return <div></div>;
    }
    return (
        <li className={classes['command-info-person']} style={{"borderBottom":"1px solid rgba(0, 0, 0, 0.2)"}}>
        <div className={classes["photo"]}>
            <img 
            style={{"borderRadius":"50%"}}
            src={intern?.image
                ? BASE_URL + intern.image
                : require("../images/profile.svg").default}
            width="50"
            height="55" 
            alt="фото юзера"/>
        </div>
        <div className={classes["fio"]}>
            <a href={`../user/${intern?.id}`}>{`${intern?.surname ?? ""} ${intern?.firstname ?? ""} ${intern?.patronymic ?? ""}`}</a>
        </div>
            <div className={classes["contacts"]}>
                <a target="_blank" rel="noreferrer"  href={intern?.vk ?? ""} >ВК</a>
                <p><a target="_blank" rel="noreferrer" href={intern?.telegram ?? ""}>ТГ</a></p>
                <p>{intern.email}</p>
            </div>
            <div className={classes["education"]}>
                {intern?.educational_institution ?? "Учебное заведение"}
                <p>{intern?.specialization ?? "Специальность"}</p>
                <p>{intern?.course ?? "Курс"}</p>
            </div>
            <TeamTableForm team_id={team_id} user_id={intern.id}/>
            <div className={classes["link"]}><a className={classes["detailed-report-a"]}  href={`../report/${team_id}/${intern.id}`}>Отчёт</a></div>
    </li>
    );
}

export default TutorTeamUser;