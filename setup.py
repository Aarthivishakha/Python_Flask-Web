from setuptools import find_packages, setup


setup(
    name="flask-web-api",
    version="1.0.0",
    description="Flask REST API starter for Python 3.4",
    packages=find_packages(),
    python_requires=">=3.4,<3.5",
    install_requires=[
        "Flask==1.0.4",
        "Werkzeug==0.16.1",
        "Jinja2==2.10.3",
        "MarkupSafe==1.1.1",
        "itsdangerous==1.1.0",
        "click==7.1.2",
    ],
)
