import './Base.css';
import { BrowserRouter as Router, Link} from 'react-router-dom';
import Route from 'react-router-dom/Route';
import Home from './Home';
import Template from './Template';
import Composefile from './composeFile';
import Imagelist from './imageList';

function Base() {
    return (
        <Router>
        <div className="Homepage">
        <div className="navbar">
        <ul>
          <li>
          <div className="nav-link">
            <Link to="/image" exact style={{ color: '#000', textDecoration: 'none' }}>Docker Image</Link>
            </div>
          </li>
          <li>
          <div className="nav-link">
            <Link to="/composefile" exact style={{ color: '#000', textDecoration: 'none' }}>Docker compose file</Link>
            </div>
          </li>
          <li>
              <div className="nav-link">
            <Link to="/template" exact style={{ color: '#000', textDecoration: 'none' }}>Template</Link>
            </div>
          </li>
          <li>
              <div className="nav-link">
            <Link to="/imagelist" exact style={{ color: '#000', textDecoration: 'none' }}>Image List</Link>
            </div>
          </li>
          </ul>
          </div>
        <Route path="/image" exact strict render={
          () => {
            return ( <Home />);
          }
        }/>
         <Route path="/composefile" exact strict render={
          () => {
            return ( <Composefile />);
          }
        }/>
        <Route path="/template" exact strict render={
          () => {
            return ( <Template />);
          }
        }/>
        <Route path="/imagelist" exact strict render={
          () => {
            return ( <Imagelist />);
          }
        }/>
        </div>
      </Router>
    );
}

export default Base;