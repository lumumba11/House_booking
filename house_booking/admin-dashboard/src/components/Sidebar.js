import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => (
  <div className="sidebar">
    <ul>
      <li><Link to="/dashboard">Dashboard Home</Link></li>
      <li><Link to="/houses">Houses Management</Link></li>
      <li><Link to="/bookings">Bookings Management</Link></li>
      <li><Link to="/users">Users Management</Link></li>
    </ul>
  </div>
);

export default Sidebar;
