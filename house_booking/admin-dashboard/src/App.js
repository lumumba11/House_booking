import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import DashboardHome from './components/DashboardHome';
import Houses from './pages/Houses';
import Bookings from './pages/Bookings';
import Users from './pages/Users';
const App = () => (
  <Router>
    <div className="app">
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
    </div>
  </Router>
);

export default App;
