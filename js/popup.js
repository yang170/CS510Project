// Grab the button
let changeColor = document.getElementById("changeColor");

// Set button color
chrome.storage.sync.get("color", ({ color }) => {
  changeColor.style.backgroundColor = color;
});

// When the button is clicked, inject setPageBackgroundColor into current page
changeColor.addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    function: setPageBackgroundColor,
  });
});

// The body of this function will be executed as a content script inside the
// current page
function setPageBackgroundColor() {
  chrome.storage.sync.get("color", ({ color }) => {
    document.body.style.backgroundColor = color;
  });
}

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
    (injectionResults) => {
      console.log(injectionResults);
      document.getElementById("selectedText").innerHTML =
        injectionResults[0].result;
    }
  );
});
