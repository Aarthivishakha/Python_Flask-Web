from setuptools import find_packages, setup


setup(
    name="flask-web-api",
    version="1.0.0",
    description="Flask REST API starter for Python 3.6",
    packages=find_packages(),
    python_requires=">=3.6,<3.7",
    install_requires=[
        "Flask==2.0.3",
        "Werkzeug==2.0.3",
        "Jinja2==3.0.3",
        "MarkupSafe==2.0.1",
        "itsdangerous==2.0.1",
        "click==8.0.4",
    ],
)
