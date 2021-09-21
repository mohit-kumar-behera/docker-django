import React from 'react';
import './styles.css'

function MisConfig(props){
    // console.log(props.data[0])
    let data = props.data[0];
    return(
        <div style={{
            
        }}>
            {data.Misconfigurations.map((value, key) => {
                // console.log(value)
                // value.forEach((k, v) => {
                //     console.log(k, v)
                // })
                return <div style={{
                    border: 2,
                    borderColor: 'white',
                    // backgroundColor: 'grey',
                    padding: 5,
                }} key={key}>

                        {/* <p>Type: {value.Type}</p>
                        <p>ID: {value.ID}</p> */}
                        <h3>Title: {value.Title}</h3>
                        <p>Description: {value.Description}</p>
                        <p>Message: {value.Message}</p>
                        <p>Namespace: {value.Namespace}</p>
                        <p>Query: {value.Query}</p>
                        <p>Resolution: {value.Resolution}</p>
                        <p>Status: {value.Status}</p>
                    </div>
            })}
        </div>
    )
}

export default MisConfig;