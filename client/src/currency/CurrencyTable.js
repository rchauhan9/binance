import React from 'react';
import CurrencyRow from "./CurrencyRow";


const CurrencyTable = () => {


    return (
        <table className="table">
            <thead>
            <tr>
                <th scope="col">Name</th>
                <th scope="col">Ticker</th>
                <th scope="col">Price</th>
                <th scope="col">Volume</th>
            </tr>
            </thead>
            <tbody>
            <CurrencyRow name="Bitcoin" ticker="BTCUSDT"/>
            <CurrencyRow name="Ethereum" ticker="ETHUSDT"/>
            </tbody>
        </table>
    )
}

export default CurrencyTable;