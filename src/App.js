import './App.css';
// import { Routes ,Route } from 'react-router-dom';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Signup from './components/LoginSignup/Signup';
import Login from './components/LoginSignup/Login';

function App() {
  return (
    <BrowserRouter>
    <Routes>
        <Route path="/" element={<Signup />}>
          {/* <Route index element={<Signup />} /> */}
        </Route>
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
