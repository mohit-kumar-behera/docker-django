import { useState } from 'react';
import './Home.css';
import Template from './Template';
// import textEditor from './textEditor';

var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

function Home() {

  const [dockerConfig, setDockerConfig] = useState('');
  const [projectName, setProjectName] = useState('');

  const onClickSync = () => {
    var raw = JSON.stringify({
      "project_name": projectName
    });
    
    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };
    fetch("http://127.0.0.1:5000/create_project/", requestOptions)
    .then(response => response.json())
    .then(result => {
      console.log(result.dockerfile)
      setDockerConfig(result.dockerfile)
    })
    .catch(error => console.log('error', error));
  }

  const onClickScan = () => {
    
  }

  // const handleChange = (e) => {
  //   console.log(e.target.value);
  // }

  return (
    <div className="Homepage">
        <div className="Homepage">
          <div className="form-element">
            <p>Project name:</p>
            <input 
            type="text" 
            name="project name" 
            onChange={(e) => setProjectName(e.target.value)}
            placeholder="Project name" />
            <button onClick={onClickSync}>sync</button>
          </div> 
          <div className="form-element">
            <p>Configure docker file:</p>
            <textarea 
              value={dockerConfig} 
              onChange={e => setDockerConfig(e.target.value)} 
              wrap="off" cols="50" rows="20">
            </textarea>
          </div> 
          <div className="form-element">
            <button onClick={}>scan</button>
          </div>
          <div className="form-element">
          <p>Choose from Templates:</p>
            <Template />
          </div>
          <div className="form-element">
            <button>build</button>
          </div>
          </div>
     </div>
  );
}

export default Home;
