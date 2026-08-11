# Flask Web / REST API (Python 3.15 pre-release)

Legacy Flask REST API with an application factory, blueprints, validation,
service-layer storage, tests, and version-aware analysis-tool metadata.

```bash
virtualenv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
python run.py
```

Endpoints: `GET /health` and CRUD at `/api/v1/items`.

Python 3.15 uses the current Flask 3.1 application structure and modern typing.
Until Python 3.15 reaches its stable release, CI pins the current beta and the
Dockerfile uses the official rolling `3.15-rc-slim` pre-release image.
The complete analysis tool set runs in its isolated analyzer environment.
