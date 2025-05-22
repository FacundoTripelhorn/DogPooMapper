# Dog‑Poop Map 🐶💩

Track where each dog goes poop in your yard. The system captures events with YOLOv8, stores them via FastAPI + SQLModel, and visualises them later. You can run everything with Docker or directly on your laptop.

---

## 1. Prerequisites

- Python 3.10 or newer (only if you’ll run natively)
- Git
- Docker Desktop (optional but recommended)

---

## 2. Environment variables

Copy the template and adjust if needed:

```bash
cp .env.example .env      # On Windows, copy it manually
```

By default the app uses SQLite at `data/poop.db`. Change `POOP_DB` if you prefer Postgres.

---

## 3. Native installation

### 3.1 Windows (PowerShell)

```powershell
py -3 -m venv .venv              # create virtual‑env
.\.venv\Scripts\Activate.ps1     # activate it
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload  # http://localhost:8000/docs
```

> **Execution‑policy error?** Run once as Administrator:
>
> ```powershell
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### 3.2 Windows (CMD)

```cmd
py -3 -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r backend\requirements.txt
uvicorn backend.app.main:app --reload
```

### 3.3 macOS / Linux (bash/zsh)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload
```

---

## 4. Docker installation (recommended)

1. Install Docker Desktop.
2. Copy `.env.example` to `.env`.
3. Edit `config/frigate.yml` with your RTSP camera credentials.
4. Launch the stack:

```bash
docker compose up --build
```

- API docs → <http://localhost:8000/docs>
- Frigate UI → <http://localhost:5000>

Stop with `Ctrl‑C`, then `docker compose down`.

---

## 5. Run tests

```bash
# Inside the virtual‑env
pytest -q backend/app/tests
```

---

## 6. Next steps

1. Open Swagger UI and make sure `POST /events/` and `GET /events/` are visible.
2. Send a sample event; a new file `data/poop.db` should appear.
3. Train your YOLOv8 **pooping‑dog** model and push detections via `services/detector.py`.
4. Build a heat‑map visualiser or hook Grafana.

Happy coding! 🐾
