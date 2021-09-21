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
        axios.get('http://127.0.0.1:5000/api/capabilities')
        .then( response => {
            console.log(response)
            this.setState({posts: response.data})
        })
        .catch(error => {
            console.log(error)
        })
    }
    render() { 
        const {posts} = this.state
        return (
        <div>
        <p>existing templates</p>
        {
            posts.length ?
            posts.map(post => <div key = {post.id}>{post.title}</div> ) :
            null
        }

        </div>
        );
    }
}
 
export default TemplateList