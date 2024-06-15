import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import DashboardHome from './components/DashboardHome';
import Houses from './pages/Houses';
import Bookings from './pages/Bookings';
import Users from './pages/Users';
import Login from './pages/Login';
import Signup from './pages/Signup';
import PasswordReset from './pages/PasswordReset';
import PrivateRoute from './components/PrivateRoute';

const App = () => (
    <Router>
        <div className="app">
            <Routes>
                <Route path="/signup" element={<Signup />} />
                <Route path="/login" element={<Login />} />
                <Route path="/password-reset" element={<PasswordReset />} />
                <Route path="/" element={<Navigate to="/signup" />} />
                <PrivateRoute path="/*">
                    <Sidebar />
                    <div className="main-content">
                        <Header />
                        <Routes>
                            <Route path="/dashboard" element={<DashboardHome />} />
                            <Route path="/houses" element={<Houses />} />
                            <Route path="/bookings" element={<Bookings />} />
                            <Route path="/users" element={<Users />} />
                        </Routes>
                    </div>
                </PrivateRoute>
            </Routes>
        </div>
    </Router>
);

export default App;
