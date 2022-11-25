import { useState, useEffect } from "react";
import moment from "moment"
import "../css/timer.css"
const Timer = ({product}) => {

    const [DD, setDD] = useState(null);
    const [HH, setHH] = useState(null);
    const [MM, setMM] = useState(null);
    const [SS, setSS] = useState(null);
    
    useEffect(() => {
        
        let now = moment();
        let end = moment(product[7], 'YYYY-MM-DD hh:mm');

        let diff = moment.duration(end.diff(now))._data;
        let d = diff.days;
        let h = diff.hours;
        let m = diff.minutes;
        let s = diff.seconds;

        
        let dd = ('0' + d).slice(-2);
        let hh = ('0' + h).slice(-2);
        let mm = ('0' + m).slice(-2);
        let ss = ('0' + s).slice(-2);
        
        setTimeout(() => {
            
            setDD(dd)
            setHH(hh);
            setMM(mm);
            setSS(ss);
            
        }, 1000);
        
    }, [SS]);
    return(
        <div className="time-container">
                <div className="time">
                    <p>{DD}</p>
                    <p>Days</p>
                </div>
                <div className="time">
                    <p>{HH}</p>
                    <p>Hours</p>
                </div>
                <div className="time">
                    <p>{MM}</p>
                    <p>Minutes</p>
                </div>
                <div className="time">
                    <p>{SS}</p>
                    <p>Seconds</p>
            </div>

        </div>
    )
}

export default Timer;