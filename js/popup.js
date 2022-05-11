async function getCurrentTab() {
  let queryOptions = { active: true, currentWindow: true };
  let [tab] = await chrome.tabs.query(queryOptions);
  return tab;
}

function genCard(title, publicationName, abstract, url) {
  return `
    <div class="card">
      <div class="card-header">
        Publisher: ${publicationName}
      </div>
      <div class="card-body">
        <h5 class="card-title">
          ${title}
        </h5>
        <p class="card-text">${abstract}</p>
        <a target="_blank" href="${url}" class="btn btn-primary">View paper</a>
      </div>
    </div>`;
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

      document.getElementById("selectedText").innerHTML = selectedText;

      let Http = new XMLHttpRequest();
      let url = "http://localhost:5000/ref?size=5&text=" + selectedText;
      Http.open("GET", url);
      Http.send();

      Http.onreadystatechange = (_event) => {
        if (Http.responseText.length == 0) {
          return;
        }

        let articles = JSON.parse(Http.responseText);
        let cards = "";
        articles.forEach((article) => {
          cards += genCard(
            article.title,
            article.publicationName,
            article.abstract,
            article.url
          );
        });
        document.getElementById("refrences").innerHTML = cards;
      };
    }
  );
});
