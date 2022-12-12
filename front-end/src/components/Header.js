import React, { useContext } from "react";
import AuthContext from "../context/AuthContext";

const Header = () => {
    let { user, logoutUser } = useContext(AuthContext);
    return (
        <div>
            <header className="main-header">
                <img
                    className="small-logo"
                    src={require("../images/logo_small.svg").default}
                    width="49.82"
                    height="50"
                    alt="Логотип"
                />
                <div className="profile">
                    <a href={user ? `/user/${user.user_id}` : ""}>
                        <img
                            src={require("../images/profile.svg").default}
                            width="24"
                            height="24"
                            alt="Мой профиль"
                        />
                    </a>
                    <p>Мой Профиль</p>
                </div>
                <div className="exit">
                    {user ? (
                        <a href="/login">
                            <img
                                onClick={logoutUser}
                                src={require("../images/exit.svg").default}
                                width="18"
                                height="18"
                                alt="Выйти"
                            />
                        </a>
                    ) : (
                        <a href="/login">Login</a>
                    )}
                </div>
            </header>
        </div>
    );
};

export default Header;
