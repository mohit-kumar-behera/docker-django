import './Template.css';
import FormatCapabilities from './FormatCapabilities';
import TemplateList from './Components/TemplateList';

function Template() {
  return (
    <div>
      <h3>Existing Templates</h3>
      <TemplateList />
    <div className="Template">
        <h4>TEMPLATE--1</h4>
        <div className="Rectangle">
        <table>
  <tr>
    <th> </th>
    <th>Capability Name </th>
    <th>Capability ID </th>
  </tr>
  <tr>
    <td>1.</td>
    <td>ADD</td>
    <td>CAP_1</td>
  </tr>
  <tr>
    <td>2.</td>
    <td>ADD</td>
    <td>CAP_2</td>
  </tr>
  <tr>
    <td>3.</td>
    <td>ADD</td>
    <td>CAP_</td>
  </tr>
</table>
</div>
   <button>ADD</button>
   <h4>TEMPLATE--2</h4>
        <div className="Rectangle">
        <table>
  <tr>
    <th> </th>
    <th>Capability Name </th>
    <th>Capability ID </th>
  </tr>
  <tr>
    <td>1.</td>
    <td>ADD</td>
    <td>CAP_1</td>
  </tr>
  <tr>
    <td>2.</td>
    <td>ADD</td>
    <td>CAP_2</td>
  </tr>
  <tr>
    <td>3.</td>
    <td>ADD</td>
    <td>CAP_</td>
  </tr>
</table>
</div>
   <button>ADD</button>
     </div>
     <div>
     <h3>Create New Templates</h3>
     <p>Name of Template:</p>
     <input 
            type="text" 
            name="template name" 
            placeholder="Template name" />
      <p>Choose Capabilities:</p>
      <input type="checkbox" id="CAP_1" name="CAP_1" value="CAP_1"/>
      <label for="CAP_1">CAP_1</label><br/>
      <input type="checkbox" id="CAP_2" name="CAP_2" value="CAP_2"/>
      <label for="CAP_2"> CAP_2</label><br/>
      <input type="checkbox" id="CAP_3" name="CAP_3" value="CAP_3"/>
      <label for="CAP_3"> CAP_3</label>
      <br/>
      <button>CREATE</button>
      </div>
      <div>
      <FormatCapabilities />
      </div>
     </div>
     
  );
}

export default Template;