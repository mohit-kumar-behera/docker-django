import React from 'react';
import axios from 'axios';

class CapabilityList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      posts: [],
      caps: {},
      temp: {},
    };
    this.setchosecapabilities = this.setchosecapabilities.bind(this);
    this.onClickCreate = this.onClickCreate.bind(this);
    this.setTemplateName = this.setTemplateName.bind(this);
  }

  setchosecapabilities(val) {
    console.log(val);
    let caps = this.state.caps;
    caps[val - 1] = !caps[val - 1];
    this.setState({ caps: caps });
  }
  setTemplateName(name) {
    console.log(name);
    this.setState({ temp: name });
  }
  onClickCreate() {
    let temp = this.state.temp;
    let caps = [];
    for (let i = 0; i < this.state.posts.length; i++) {
      if (this.state.caps[i]) {
        caps.push(this.state.posts[i]);
      }
    }
    console.log(caps);
    const template = { temp, caps };
    console.log(template);
    fetch('http://127.0.0.1:5000/api/create_template/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(template),
    })
      .then(() => {
        console.log('New template added');
      })
      .catch((error) => console.log('error', error));
  }
  componentDidMount() {
    axios
      .get('http://127.0.0.1:5000/api/capabilities')
      .then((response) => {
        console.log(response);
        let caps = {};
        for (let i = 0; i < response.data.message.length; i++) {
          caps[i] = false;
        }
        this.setState({ posts: response.data.message, caps: caps });
      })
      .catch((error) => {
        console.log(error);
      });
  }
  render() {
    const { posts } = this.state;
    return (
      <div>
        <p>Name of Template:</p>
        <input
          type="text"
          name="template name"
          onChange={(e) => this.setTemplateName(e.target.value)}
          placeholder="Template name"
        />
        {posts.length
          ? posts.map((post) => {
              return (
                <div
                  key={post.CAP_Id}
                  style={{
                    padding: 5,
                    margin: 5,
                  }}
                >
                  <div>
                    <div>
                      <input
                        type="checkbox"
                        id="CAP"
                        name="CAP"
                        onClick={(e) =>
                          this.setchosecapabilities(e.target.value)
                        }
                        value={post.CAP_Id}
                      />
                      <label for="CAP_1">
                        {post.Name_of_capability} --{' '}
                        {post.description_of_capability}{' '}
                      </label>
                      <br />
                      <br />
                    </div>
                  </div>
                </div>
              );
            })
          : null}
        <button onClick={this.onClickCreate}>CREATE</button>
      </div>
    );
  }
}

export default CapabilityList;
