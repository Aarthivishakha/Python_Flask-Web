from setuptools import find_packages, setup


setup(
    name="flask-web-api",
    version="1.0.0",
    description="Flask REST API starter for Python 2.7",
    packages=find_packages(),
    install_requires=[
        "Flask==1.1.4",
        "Werkzeug==1.0.1",
        "Jinja2==2.11.3",
        "MarkupSafe==2.0.1",
        "itsdangerous==1.1.0",
        "click==7.1.2",
    ],
)
