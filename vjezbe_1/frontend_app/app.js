// Klijent šalje HTTP zahtjev poslužitelju (Render) i prikazuje primljeni JSON.
const statusEl = document.getElementById("status");
const jelovnikEl = document.getElementById("jelovnik");
const filteriEl = document.getElementById("filteri");
const httpInfoEl = document.getElementById("http-info");

let jelovnik = [];

async function dohvatiJelovnik() {
  try {
    const odgovor = await fetch("jelovnik.json");
    httpInfoEl.textContent = `Odgovor poslužitelja: ${odgovor.status} ${odgovor.statusText || ""} · ${odgovor.headers.get("content-type") ?? ""}`;

    if (!odgovor.ok) {
      throw new Error(`HTTP ${odgovor.status}`);
    }

    jelovnik = await odgovor.json();
    statusEl.hidden = true;
    prikaziFiltere();
    prikaziJelovnik("Sve");
  } catch (greska) {
    statusEl.textContent = `Jelovnik nije moguće učitati (${greska.message}).`;
    statusEl.classList.add("greska");
  }
}

function prikaziFiltere() {
  const kategorije = ["Sve", ...new Set(jelovnik.map((jelo) => jelo.kategorija))];
  filteriEl.innerHTML = "";
  for (const kategorija of kategorije) {
    const gumb = document.createElement("button");
    gumb.textContent = kategorija;
    gumb.setAttribute("aria-pressed", kategorija === "Sve");
    gumb.addEventListener("click", () => {
      filteriEl.querySelectorAll("button").forEach((b) => b.setAttribute("aria-pressed", b === gumb));
      prikaziJelovnik(kategorija);
    });
    filteriEl.appendChild(gumb);
  }
}

function prikaziJelovnik(odabrana) {
  const jela = odabrana === "Sve" ? jelovnik : jelovnik.filter((j) => j.kategorija === odabrana);
  const poKategoriji = Map.groupBy
    ? Map.groupBy(jela, (j) => j.kategorija)
    : jela.reduce((m, j) => m.set(j.kategorija, [...(m.get(j.kategorija) ?? []), j]), new Map());

  jelovnikEl.innerHTML = "";
  for (const [kategorija, stavke] of poKategoriji) {
    const sekcija = document.createElement("div");
    sekcija.className = "kategorija";
    sekcija.innerHTML = `<h2>${kategorija}</h2>`;
    for (const jelo of stavke) {
      const red = document.createElement("article");
      red.className = "jelo";
      red.innerHTML = `
        <div>
          <h3>${jelo.naziv}</h3>
          <p>${jelo.opis}</p>
        </div>
        <span class="cijena">${jelo.cijena.toFixed(2).replace(".", ",")} €</span>`;
      sekcija.appendChild(red);
    }
    jelovnikEl.appendChild(sekcija);
  }
}

dohvatiJelovnik();
