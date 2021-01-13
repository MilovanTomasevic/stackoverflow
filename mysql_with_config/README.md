Install dependencies:

```sh
pip install -r requirements.txt
```

Code:
```py
from python_mysql_dbconfig import read_db_config
from db_lib import MySQLDataBase


if __name__ == "__main__":
    conn = MySQLDataBase().connection(read_db_config())

    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")

    row = cursor.fetchone()
    print("Server version:", row[0])

    cursor.close()
    conn.close()
    print("Connection closed.")
```

Run:
```sh
python test.py
```

Output:
```sh
Connecting to MySQL database...
Connection established.
Server version: 8.0.22
Connection closed.
```
