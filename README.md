# Lavanya

Upload an Audio file, and save it into your computer (UUID-based).

## Requirements

- Python Interpreter (3.8+ preferred).
- Virtualenv (For holding project-specific isolated libraries).

## Installation

Create a virtual environment to run the application.

```sh
virtualenv -p python3 venv
```

Enter Virtual Environment

```sh
# For macOS or Linux
source venv/bin/activate
```

```powershell
# For Windows
.\venv\Scripts\activate.ps1
```

Install Libraries

```sh
pip install -r requirements.txt
```

## Start Server

Run the following command to start the server

```sh
FLASK_APP=lavanya flask run
```

## License

Copyright (c) 2022 [Goutham Krishna K V](https://gouthamkrishnakv.pages.dev). All Rights Reserved.

[GNU Affero General Public License 3.0](LICENSE)
