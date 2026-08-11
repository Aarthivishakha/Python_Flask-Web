from setuptools import find_packages, setup


setup(
    name="flask-web-api",
    version="1.0.0",
    description="Flask REST API starter for Python 3.5",
    packages=find_packages(),
    python_requires=">=3.5,<3.6",
    install_requires=[
        "Flask==1.1.4",
        "Werkzeug==1.0.1",
        "Jinja2==2.11.3",
        "MarkupSafe==1.1.1",
        "itsdangerous==1.1.0",
        "click==7.1.2",
    ],
)
