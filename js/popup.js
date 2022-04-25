async function getCurrentTab() {
  let queryOptions = { active: true, currentWindow: true };
  let [tab] = await chrome.tabs.query(queryOptions);
  return tab;
}

getCurrentTab().then((res) => {
  let tabId = res.id;

  function grab() {
    return window.getSelection().toString();
  }

  chrome.scripting.executeScript(
    {
      target: { tabId: tabId },
      func: grab,
    },
    (selection) => {
      selectedText = selection[0].result;

      // if nothing is selected
      if (selectedText === "") {
        document.getElementById("selectedText").innerHTML =
          "Please select some text";
        document.getElementById("refrences").innerHTML = "No references found";
        return;
      }

      console.log(selection);
      document.getElementById("selectedText").innerHTML = selectedText;

      const Http = new XMLHttpRequest();
      const url = "http://localhost:5000/ref?text=" + selectedText;
      Http.open("GET", url);
      Http.send();

      Http.onreadystatechange = (_event) => {
        // TODO: error handling
          res = Http.responseText;
          res_json = JSON.parse(res)
          let str = "";
          for (let i = 0; i < 10; i++) {
              str += "<li>" + "Title: " + res_json[i].title + "<br>" + "<br>"
                  + "Publication Name: " + res_json[i].publicationName + "<br>" + "<br>"
                  + "Abstract: " + res_json[i].abstract + "<br>" + "<br>"
                  + "Url: " + res_json[i].url + "<br>" + "<br>" + "</li>";
          } 
          document.getElementById("refrences").innerHTML = str
          
      };
    }
  );
});
