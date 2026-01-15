# Breadbox API

A Flask-based REST API for managing facts and jokes with MySQL backend.

## Installation

### Prerequisites
- Python 3.7 or higher
- MySQL server running locally
- Git (optional)

### Setup

1. Clone or download this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure your database credentials in `apikeys.py`:
   ```python
   BREADID = "your_mysql_user"
   BREADPW = "your_mysql_password"
   ```

6. Run the application:
   ```bash
   python breadboxapi.py
   ```

The API will be available at `http://localhost:5000`

## API Endpoints

### GET Endpoints
- `/v1/breadbox` - Get random fact or joke
- `/getTable` - List all available tables
- `/facts` - Get all facts
- `/jokes` - Get all jokes
- `/facts/<id>` - Get specific fact by ID
- `/jokes/<id>` - Get specific joke by ID
- `/export/facts` - Export facts to JSON
- `/export/jokes` - Export jokes to JSON
- `/export/all` - Export all data to JSON

### POST Endpoints
- `/addFact` - Add a new fact
- `/addJoke` - Add a new joke

### PUT Endpoints
- `/updateFacts` - Update a fact
- `/updateJokes` - Update a joke

### DELETE Endpoints
- `/deleteFact/<id>` - Delete a fact
- `/deleteJoke/<id>` - Delete a joke

## Packaging

### For distribution:
```bash
python setup.py sdist bdist_wheel
```

This creates distributable packages in the `dist/` folder.

### To install locally:
```bash
pip install -e .
```

## Creating an Executable (Windows)

To create a standalone `.exe` file:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the executable:
   ```bash
   pyinstaller --onefile breadboxapi.py
   ```

The `.exe` will be in the `dist/` folder.
