import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";
import classes from "./css/Header.module.css";

const Header = () => {
    let { user, logoutUser } = useContext(AuthContext);
    return (
        <header className={classes["main-header"]}>
            <a href={user ? `/main` : ""}>
                <img
                    className={classes["small-logo"]}
                    src={require("../images/logo_small.svg").default}
                    width="49.82"
                    height="50"
                    alt="Логотип"
                />
            </a>
            {user ? (
                <div className={classes["profile"]}>
                    <a href={user ? `/user/${user.user_id}` : ""}>
                        <img
                            className={classes["profile-img"]}
                            src={require("../images/profile.svg").default}
                            width="24"
                            height="24"
                            alt="Мой профиль"
                        />
                    </a>
                    <a
                        href={user ? `/user/${user.user_id}` : ""}
                        className={classes["profile-p"]}
                    >
                        Мой Профиль
                    </a>
                </div>
            ) : (
                <div className={classes["profile"]}></div>
            )}
            <div className={classes["exit"]}>
                <img
                    className={classes["exit-img"]}
                    onClick={logoutUser}
                    src={require("../images/exit.svg").default}
                    width="18"
                    height="18"
                    alt="Выйти"
                />
                <span onClick={logoutUser} className={classes["profile-p"]}>
                    {user ? "ВЫЙТИ" : "Авторизироваться"}
                </span>
            </div>
        </header>
    );
};

export default Header;
