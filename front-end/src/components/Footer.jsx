import React from 'react';
import "./css/footer.css"

function Footer(props) {
    return (
        <div>
        <footer className="main-footer">
        <p className="ural-intern"> © <a href='https://uralintern.ru/'> Уральский центр стажировок, 2022</a></p>
        <div className="VK-link">
            <p>По вопросам можно обращаться сюда:</p>
            <a href='https://vk.com/public167343216'><img src={require('../images/VK.svg').default} width="30" height="30" alt="Vk"/></a>
        </div>
    </footer>
        </div>
    );
}

export default Footer;