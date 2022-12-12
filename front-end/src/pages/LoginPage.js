import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";
const LoginPage = () => {
    let { loginUser } = useContext(AuthContext);
    console.log(loginUser);
    return (
        <div className="body">
            <main className="main">
                <h2 className="welcome-phrase">Добро пожаловать!</h2>
                <div className="content">
                    <div className="welcome-content">
                        <img
                            src="images/logo_big.png"
                            width="453"
                            height="358"
                            alt="Логотип"
                        />
                        <p>
                            Личный кабинет uralintern.ru - средство учёта и
                            контроля, позволяющее отслеживать и оценивать вклад
                            каждого участника в командный проект, выполняемый во
                            время прохождения стажировки.
                        </p>
                    </div>
                    <div className="authentication">
                        <h3>Вход в систему</h3>
                        <form
                            onSubmit={loginUser}
                            className="log-to-account"
                            action=""
                            method="post"
                        >
                            <input
                                className="log-to-account-input login"
                                type="text"
                                name="username"
                                aria-label="Логин"
                                placeholder="Логин"
                                required
                            />
                            <br />
                            <input
                                className="log-to-account-input password"
                                type="password"
                                name="password"
                                aria-label="Пароль"
                                placeholder="Пароль"
                                required
                            />
                            <br />
                            <button
                                className="log-to-account-button"
                                type="submit"
                            >
                                Войти
                            </button>
                        </form>
                    </div>
                </div>
            </main>
        </div>
    );
};

export default LoginPage;
