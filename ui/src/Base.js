import './Home.css';
import { BrowserRouter as Router, Link} from 'react-router-dom';
import Route from 'react-router-dom/Route';
import Home from './Home';
import Template from './Template';

function Base() {
    return (
        <Router>
        <div className="Homepage">
        <nav>
        <ul>
          <li>
          <div className="nav-link">
            <Link to="/home" exact style={{ color: '#000', textDecoration: 'none' }}>Home</Link>
            </div>
          </li>
          <li>
              <div className="nav-link">
            <Link to="/template" exact style={{ color: '#000', textDecoration: 'none' }}>Template</Link>
            </div>
          </li>
          </ul>
          </nav>
        <Route path="/home" exact strict render={
          () => {
            return ( <Home />);
          }
        }/>
        <Route path="/template" exact strict render={
          () => {
            return ( <Template />);
          }
        }/>
        </div>
      </Router>
    );
}

export default Base;