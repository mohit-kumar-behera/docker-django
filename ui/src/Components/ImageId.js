import React from 'react';
import './styles.css'

function Imageid(props){
    let data = props.data[0];
    return(
        <div style={{
            
        }}>
            {data.Imageid.map((value, key) => {
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

                        
                        <h3>Title: {value.id}</h3>
                       
                    </div>
            })}
        </div>
    )
}

export default Imageid;