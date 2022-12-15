import React from 'react';

function RadioButton({value, name, onChange, isChecked}) {
    return (
        <label>
            <input
                name={name}
                className="radio-button"
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