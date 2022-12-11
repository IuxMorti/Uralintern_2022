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

function App() {
    return (
        <div className="App">
            <Router>
                <AuthProvider>
                    <Header />
                    <PrivateRoute component={HomePage} path="/profile" exact />
                    <Route path="/user/:userId" component={User} />
                    <Route path="/team/:teamId" component={Team} />
                    <Route component={LoginPage} path="/login" exact />
                    <Footer />
                </AuthProvider>
            </Router>
        </div>
    );
}

export default App;
