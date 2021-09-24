import './Template.css';
import TemplateList from './Components/TemplateList';
import CapabilityList from './Components/CapabilityList';


function Template() {

  


  return (
    <div className="contentpage">
      <h3>Existing Templates:</h3>
      <TemplateList />
     
     <div>
     <h3>Create New Template:</h3>
      <CapabilityList /> 
      </div>
    
     </div>
     
  );
}

export default Template;