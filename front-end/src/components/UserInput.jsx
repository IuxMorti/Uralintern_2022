import React from 'react';
import classes from "./css/Input.module.css"

function UserInput({type = "text", value, onChange,name, readonly}) {

    return (
        <div>
            <input
                className={classes.input}
                onChange={(e) => onChange({name: name, value: e.target.value})}
                type={type}
                value={value}
                readOnly={readonly}
            />
        </div>
    );
}

export default UserInput;