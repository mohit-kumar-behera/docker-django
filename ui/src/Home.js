import { useState } from 'react';
import './Home.css';
import MisConfigs from './Components/MisConfig';
import Imageid from './Components/ImageId';

var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

function Home() {

  const [dockerConfig, setDockerConfig] = useState('');
  const [projectName, setProjectName] = useState('');
  const [trivyResp, setTrivyResp] = useState('');
  const [imageId, setimageId] = useState('');

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
      // console.log(result.dockerfile)
      setDockerConfig(result.dockerfile)
    })
    .catch(error => console.log('error', error));
  }

  const onClickScan = () => {
    var raw = JSON.stringify({
      "project_name": projectName,
      "docker_content": dockerConfig
    });
    
    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };
    fetch("http://127.0.0.1:5000/scan/", requestOptions)
    .then(response => response.json())
    .then(result => {
      console.log(JSON.parse(result.trivy_response))
      setTrivyResp(JSON.parse(result.trivy_response))
    })
    .catch(error => console.log('error', error));
  }

  const onClickBuild = () => {
    var raw = JSON.stringify({
      "project_name": projectName
    });
    
    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };
    fetch("http://127.0.0.1:5000/build/", requestOptions)
    .then(response => response.json())
    .then(result => {
      // console.log(result.image_id)
      setimageId(JSON.parse(result.image_id))
    })
    .catch(error => console.log('error', error));
  }

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
            placeholder="Project name" />
            <br />
            <button onClick={onClickSync}>sync</button>
            
          </div> 
          <div className="form-element">
            <p>Write in Docker File:</p>
            <textarea 
              value={dockerConfig} 
              onChange={e => setDockerConfig(e.target.value)} 
              wrap="off" cols="75" rows="20">
            </textarea>
          </div> 
          <br />
          <div className="form-element">
            <button onClick={onClickScan}>scan</button>
          </div>
          <div>
            { trivyResp !== '' && <MisConfigs data={trivyResp} />}
          </div>
          <br />
          <div className="form-element">
            <button onClick={onClickBuild}>build</button>
          </div>
          <div>
            { imageId !== '' && <Imageid data={imageId} />}
          </div>
          </div>
     </div>
  );
}

export default Home;
