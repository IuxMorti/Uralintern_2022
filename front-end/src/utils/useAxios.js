import axios from "axios";
import jwt_decode from "jwt-decode";
import dayjs from "dayjs";
import { useContext } from "react";
import AuthContext from "../context/AuthContext";
import BASE_URL from "../Auth/BaseUrl";
import END_POINTS from "../Auth/EndPoints";

const baseURL = BASE_URL;

const useAxios = () => {
    const { authTokens, setUser, setAuthTokens, logoutUser } =
        useContext(AuthContext);

    const axiosInstance = axios.create({
        baseURL,
        headers: { Authorization: `Bearer ${authTokens?.access}` },
    });

    axiosInstance.interceptors.request.use(async (req) => {
        const user = jwt_decode(authTokens.access);
        const isExpired = dayjs.unix(user.exp).diff(dayjs()) < 1;

        if (!isExpired) return req;

        try {
            const response = await axios.post(
                `${baseURL + END_POINTS.AUTH.REFRESH}`,
                {
                    refresh: authTokens.refresh,
                }
            );
            if (response.status === 200) {
                localStorage.setItem(
                    "authTokens",
                    JSON.stringify(response.data)
                );

                setAuthTokens(response.data);
                setUser(jwt_decode(response.data.access));

                req.headers.Authorization = `Bearer ${response.data.access}`;
                return req;
            }
        } catch (e) {
            if (e.response.status === 401) {
                logoutUser();
                return req;
            }
        }
    });

    return axiosInstance;
};

export default useAxios;
