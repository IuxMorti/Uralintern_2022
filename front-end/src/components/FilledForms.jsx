import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import END_POINTS from '../Auth/EndPoints';
import useAxios from '../utils/useAxios';
import classes from "./css/FilledForms.module.css"
function FilledForms({userId}) {
    const api = useAxios();
    const [form, setForm] = useState({});
    const getForm = async () =>{
            api.get(END_POINTS.API.GET_FORMS + userId)
            .then((res) => {
                const data = res.data;
                //console.log(data);
                setForm({...data});
            }).catch((err) => console.log(err));

    }
    useEffect(() => {
        getForm();
    }, []);


    return (
        <div className={classes["cloud"]}>
        <p className={classes["filled-forms"]}>
            Заполненные формы:
        </p>
        <p className={classes["filled-forms-count"]}>
            {(form.estimated ?? "0") + "/" + (form.total ?? "0")}
        </p>
    </div>
    );
}

export default FilledForms;