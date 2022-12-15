import axios from "axios";
import jwt_decode from "jwt-decode";
import dayjs from "dayjs";
import BASE_URL from "../Auth/BaseUrl";
import END_POINTS from "../Auth/EndPoints";

const baseURL = BASE_URL;

let authTokens = localStorage.getItem("authTokens")
    ? JSON.parse(localStorage.getItem("authTokens"))
    : null;

const axiosInstance = axios.create({
    baseURL,
    headers: { Authorization: `Bearer ${authTokens?.access}` },
});

axiosInstance.interceptors.request.use(async (req) => {
    if (!authTokens) {
        authTokens = localStorage.getItem("authTokens")
            ? JSON.parse(localStorage.getItem("authTokens"))
            : null;
        req.headers.Authorization = `Bearer ${authTokens?.access}`;
    }

    const user = jwt_decode(authTokens.access);
    const isExpired = dayjs.unix(user.exp).diff(dayjs()) < 1;

    if (!isExpired) return req;

    const response = await axios.post(`${baseURL + END_POINTS.AUTH.REFRESH}`, {
        refresh: authTokens.refresh,
    });

    localStorage.setItem("authTokens", JSON.stringify(response.data));
    req.headers.Authorization = `Bearer ${response.data.access}`;
    return req;
});

export default axiosInstance;