import React from 'react';
import RadioButton from './RadioButton';

function Criterion({nameCriterion, name, onChange, isChecked}) {
/*отправляет объект с name и ключом и обновляет*/
    return (
        
        <p className="criteria">
            <img
                src={require("../images/question_mark.png").default}
                width="20"
                height="20"
                alt=""
            />{" "}
            {`${nameCriterion}:`}
            <RadioButton name={name} value={-1} onChange={onChange} isChecked={isChecked}/>
            <RadioButton name={name} value={0} onChange={onChange} isChecked={isChecked}/>
            <RadioButton name={name} value={1} onChange={onChange} isChecked={isChecked}/>
            <RadioButton name={name} value={2} onChange={onChange} isChecked={isChecked}/>
            <RadioButton name={name} value={3} onChange={onChange} isChecked={isChecked}/>
        </p>
    );
}

export default Criterion;