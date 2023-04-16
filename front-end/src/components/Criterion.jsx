import React from 'react';
import RadioButton from './RadioButton';
import classes from './css/Criterion.module.css'
import classNames from 'classnames';
import QuestionMark from './QuestionMark';

function Criterion({nameCriterion, name, onChange, isChecked, info}) {
/*отправляет объект с name и ключом и обновляет*/
    return (
        
        <p className={classNames(classes[".mark-form-p"],classes["criteria"])}>
            
            <QuestionMark               
                tabIndex={0}
                onMouseEnter={() => info({visible:true, name})}
                onMouseLeave={() => info({visible:false, name: null})}
                width="20"
                height="20"
                alt="" />
                {" "}
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