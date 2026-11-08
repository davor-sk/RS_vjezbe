# Backend – REST API u FastAPI-ju (Zadatak 2)

## Javni URL

https://rs-vjezbe-davor-api.onrender.com/

Dokumentacija (Swagger): https://rs-vjezbe-davor-api.onrender.com/docs

## Endpointi

| Metoda | Putanja | Opis |
|---|---|---|
| GET | `/` | provjera radi li poslužitelj |
| GET | `/jelovnik` | sva jela |
| GET | `/jelovnik/{id}` | jedno jelo (404 ako ne postoji) |
| GET | `/narudzbe` | sve narudžbe |
| POST | `/narudzbe` | nova narudžba |

## Lokalno pokretanje

```
pip install -r requirements.txt
uvicorn main:app --reload
```

Zatim otvoriti http://localhost:8000/docs

## Render postavke (Web Service)

- Root Directory: `vjezbe_1/backend_app`
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

## Testiranje s curl

```
curl https://rs-vjezbe-davor-api.onrender.com/jelovnik
curl https://rs-vjezbe-davor-api.onrender.com/jelovnik/2
curl -X POST https://rs-vjezbe-davor-api.onrender.com/narudzbe -H "Content-Type: application/json" -d "{\"ime\": \"Davor\", \"jelo_id\": 2, \"kolicina\": 1}"
curl https://rs-vjezbe-davor-api.onrender.com/narudzbe
```

(POST naredba je napisana za Windows Command Prompt.)

## Testiranje s Postmanom

Import → `Konoba_RS_API.postman_collection.json`
