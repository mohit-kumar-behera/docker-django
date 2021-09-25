import React from 'react';
import axios from 'axios';


class Imagelist extends React.Component {
    constructor(props) {
        super(props);
        this.state = { 
            posts: []
         }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:5000/api/images')
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
                    <div className="templist" key = {post.TEMP_Id} >
                        
                        <h3>{post.Name_of_template}</h3>
                        <div>
                        <table >
                                        
                                            <h4>Capability ID || Capability Name : Description of capability </h4>
                                        <hr />
                            {post.capabilities.map(cap => {
                                return <div>
                                
                                            <h6>{cap.CAP_Id} || <strong>{cap.Name_of_capability}</strong> : {cap.description_of_capability}</h6>
                                       
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
 
export default Imagelist





