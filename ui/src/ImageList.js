import React from 'react';
import axios from 'axios';
import './imageList.css'


class Imagelist extends React.Component {
        constructor(props) {
          super(props);
          this.state = {
            posts: [],
            imgs: {},
            repo: {},
          };
          this.setchooseimgid = this.setchooseimgid.bind(this);
          this.onClickPush = this.onClickPush.bind(this);
          this.setReponame = this.setReponame.bind(this);
        }
      
        setchooseimgid(val) {
          console.log(val);
          let imgs = this.state.imgs;
          imgs[val - 1] = !imgs[val - 1];
          this.setState({ imgs: imgs });
        }
        setReponame(name) {
          console.log(name);
          this.setState({ repo: name });
        }
        onClickPush() {
          let repo = this.state.repo;
          let imgs = [];
          for (let i = 0; i < this.state.posts.length; i++) {
            if (this.state.imgs[i]) {
              imgs.push(this.state.posts[i]);
            }
          }
          console.log(imgs);
          const pushimg = { repo, imgs };
          console.log(pushimg);
          fetch('http://127.0.0.1:5000/api/push/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(pushimg),
          })
     
          .catch(error => console.log('error', error));
      
      
          }
          componentDidMount() {
              axios.get('http://127.0.0.1:5000/api/images')
              .then( response => {
                  console.log(response)
                  let imgs = {}
                  for (let i=0 ; i<response.message.length ; i++)
                  {
                      imgs[i]=false
                  }
                  this.setState({posts: response.message,imgs :imgs})
              })
              .catch(error => {
                  console.log(error)
              })
          }
          render() { 
              const {posts} = this.state
              return (
              <div className="contentpage">
              
              {
                  posts.length ?
                  posts.map(post => {
      
                      return (
                          <div key = {post.Id} >
                              <div className='check'>
                              
                                             <input type="radio" id="IMG" name="IMG" onClick={(e) => this.setchooseimgid(e.target.value)} value={post.Id}/>
                                              <label for="IMG">{post.Id} </label><br/>
                                              <br/>
                                 
                               </div>
                              
                          </div>
                    
                      )
                  } ) :
                  null
              }
                
                <p>Name of Repo:</p>
                <input type="text" name="repo name" onChange={(e) => this.setReponame(e.target.value)} placeholder="Repo name" />
                <br />
                <button onClick={this.onClickPush} >push</button> 
                <br />
              </div>
              );
          }
      
      }
    
    export default Imagelist;
    




