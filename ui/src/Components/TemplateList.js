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
                        border: 1,
                        borderStyle: 'dashed',
                        padding: 5,
                        margin: 5
                    }}>
                        <h3 style={{
                            backgroundColor: 'grey',
                            padding: 5,
                            margin: 5,
                        }}>{post.Name_of_template}</h3>
                        <div>
                            <h4>CAP_Id | Name_of_capability | description_of_capability</h4>
                            {post.capabilities.map(cap => {
                                return <div>
                                        <h5>{cap.CAP_Id}. {cap.Name_of_capability} | {cap.description_of_capability}</h5>
                                    </div>
                            })}  
                        </div>
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