document.getElementById('translateBtn').addEventListener('click', async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  
  if (!tab.url.includes("youtube.com/watch")) {
    document.getElementById('status').textContent = "Not a YouTube video!";
    document.getElementById('status').style.color = "#cf6679";
    return;
  }

  document.getElementById('status').textContent = "Initializing Bridge...";
  document.getElementById('translateBtn').disabled = true;
  document.getElementById('progressContainer').style.display = "block";

  chrome.runtime.sendMessage({ action: "translate_current_video", url: tab.url }, (response) => {
    console.log("Response:", response);
  });
});

chrome.runtime.onMessage.addListener((message) => {
  if (message.action === "vts_progress") {
    const data = message.data;
    const statusEl = document.getElementById('status');
    const barEl = document.getElementById('progressBar');

    if (data.status === "downloading") {
      statusEl.textContent = "Downloading Audio (Silent)...";
      barEl.style.width = "25%";
    } else if (data.status === "transcribing") {
      statusEl.textContent = "Transcribing (AI Mode)...";
      barEl.style.width = "60%";
    } else if (data.status === "translating") {
      statusEl.textContent = "Applying Translation...";
      barEl.style.width = "85%";
    } else if (data.status === "complete") {
      statusEl.textContent = "Success! Output Ready.";
      barEl.style.width = "100%";
      document.getElementById('translateBtn').disabled = false;
      statusEl.style.color = "#03dac6";
    }
  } else if (message.action === "vts_error") {
    document.getElementById('status').textContent = "Error: " + message.error;
    document.getElementById('status').style.color = "#cf6679";
    document.getElementById('translateBtn').disabled = false;
  }
});
