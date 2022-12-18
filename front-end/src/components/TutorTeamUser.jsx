import React from 'react';
import TeamTableForm from './TeamTableForm';
import classes from "./css/TutorTeamUserList.module.css"


function TutorTeamUser({intern, team_id}) {

    
    console.log(team_id);
    if(!intern){
        return <div></div>;
    }
    return (
        <li className={classes['command-info-person']}>
        <div className={classes["photo"]}>
            <img 
            src={ intern?.image
                 ?? require("../images/profile.svg").default }
            width="40"
            height="44" 
            alt="фото юзера"/>
        </div>
        <div className={classes["fio"]}>
            {`${intern?.surname} ${intern?.firstname} ${intern?.patronymic}`}
        </div>
                <div className={classes["contacts"]}>
                    <a href={intern?.vk ?? ""} >ВК</a>
                    <p><a href={intern?.telegram ?? ""}>ТГ</a></p>
                    <p>{intern.email}</p>
                </div>
                <div className={classes["education"]}>
                    {intern?.educational_institution ?? "Учебное заведение"}
                    <p>{intern?.specialization ?? "Специальность"}</p>
                    <p>{intern?.course ?? "Курс"}</p>
                </div>
        
        {/* <div className="text forms">2/0/10</div> */}
        <TeamTableForm team_id={team_id} user_id={intern.id}/>
    </li>
    );
}

export default TutorTeamUser;