import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import END_POINTS from '../Auth/EndPoints';
import useAxios from '../utils/useAxios';

function FilledForms({userId}) {
    const api = useAxios();
    const [status, SetStatus] = useState(-1);
    const [form, setForm] = useState({});
    const getForm = async () =>{
        try{
            const response = await api.get(END_POINTS.API.GET_FORMS + userId);
            SetStatus(response.status);
            if (status === 200) {
                const data = response.data;
                console.log(data); 
                setForm({ ...data });
            } else {
                console.log(response.status);
            }
        }
        catch(e){
            console.log(e);
        }
    }

    if(!Object.keys(form).length){
        getForm();
        return (<div></div>)
    }
    return (
        <div className="cloud">
        <p className="filled-forms">
            Заполненные формы:
        </p>
        <p className="filled-forms-count">
            {form["estimated"] + "/" + form["total"]}
        </p>
    </div>
    );
}

export default FilledForms;