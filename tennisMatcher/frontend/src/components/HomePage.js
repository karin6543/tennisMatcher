import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';

import CreateRoomPage from "./CreateRoomPage";
import React from 'react'
import RoomJoinPage from "./RoomJoinPage";

const HomePage = () => {
    return (<Router>
        <Routes>
            <Route exact path="/" element={<div>home page?</div>} />
            <Route path="/join" element={<RoomJoinPage />} />
            <Route path="/create" element={<CreateRoomPage />} />
        </Routes>
    </Router>)
}

export default HomePage;
