import React from 'react';
import TeamTableForm from './TeamTableForm';

function TutorTeamUser({intern, team_id}) {

    
    console.log(team_id);
    if(!intern){
        return <div></div>;
    }
    return (
        <li className='command-info-person'>
        <div className="photo">
            <img 
            src={ intern?.image
                 ?? require("../images/profile.svg").default }
            width="40"
            height="44" 
            alt="фото юзера"/>
        </div>
        <div className="text fio">
            {`${intern?.surname} ${intern?.firstname} ${intern?.patronymic}`}
        </div>
                <div className="text contacts">
                    <a href={intern?.vk ?? ""} >ВК</a>
                    <p><a href={intern?.telegram ?? ""}>ТГ</a></p>
                    <p>{intern.email}</p>
                </div>
                <div className="text education">
                    {intern?.educational_institution ?? "Учебное заведение"}
                    <p>{intern?.specialization ?? "Специальность"}</p>
                    <p>{intern?.course ?? "Курс"}</p>
                </div>
        
        <div className="text forms">2/0/10</div>
        <TeamTableForm team_id={team_id} user_id={intern.id}/>
    </li>
    );
}

export default TutorTeamUser;