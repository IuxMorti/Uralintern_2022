import "./App.css";
import { BrowserRouter as Router, Route } from "react-router-dom";
import PrivateRoute from "./utils/PrivateRoute";
import { AuthProvider } from "./context/AuthContext";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import Header from "./components/Header";
import User from "./pages/User";
import Footer from "./components/Footer";
import Team from "./pages/Team";
import Form from "./pages/Form";
import Report from "./pages/Report";
import LoginRoute from "./utils/LoginRoute";

function App() {
    return (
        <div className="App">
            <Router>
                <AuthProvider>
                    <Header />
                    <LoginRoute path="/" exact />
                    <PrivateRoute path="/main" component={HomePage} />
                    <PrivateRoute path="/user/:userId" component={User} />
                    <PrivateRoute path="/team/:teamId" component={Team} />
                    <Route path="/login" component={LoginPage} exact />
                    <PrivateRoute path="/form/:teamId" component={Form} />
                    <PrivateRoute
                        path="/report/:teamId/:userId"
                        component={Report}
                    />
                    <Footer />
                </AuthProvider>
            </Router>
        </div>
    );
}

export default App;
