(() => {
  const root = document.documentElement;
  const toggle = document.getElementById("theme-toggle");
  const icon = document.getElementById("theme-icon");
  const media = window.matchMedia("(prefers-color-scheme: dark)");

  function setTheme(theme, persist) {
    root.dataset.theme = theme;
    if (icon) icon.textContent = theme === "dark" ? "☀" : "☾";
    if (persist) {
      try { localStorage.setItem("roomizi-theme", theme); } catch (_) {}
    }
  }

  let savedTheme = null;
  try { savedTheme = localStorage.getItem("roomizi-theme"); } catch (_) {}
  setTheme(savedTheme || (media.matches ? "dark" : "light"), false);

  if (toggle) {
    toggle.addEventListener("click", () => {
      setTheme(root.dataset.theme === "dark" ? "light" : "dark", true);
    });
  }

  media.addEventListener?.("change", event => {
    let saved = null;
    try { saved = localStorage.getItem("roomizi-theme"); } catch (_) {}
    if (!saved) setTheme(event.matches ? "dark" : "light", false);
  });

  document.querySelectorAll(".flash-message").forEach(message => {
    window.setTimeout(() => {
      message.style.opacity = "0";
      window.setTimeout(() => message.remove(), 500);
    }, 5000);
  });
})();