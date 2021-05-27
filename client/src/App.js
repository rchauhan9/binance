import React, {useState, useEffect, useRef} from 'react';

import CurrencyTable from "./currency/CurrencyTable";

const App = () => {
    return (
        <div>
            <nav className="navbar navbar-light bg-light">
                <a className="navbar-brand" href="#" style={{marginLeft: 20}}>Crypto Dashboard</a>
            </nav>
            <div className="container">
                <CurrencyTable />
            </div>
        </div>
    );
};

export default App;