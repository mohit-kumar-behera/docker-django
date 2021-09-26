import React from 'react';
import './styles.css'

function MisConfig(props){
    // console.log(props.data[0])
    let data = props.data[0];
    return(
        <div style={{
            
        }}>
            {data.Misconfigurations.map((value, key) => {
                console.log(value)
                // value.forEach((k, v) => {
                //     console.log(k, v)
                // })
                return <div style={{
                    border: 2,
                    borderColor: 'white',
                    // backgroundColor: 'grey',
                    padding: 5,
                }} key={key}>

                        <h6>Type: {value.Type}</h6>
                        <p>ID: {value.ID}</p>
                        <p>Title: {value.Title}</p>
                        <p>Severity: {value.Severity}</p>
                        <p>Message: {value.Message}</p>
                        <p>Description: {value.Description}</p>
                        <p>Resolution: {value.Resolution}</p>
                        <p>Status: {value.Status}</p>
                    </div>
            })}
        </div>
    )
}

export default MisConfig;