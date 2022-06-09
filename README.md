# Dict

The program maintains a short English-Swedish dictionary

The available commands are:

- list
- add
- delete
- quit

## Database connection

The program uses a PostgreSQL database to store the dictionary list. The database and a user role had were created separately in psql, and the file dict.sql was run against it in order to create a table and populate it with a few words.
