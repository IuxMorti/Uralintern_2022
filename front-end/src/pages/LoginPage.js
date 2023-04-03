import classNames from "classnames";
import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";
import classes from "../css/module/auth.module.css";

const LoginPage = () => {
    let { loginUser, user } = useContext(AuthContext);
    return (
        <div className={classes.main}>
            <h2 className={classes["welcome-phrase"]}>Добро пожаловать!</h2>
            <div className={classes["content"]}>
                <div className="welcome-content">
                    <img
                        className={classes["welcome-content-img"]}
                        src={require("../images/logo_big.png").default}
                        width="453"
                        height="358"
                        alt="Логотип"
                    />
                    <p className={classes["welcome-content-p"]}>
                        Личный кабинет uralintern.ru - средство учёта и
                        контроля, позволяющее отслеживать и оценивать вклад
                        каждого участника в командный проект, выполняемый во
                        время прохождения стажировки.
                    </p>
                </div>
                <div className={classes["authentication"]}>
                    <h3 className={classes["authentication-h3"]}>
                        Вход в систему
                    </h3>
                    {!user ? (
                        <form onSubmit={loginUser}>
                            <input
                                className={classNames(
                                    classes["log-to-account-input"],
                                    classes["login"]
                                )}
                                type="text"
                                name="username"
                                aria-label="Логин"
                                placeholder="Логин"
                                required
                            />
                            <br />
                            <input
                                className={classNames(
                                    classes["log-to-account-input"],
                                    classes["password"]
                                )}
                                type="password"
                                name="password"
                                aria-label="Пароль"
                                placeholder="Пароль"
                                required
                            />
                            <br />
                            <button
                                className={classes["log-to-account-button"]}
                                type="submit"
                            >
                                Войти
                            </button>
                        </form>
                    ) : (
                        <div>Вы уже Авторизированы</div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default LoginPage;
