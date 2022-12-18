import React from 'react';

function RadioButton({value, name, onChange, isChecked}) {

    const style ={
        background: "#FFFFFF",
        border: "2px solid #F57C00",
    };

    return (
        <label>
            <input
                name={name}
                className={style}
                type="radio"
                value={value}
                checked ={isChecked(name, value)}
                onChange={(e) => onChange(name, e.target.value)}
            />
            {value}
        </label>
    );
}

export default RadioButton;