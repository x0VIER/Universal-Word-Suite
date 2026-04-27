chrome.action.onClicked.addListener((tab) => {
  if (tab.url.includes("youtube.com/watch")) {
    console.log("Starting translation for:", tab.url);
    
    // Get cookies for YouTube
    chrome.cookies.getAll({ domain: "youtube.com" }, (cookies) => {
      // Format cookies for yt-dlp (Netscape format or similar)
      // Actually, we can just send the JSON and have the host convert it
      const cookieData = cookies.map(c => ({
        domain: c.domain,
        path: c.path,
        secure: c.secure,
        expirationDate: c.expirationDate,
        name: c.name,
        value: c.value,
        httpOnly: c.httpOnly
      }));

      const port = chrome.runtime.connectNative('com.rawcapture.yt');
      port.postMessage({ 
        action: "capture", 
        url: tab.url,
        cookies: cookieData
      });

      port.onMessage.addListener((msg) => {
        console.log("Received from host:", msg);
      });

      port.onDisconnect.addListener(() => {
        console.log("Disconnected from host");
      });
    });
  }
});
