import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Houses = () => {
    const [houses, setHouses] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/api/houses/')
            .then(response => setHouses(response.data))
            .catch(error => console.error('Error fetching houses:', error));
    }, []);

    return (
        <div>
            <h1>Houses</h1>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Owner</th>
                        <th>Price</th>
                        <th>Location</th>
                        <th>Availability</th>
                    </tr>
                </thead>
                <tbody>
                    {houses.map(house => (
                        <tr key={house.id}>
                            <td>{house.id}</td>
                            <td>{house.name}</td>
                            <td>{house.owner}</td>
                            <td>{house.price_per_night}</td>
                            <td>{house.location}</td>
                            <td>{house.availability ? 'Yes' : 'No'}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Houses;
