# Flask Web / REST API (Python 3.9)

Legacy Flask REST API with an application factory, blueprints, validation,
service-layer storage, tests, and version-aware analysis-tool metadata.

```bash
virtualenv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
python run.py
```

Endpoints: `GET /health` and CRUD at `/api/v1/items`.

Python 3.9 uses the current Flask 3.1 application structure. Some analysis tools
still require a newer interpreter and run in the isolated analyzer environment.
