import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="dict",
   user="dict",
   password="abc123"
)

# read_dict: returns the list of all dictionary entries:
#   argument: C - the database connection
def read_dict(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows

# add_word: adds a word and its translation to the list
#   argument: C - the database connection
#   argument: word - the English word to be added to the listz
#   argument: translation - translation of the word into Swedish
def add_word(conn, word, translation):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()

# delete_word: removes a word from the list
#   argument: C - the database connection
#   argument: ID - the database ID of the word to be removed 
def delete_word(conn, ID):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()

# save_dict: commits all changes to the database
#   argument: C - the database connection
def save_dict(conn):
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close()


print("Welcome to the dictionary!")
print("Available commands are 'list', 'add', 'delete' and 'quit'")
while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print("Listing the dictionary:")
        rows = read_dict(conn)
        for i, wd, trans in rows:
            print(f"{i}: {wd} - {trans}")
    elif cmd == "add":
        word = input("  Word: ")
        trans = input("  Translation: ")
        add_word(conn, word, trans)
        print(f" Added word {word}")
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
        print(f" Deleted the word with ID {ID}")
    elif cmd == "quit":
        print("Saving the changes.")
        save_dict(conn)
        break

print("-----Goodbye!-----")
