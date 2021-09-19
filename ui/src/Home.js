import './Home.css';
import Template from './Template';
// import textEditor from './textEditor';

function Home() {
  return (
    <div className="Homepage">
        <form >
        <div className="Homepage">
          <div className="form-element">
            <p>Project name:</p>
            <input type="text" name="project name" placeholder="Project name" />
          </div> 
          <div className="form-element">
           <p>Configure docker file:</p>
           <textarea wrap="off" cols="30" rows="5"></textarea>
          </div> 
          <div className="form-element">
          <button>scan</button>
          </div>
          <div className="form-element">
          <p>Choose from Templates:</p>
          <Template />
          </div>
          <div className="form-element">
          <button>build</button>
          </div>
          </div>
        </form>
     </div>
  );
}

export default Home;
