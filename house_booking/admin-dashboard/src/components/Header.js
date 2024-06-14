import React from 'react';
import { AppBar, Toolbar, Typography, IconButton } from '@mui/material';
import AccountCircle from '@mui/icons-material/AccountCircle';

const Header = () => (
    <AppBar position="static">
        <Toolbar>
            <Typography variant="h6" style={{ flexGrow: 1 }}>
                Admin Dashboard
            </Typography>
            <IconButton color="inherit">
                <AccountCircle />
            </IconButton>
        </Toolbar>
    </AppBar>
);

export default Header;
