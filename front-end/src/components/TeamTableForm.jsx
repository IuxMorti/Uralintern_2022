import React, { useState, useEffect } from 'react';
import END_POINTS from '../Auth/EndPoints';
import useAxios from '../utils/useAxios';
import classes from "./css/TableForm.module.css"

function TeamTableForm({team_id, user_id}) {
    console.log(team_id);
    const api = useAxios();
    const [status,SetStatus] = useState(0);
    const [form, setForm] = useState({});

    const getEstimations = async () => {
        try {
            const response = await api.get(END_POINTS.API.GET_ESTIMATIONS + `${user_id}/${team_id}`);
            SetStatus(response.status);
            if (response.status === 200) {
                const data = response.data.total_estimation;
                setForm({ ...data });
            } else {
                console.log(response.status);
            }
        } catch(e) {
            console.log("TABBLE ERROR");
        }
    };
    useEffect(() => {
        getEstimations();

    }, [team_id, user_id]);


    if(status === 0){
        
        <table>
        <tr>
            <th>Обучаемость</th>
            <th>Командность</th>
            <th>Вовлечённость</th>
            <th>Организованность</th></tr>
        <tr>
            <td>{"0"}</td>
            <td>{"0"}</td>
            <td>{"0"}</td>
            <td>{"0"}</td>
            </tr> 
    </table>
    }

    return (
        <div className={classes["text-table"]}>
            <table className={classes["table"]}>
                <tr>
                    <th className={classes["th"]}>Обучаемость</th>
                    <th className={classes["th"]}>Командность</th>
                    <th className={classes["th"]}>Вовлечённость</th>
                    <th className={classes["th"]}>Организованность</th>
                </tr>
                <tr>
                    <td className={classes["td"]}>{form.competence1?.toFixed(2) ?? "N"}</td>
                    <td className={classes["td"]}>{form.competence2?.toFixed(2) ?? "N"}</td>
                    <td className={classes["td"]}>{form.competence3?.toFixed(2) ?? "N"}</td>
                    <td className={classes["td"]}>{form.competence4?.toFixed(2) ?? "N"}</td>
                </tr> 
            </table>
        </div> 
    );
}

export default TeamTableForm;