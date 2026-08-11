from setuptools import find_packages, setup


setup(
    name="flask-web-api",
    version="1.0.0",
    description="Flask REST API starter for Python 2.6",
    packages=find_packages(),
    install_requires=[
        "Flask==0.12.5",
        "Werkzeug==0.14.1",
        "Jinja2==2.10.1",
        "MarkupSafe==1.1.1",
        "itsdangerous==0.24",
        "click==6.7",
    ],
)
