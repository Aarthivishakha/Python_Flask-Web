# Flask Web / REST API (Python 3.16 development)

Legacy Flask REST API with an application factory, blueprints, validation,
service-layer storage, tests, and version-aware analysis-tool metadata.

```bash
virtualenv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
python run.py
```

Endpoints: `GET /health` and CRUD at `/api/v1/items`.

Python 3.16 uses the current Flask 3.1 application structure and modern typing.
This is an experimental development branch: Python 3.16 alpha 1 is scheduled
for October 2026. CI uses `3.16-dev`; because no official 3.16 Docker image
exists yet, the multi-stage Dockerfile builds the current CPython development
branch from source. Ruff checks against its newest available `py315` grammar.
The complete analysis tool set runs in its isolated analyzer environment.
