from setuptools import setup, find_packages

setup(
    name="breadbox-api",
    version="1.0.0",
    description="Breadbox API - Flask application for managing facts and jokes",
    author="Anthony Woodcock",
    author_email="antoniobwoods2@gmail.com",
    py_modules=["breadboxapi", "apikeys"],
    install_requires=[
        "Flask==2.3.0",
        "mysql-connector-python==8.0.33",
        "requests==2.31.0",
        "waitress==3.0.2",
        "gunicorn==23.0.0",
        "pyinstaller==6.18.0",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "breadbox-api=breadboxapi:main",
        ],
    },
)
