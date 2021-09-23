import React from 'react';
import axios from 'axios';


class TemplateList extends React.Component {
    constructor(props) {
        super(props);
        this.state = { 
            posts: []
         }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:5000/api/templates')
        .then( response => {
            console.log(response)
            this.setState({posts: response.data.message})
        })
        .catch(error => {
            console.log(error)
        })
    }
    render() { 
        const {posts} = this.state
        return (
        <div>
        {/* <p>existing templates</p> */}
        {
            posts.length ?
            posts.map(post => {

                return (
                    <div key = {post.TEMP_Id} style={{
                        padding: 5,
                        margin: 5
                    }}>
                        
                        <h3 style={{
                            backgroundColor: 'grey',
                            padding: 5,
                            margin: 5,
                        }}>{post.Name_of_template}</h3>
                        <div>
                        <table style={{border: 1,
                        padding: 5,
                            margin: 5,
                            borderStyle: 'dashed',}}>
                       
                                        <tr>
                                            <td>Capability ID</td>
                                            <td>Capability Name</td>
                                            <td>description_of_capability </td>
                                        </tr>
                            {post.capabilities.map(cap => {
                                return <div>
                                       
                                        <tr>
                                            <td>{cap.CAP_Id}</td>
                                            <td>{cap.Name_of_capability} </td>
                                            <td>{cap.description_of_capability}</td>
                                        </tr>
                                    </div>
                            })} 
                        </table> 
                       
                        </div>
                        <br />
                    </div>
              
                )
            } ) :
            null
        }

        </div>
        );
    }
}
 
export default TemplateList

