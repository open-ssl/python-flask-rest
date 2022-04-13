Simple REST API with using Flask, SQLite3, SQLAlchemy

Commands for install:
- virtualvenv venv
- source venv/bin/activate
- pip install flask flask-jsonpify flask-sqlalchemy flask-restful
- pip freeze

Activate step by step:

1. DB activate
- sqlite3 chinbook.db
2. Activate venv (another tab)
- cd venv
- source bin/activate
3. Server activate
- python3 server.py
4. Call API

How to call API?

1. With using requests

import requests

# Get request
get_api = requests.get('http://127.0.0.1:5002/employees/2')

# Delete request
delete_api = requests.delete('http://127.0.0.1:5002/employees/2')

# Post request
post_api = requests.post('http://127.0.0.1:5002/employees/2')

# Put request
put_api = requests.put('http://127.0.0.1:5002/employees/2')


2 With using curl

# Get request
curl http://127.0.0.1:5002/employees/2

# Delete request
curl -X DELETE http://127.0.0.1:5002/employees/2 -H "Accept: application/json"

# Post request

curl -X POST http://127.0.0.1:5002/employees -H "Content-Type: application/json" -d '{
  "Address": "825 8 Ave SW",
  "BirthDate": "1958-12-08 00:00:00",
  "City": "City",
  "Country": "Country",
  "Email": "nancy@chinookcorp.com",
  "EmployeeId": 20,
  "Fax": "+1 (403) 262-3322",
  "FirstName": "Stas",
  "HireDate": "2002-05-01 00:00:00",
  "LastName": "LastName",
  "Phone": "+1 (403) 262-3443",
  "PostalCode": "T2P 2T3",
  "ReportsTo": 1,
  "State": "AB",
  "Title": "Sales Manager"}'

# Put request
