import './Template.css';
import FormatCapabilities from './FormatCapabilities';
import TemplateList from './Components/TemplateList';
import CapabilityList from './Components/CapabilityList';



function Template() {

  


  return (
    <div>
      <h3>Existing Templates</h3>
      <TemplateList />
     
     <div>
     <h3>Create New Templates</h3>
     
      <CapabilityList />
      
      </div>
      <div>
      <FormatCapabilities />
      </div>
     </div>
     
  );
}

export default Template;