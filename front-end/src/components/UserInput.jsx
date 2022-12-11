import React from 'react';

function UserInput({type = "text", value, onChange,name, readonly}) {

    return (
        <div>
            <input
                onChange={(e) => onChange({name: name, value: e.target.value})}
                type={type}
                value={value}
                readOnly={readonly}
            />
        </div>
    );
}

export default UserInput;