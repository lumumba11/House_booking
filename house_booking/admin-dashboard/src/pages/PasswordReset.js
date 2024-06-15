// src/pages/PasswordReset.js
import React, { useState } from 'react';
import axios from 'axios';

const PasswordReset = () => {
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');

    const handlePasswordReset = async (e) => {
        e.preventDefault();
        try {
            if (!email) {
                setMessage('Email is required');
                return;
            }
            await axios.post('http://127.0.0.1:8000/api/rest-auth/password/reset/', { email });
            setMessage('Password reset email sent');
        } catch (err) {
            if (err.response && err.response.status === 400) {
                setMessage('Invalid email or email not found');
            } else {
                setMessage('Error sending password reset email');
            }
        }
    };

    return (
        <div className="password-reset-container">
            <h2>Password Reset</h2>
            <form onSubmit={handlePasswordReset}>
                <div>
                    <label>Email:</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                {message && <p style={{ color: message.includes('Error') ? 'red' : 'green' }}>{message}</p>}
                <button type="submit">Send Password Reset Email</button>
            </form>
        </div>
    );
};

export default PasswordReset;
