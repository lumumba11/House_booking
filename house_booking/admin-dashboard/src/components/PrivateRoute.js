// src/components/PrivateRoute.js
import React from 'react';
import { Navigate } from 'react-router-dom';

const PrivateRoute = ({ children }) => {
    const isAuthenticated = !!localStorage.getItem('access_token');
    return isAuthenticated ? (
        children
    ) : (
        <Navigate to="/login" replace state={{ from: window.location.pathname }} />
    );
};

export default PrivateRoute;
