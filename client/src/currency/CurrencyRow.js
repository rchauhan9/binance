import React, {useEffect, useRef, useState} from "react";


const CurrencyRow = ({name, ticker}) => {
    const [isPaused, setPause] = useState(false);
    const ws = useRef(null);

    const [price, setPrice] = useState('');
    const [volume, setVolume] = useState('');

    useEffect(() => {
        ws.current = new WebSocket(`ws://localhost:5678/${ticker}`);
        ws.current.onopen = () => console.log("ws opened");
        ws.current.onclose = () => console.log("ws closed");
        return () => {
            ws.current.close();
        };
    }, []);

    useEffect(() => {
        if (!ws.current) return;

        ws.current.onmessage = e => {
            if (isPaused) return;
            const message = JSON.parse(e.data);
            console.log("e", message);
            setPrice(message.data.c)
            setVolume(message.data.v)
        };
    }, [isPaused]);

    return (
        <tr>
            <th scope="row">{name}</th>
            <td>{ticker}</td>
            <td>{price}</td>
            <td>{volume}</td>
        </tr>
    )
}


export default CurrencyRow;