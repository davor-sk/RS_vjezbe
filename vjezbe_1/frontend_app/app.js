const API_URL = "https://rs-vjezbe-davor-api.onrender.com";

async function ucitajJelovnik() {
  const odgovor = await fetch(API_URL + "/jelovnik");
  const jelovnik = await odgovor.json();

  const lista = document.getElementById("jelovnik");
  const izbornik = document.getElementById("jelo");
  lista.innerHTML = "";

  for (const jelo of jelovnik) {
    lista.innerHTML += `<li>${jelo.naziv} – ${jelo.cijena} €</li>`;
    izbornik.innerHTML += `<option value="${jelo.id}">${jelo.naziv}</option>`;
  }
}

async function ucitajNarudzbe() {
  const odgovor = await fetch(API_URL + "/narudzbe");
  const narudzbe = await odgovor.json();

  const lista = document.getElementById("narudzbe");
  lista.innerHTML = "";

  for (const n of narudzbe) {
    lista.innerHTML += `<li>#${n.id} – ${n.ime}: jelo ${n.jelo_id}, količina ${n.kolicina}</li>`;
  }
}

document.getElementById("forma").addEventListener("submit", async (event) => {
  event.preventDefault();

  const narudzba = {
    ime: document.getElementById("ime").value,
    jelo_id: Number(document.getElementById("jelo").value),
    kolicina: Number(document.getElementById("kolicina").value),
  };

  const odgovor = await fetch(API_URL + "/narudzbe", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(narudzba),
  });

  const poruka = document.getElementById("poruka");
  if (odgovor.status === 201) {
    poruka.textContent = "Narudžba je poslana!";
    ucitajNarudzbe();
  } else {
    poruka.textContent = "Greška: " + odgovor.status;
  }
});

ucitajJelovnik();
ucitajNarudzbe();
