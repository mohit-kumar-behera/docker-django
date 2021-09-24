import { useState,useEffect } from 'react';
import './composeFile.css';
import Composeresp from './Components/Composeresp';

import axios from 'axios';

var myHeaders = new Headers();
myHeaders.append('Content-Type', 'application/json');

function Composefile() {
  const [dockerConfig, setDockerConfig] = useState('');
  const [projectName, setProjectName] = useState('');
  const [trivyResp, setTrivyResp] = useState('');
  const [posts, setPosts] = useState('');
  const [hist, setHist] = useState({});


  useEffect (()=>{
    axios.get('http://127.0.0.1:5000/api/templates')
        .then( response => {
            console.log(response)
            setPosts(response.data.message)
        })
        .catch(error => {
            console.log(error)
        })
  },[])
  const handleAdd = (post) => {
    //if(hist[post.Name_of_template] !== true)
    
      //hist[post.Name_of_template] = true
      var val = dockerConfig
      console.log("handletrigger")
      for(let i =0 ; i < post.capabilities.length ; i++)
      {
        let cap = post.capabilities[i]
        //console.log(cap)
        val += `\n        - ${cap.Name_of_capability}`
      }
      setDockerConfig(val)
    
  
  } 
  const onClickSync = () => {
    if (!projectName) return;
    var raw = JSON.stringify({
      project_name: projectName,
    });

    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow',
    };
    fetch('http://127.0.0.1:5000/create_compose_project/', requestOptions)
      .then((response) => response.json())
      .then((result) => {
       
        let res = result.dockerfile;
        let str = 'securityContext:\n    capabilities:\n      add:';
        console.log(res)
        setDockerConfig(res)
        
      })
      .catch((error) => console.log('error', error));
  };

  const onClickScan = () => {
    var raw = JSON.stringify({
      project_name: projectName,
      docker_content: dockerConfig,
    });

    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow',
    };
    fetch('http://127.0.0.1:5000/scan_compose_file/', requestOptions)
      .then((response) => response.json())
      .then((result) => {
        console.log(JSON.parse(result.trivy_response));
        
        setTrivyResp(JSON.parse(result.trivy_response));
      })
      .catch((error) => console.log('error', error));
  };

  // const handleChange = (e) => {
  //   console.log(e.target.value);
  // }

  return (
    <div className="contentpage">
      <div className="content">
        <div className="form-element">
          <p>Project name:</p>
          <input
            type="text"
            name="project name"
            onChange={(e) => setProjectName(e.target.value)}
            placeholder="Project name"
          />
          <button onClick={onClickSync}>sync</button>
        </div>
        <div className="form-element">
          <p>Write in yaml file:</p>
          <textarea
            value={dockerConfig}
            onChange={(e) => setDockerConfig(e.target.value)}
            wrap="off"
            cols="75"
            rows="20"
          ></textarea>
        </div>
        <div className="form-element">
          <button onClick={onClickScan}>scan</button>
        </div>
        <div>{trivyResp !== '' && <Composeresp data={trivyResp} />}</div>
      </div>
      <div>
        {/* <p>existing templates</p> */}
        {
            posts.length ?
            posts.map(post => {
              const handle = () => {
                handleAdd(post)
              }

                return (
                    <div className="templist" key = {post.TEMP_Id} >
                        
                        <h3>{post.Name_of_template} <button onClick = {handle} >ADD</button></h3>
                        
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
    </div>
  );
}

export default Composefile;
