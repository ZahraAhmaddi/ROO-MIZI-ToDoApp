(() => {
  const root = document.documentElement;
  const toggle = document.getElementById("theme-toggle");
  const icon = document.getElementById("theme-icon");
  const media = window.matchMedia("(prefers-color-scheme: dark)");
  const $ = id => document.getElementById(id);

  function sp(grid, palette, scale) {
    const height = grid.length, width = grid[0].length;
    let rects = "";
    grid.forEach((line, y) => {
      let x = 0;
      while (x < width) {
        const char = line[x];
        if (char === "." || !palette[char]) { x++; continue; }
        let end = x;
        while (end < width && line[end] === char) end++;
        rects += `<rect x="${x}" y="${y}" width="${end-x}" height="1.02" style="fill:${palette[char]}"/>`;
        x = end;
      }
    });
    return `<svg viewBox="0 0 ${width} ${height}" width="${width*scale}" height="${height*scale}" shape-rendering="crispEdges" aria-hidden="true">${rects}</svg>`;
  }

  const CAT_SIT = [".oo......oo...",".oooooooooo...","oooooooooooo..","ooeooooooeoo..","oooooppooooo..",".oooooooooo...",".oooooooooo.oo",".ooowwwwooo.oo",".ooowwwwooo.oo",".ooowwwwoooooo",".ooowwwwooo... ",".oowwooowwoo.."];
  const CAT_SLP = ["o..o............","oooo.....ooo....","ooooooooooooooo.","oxxooooooooooooo","ooppoooooooooooo","oooooooooooooooo",".ooooooooooooooo","..oooooooooowwww"];
  const CAT_AWK = ["o..o............","oooo.....ooo....","ooooooooooooooo.","oeoooooooooooooo","ooppoooooooooooo","oooooooooooooooo",".ooooooooooooooo","..oooooooooowwww"];
  const FERN = [".....gg.....","..g..gg..g..",".ggg.gg.ggg.",".gGgggggGgg.","..ggGggGgg..","...gggggg...",".....gG.....","..rrrrrrrr..","..rbbbbbbr..","...bbbbbb...","...bBbbbb...","...bbbbbb...","....bbbb...."];
  const ROSE = ["....pppp....","...ppPPpp...","...pPppPp...","...ppPPpp...","....pppp....",".....gg.....","..gg.gg.gg..","..ggggggg...",".....gg.....","..rrrrrrrr..","..rbbbbbbr..","...bbbbbb...","...bBbbbb...","...bbbbbb...","....bbbb...."];
  const v = name => `var(--${name})`;

  function renderPixelScene() {
    const scene = $("scene");
    if (!scene) return;
    const dark = root.dataset.theme === "dark";
    const A = {o:v("catA"),x:v("catAx"),p:v("pk"),w:v("cw"),e:v("eye")};
    const B = {o:v("catB"),x:v("catBx"),p:v("pk"),w:v("cw"),e:v("eye")};
    const fern = sp(FERN,{g:v("gr"),G:v("gd"),r:v("p1r"),b:v("p1"),B:v("p1r")},7);
    const rose = sp(ROSE,{p:v("rose"),P:v("rosed"),g:v("gr"),r:v("p2r"),b:v("p2"),B:v("p2r")},7);
    const z = '<span class="z">z</span><span class="z">z</span>';
    scene.innerHTML =
      `<div class="pet">${fern}</div>` +
      (dark ? `<div class="pet">${sp(CAT_SLP,A,7)}${z}</div>` : `<div class="pet awake">${sp(CAT_SIT,A,7)}</div>`) +
      `<div class="pet">${rose}</div>` +
      (dark ? `<div class="pet flip">${sp(CAT_SLP,B,6)}${z}</div>` : `<div class="pet">${sp(CAT_AWK,B,6)}</div>`);
  }

  function setTheme(theme, persist) {
    root.dataset.theme = theme;
    if (icon) icon.textContent = theme === "dark" ? "☀" : "☾";
    renderPixelScene();
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