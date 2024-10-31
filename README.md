<p align="center">
  <img src="/static_dev/favicon/logo_no_text.svg">
</p>

<h3 align="center">KeraTech</h3>


## Quick start

### Clone the repository:
```bash
git clone https://github.com/dino-mayk/Keratech.git
```

### Create a virtual environment:

Windows:
```bash
python -m venv venv
```
Mac, Linux:
```bash
python3 -m venv venv
```

### Activate the virtual environment:

Windows:
```bash
cd venv/Scripts/
```
```bash
.\activate
```
Mac, Linux:
```bash
source venv/bin/activate
```

### Install dependencies:

Windows:
```bash
pip install -r requirements.txt
```
Mac, Linux:
```bash
pip3 install -r requirements.txt
```

### Run postgres container:

```bash
docker run -d -p 5432:5432 --name postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres postgres:latest
```

#### Django server:

Windows:
```bash
python manage.py runserver
```
Mac, Linux:
```bash
python3 manage.py runserver
```