# Zadatak 1 – Statična frontend aplikacija na Renderu

Jednostavna statična HTML/CSS/JS stranica (jelovnik restorana). Klijent (preglednik) šalje HTTP zahtjev
`GET /jelovnik.json`, poslužitelj vraća JSON, a `app.js` ga prikazuje.

## Javni URL

**https://rs-vjezbe-davor.onrender.com/**

## Datoteke

| Datoteka        | Opis                                |
| --------------- | ----------------------------------- |
| `index.html`    | ulazna stranica                     |
| `style.css`     | stilovi                             |
| `app.js`        | dohvat jelovnika (`fetch`) i prikaz |
| `jelovnik.json` | podaci koje poslužitelj vraća       |

## Lokalno pokretanje

`fetch` ne radi kad se `index.html` otvori direktno iz datoteke (`file://`), pa treba lokalni poslužitelj:

```bash
cd vjezbe_1/frontend_app
python -m http.server 8000
```

Zatim otvoriti http://localhost:8000

## Deployment (Render – Static Site)

| Postavka          | Vrijednost              |
| ----------------- | ----------------------- |
| Repository        | `davor-sk/RS_vjezbe`    |
| Branch            | `main`                  |
| Root Directory    | `vjezbe_1/frontend_app` |
| Build Command     | _(prazno)_              |
| Publish Directory | `.`                     |
