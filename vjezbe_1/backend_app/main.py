from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

jelovnik = [
    {"id": 1, "naziv": "Riblja juha", "cijena": 6.0},
    {"id": 2, "naziv": "Fuži s tartufima", "cijena": 18.0},
    {"id": 3, "naziv": "Pljukanci s kozicama", "cijena": 16.5},
    {"id": 4, "naziv": "Fritule", "cijena": 5.0},
]

narudzbe = []


class Narudzba:
    def __init__(self, ime, jelo_id, kolicina):
        if not isinstance(ime, str):
            raise ValueError("ime mora biti tekst")
        if not isinstance(jelo_id, int):
            raise ValueError("jelo_id mora biti cijeli broj")
        if not isinstance(kolicina, int):
            raise ValueError("kolicina mora biti cijeli broj")

        self.ime = ime
        self.jelo_id = jelo_id
        self.kolicina = kolicina


@app.get("/")
def pocetna():
    return {"poruka": "Poslužitelj radi!"}


@app.get("/jelovnik")
def dohvati_jelovnik():
    return jelovnik


@app.get("/jelovnik/{jelo_id}")
def dohvati_jelo(jelo_id: int):
    for jelo in jelovnik:
        if jelo["id"] == jelo_id:
            return jelo
    raise HTTPException(status_code=404, detail="Jelo ne postoji")


@app.get("/narudzbe")
def dohvati_narudzbe():
    return narudzbe


@app.post("/narudzbe", status_code=201)
def dodaj_narudzbu(podaci: dict):
    for polje in ["ime", "jelo_id", "kolicina"]:
        if polje not in podaci:
            raise HTTPException(status_code=422, detail=f"Nedostaje polje: {polje}")

    try:
        narudzba = Narudzba(podaci["ime"], podaci["jelo_id"], podaci["kolicina"])
    except ValueError as greska:
        raise HTTPException(status_code=422, detail=str(greska))

    nova = {
        "id": len(narudzbe) + 1,
        "ime": narudzba.ime,
        "jelo_id": narudzba.jelo_id,
        "kolicina": narudzba.kolicina,
    }
    narudzbe.append(nova)
    return nova
