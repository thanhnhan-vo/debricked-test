import sqlite3

# Example of an unsafe SQLite connection and query
def unsafe_login(username, password):
    # Establish connection to the SQLite database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # UNSAFE SQL query (vulnerable to SQL Injection)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    # Execute the query
    cursor.execute(query)
    result = cursor.fetchone()
    
    # If a user is found, login successful
    if result:
        print("Login successful!")
    else:
        print("Login failed!")
    
    # Close the connection
    conn.close()

# Example usage
unsafe_login("admin", "' OR '1'='1")
