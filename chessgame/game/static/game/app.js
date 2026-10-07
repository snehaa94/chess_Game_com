const boardEl = document.getElementById("board"),
  statusEl = document.getElementById("status"),
  movesEl = document.getElementById("moves");
const pieces = {
  P: "♙",
  N: "♘",
  B: "♗",
  R: "♖",
  Q: "♕",
  K: "♔",
  p: "♟",
  n: "♞",
  b: "♝",
  r: "♜",
  q: "♛",
  k: "♚",
};
let state = null,
  selected = null,
  flipped = false;
function csrf() {
  return (
    document.cookie
      .split("; ")
      .find((x) => x.startsWith("csrftoken="))
      ?.split("=")[1] || ""
  );
}
function parseFen(fen) {
  let rows = fen.split(" ")[0].split("/"),
    out = [];
  for (const row of rows) {
    let r = [];
    for (const c of row) {
      if (/[1-8]/.test(c)) for (let i = 0; i < +c; i++) r.push(null);
      else r.push(c);
    }
    out.push(r);
  }
  return out;
}
function squareName(r, c) {
  let rr = flipped ? 7 - r : r,
    cc = flipped ? 7 - c : c;
  return "abcdefgh"[cc] + (8 - rr);
}
function render() {
  const grid = parseFen(state.fen);
  boardEl.innerHTML = "";
  for (let r = 0; r < 8; r++)
    for (let c = 0; c < 8; c++) {
      const sq = document.createElement("div"),
        name = squareName(r, c);
      sq.className = "sq " + ((r + c) % 2 ? "dark" : "light");
      sq.dataset.sq = name;
      const p = grid[r][c];
      if (p) {
        const s = document.createElement("span");
        s.className =
          "piece " + (p === p.toUpperCase() ? "white-piece" : "black-piece");
        s.textContent = pieces[p];
        sq.appendChild(s);
      }
      if (selected === name) sq.classList.add("selected");
      if (state.legal_moves?.some((m) => m.startsWith(name)))
        sq.classList.add("legal");
      if (selected && state.legal_moves?.some((m) => m === selected + name))
        sq.classList.add("capture");
      sq.onclick = () => clickSquare(name);
      boardEl.appendChild(sq);
    }
  statusEl.textContent = state.status;
  movesEl.textContent = state.game_over
    ? state.result === "1-0"
      ? "White wins"
      : state.result === "0-1"
        ? "Computer wins"
        : "Draw"
    : state.turn === "white"
      ? "Your turn (White)"
      : "Computer is thinking…";
}
function clickSquare(name) {
  if (!state || state.game_over || state.turn !== "white") return;
  if (!selected) {
    if (state.legal_moves.some((m) => m.startsWith(name))) selected = name;
    render();
    return;
  }
  let uci = selected + name;
  let match = state.legal_moves.find((m) => m.startsWith(uci));
  if (!match) {
    selected = state.legal_moves.some((m) => m.startsWith(name)) ? name : null;
    render();
    return;
  }
  selected = null;
  makeMove(match);
}
async function makeMove(uci) {
  statusEl.textContent = "Computer is thinking…";
  try {
    const r = await fetch("/api/move/", {
      method: "POST",
      headers: { "Content-Type": "application/json", "X-CSRFToken": csrf() },
      body: JSON.stringify({ uci }),
    });
    const d = await r.json();
    if (!r.ok) throw Error(d.error || "Move failed");
    state = d;
    render();
  } catch (e) {
    statusEl.textContent = e.message;
    statusEl.classList.add("error");
  }
}
async function load() {
  const r = await fetch("/api/state/");
  state = await r.json();
  render();
}
document.getElementById("newGame").onclick = async () => {
  const r = await fetch("/api/new-game/", {
    method: "POST",
    headers: { "X-CSRFToken": csrf() },
  });
  state = await r.json();
  selected = null;
  render();
};
document.getElementById("flip").onclick = () => {
  flipped = !flipped;
  render();
};
load();
