from setuptools import find_packages, setup


setup(
    name="flask-web-api",
    version="1.0.0",
    description="Flask REST API starter for Python 3.7",
    packages=find_packages(),
    python_requires=">=3.7,<3.8",
    install_requires=[
        "Flask==2.2.5",
        "Werkzeug==2.2.3",
        "Jinja2==3.1.2",
        "MarkupSafe==2.1.3",
        "itsdangerous==2.1.2",
        "click==8.1.7",
    ],
)
