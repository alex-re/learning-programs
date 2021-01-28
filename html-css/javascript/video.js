ev => {
    // Maximize the standalone video when pressing F11,
    // but ignore audio elements
    if (
      ev.key == "F11" &&
      videoElement.videoWidth != 0 &&
      videoElement.videoHeight != 0
    ) {
      // If we're in browser fullscreen mode, it means the user pressed F11
      // while browser chrome or another tab had focus.
      // Don't break leaving that mode, so do nothing here.
      if (window.fullScreen) {
        return;
      }
  
      // If we're not in browser fullscreen mode, prevent entering into that,
      // so we don't end up there after pressing Esc.
      ev.preventDefault();
      ev.stopPropagation();
  
      if (!document.fullscreenElement) {
        videoElement.requestFullscreen();
      } else {
        document.exitFullscreen();
      }
    }
  }