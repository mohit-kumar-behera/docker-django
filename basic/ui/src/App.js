import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <form method="POST" action=".">
          <div className="form-element">
            <p>Type project name:</p>
            <input type="text" name="project-name" placeholder="Project name" />
          </div>
          <div className="form-element">
            <p>make your docker file:</p>
            <textarea rows="15" cols="80" name="about" />
          </div>
          <div className="form-element">
            <p>scan docker file:</p>
            <button>scan</button>
          </div>
        </form>
      </header>
    </div>
  );
}

export default App;
