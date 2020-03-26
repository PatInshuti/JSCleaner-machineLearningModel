
   
    // browser.runtime.sendMessage({URL : window.location.href}, function(response) {
       
    //     console.log("Response from Background script: ", response);
    // });
    var scripts = new Map();
    var defaultSettings = [];
    chrome.storage.local.get(['default'], function(result) {
      defaultSettings = result;
      browser.runtime.onMessage.addListener(request => {
        console.log("Message from the background script:", request);
        
        if (request.subject === "script"){
          console.log("ADD: ", request);

          if (!scripts.get(request.message.name)){
            if (request.message.label){
              scripts.set(request.message.name, {label:request.message.label.label, status:request.message.status })

            }
            else{
              scripts.set(request.message.name, {label:request.message.label, status:request.message.status })

            }
          }
        }
        if (request.subject === "updateScripts"){
          for (let element of request.message){
            console.log("UPDATE: ", element);
            if (scripts.get(element.name)){
              scripts.set(element.name, {label: element.label , status: defaultSettings[element.label]})
              console.log("updated")
            }
            
          }
          console.log("scripts", scripts); 
        }
      });
      
     

      document.addEventListener('DOMContentLoaded', (event) => {
        console.log("LOADED")
        browser.runtime.onMessage.addListener((msg, sender, response) => {
          // First, validate the message's structure.
          if ((msg.from === 'popup') && (msg.subject === 'DOMInfo')) {
            response(scripts);
          }
        });
        browser.runtime.sendMessage({
          from: 'content',
          subject: 'showPageAction',
        });
        
        
      });
      
    
    
    
    
    
    });
