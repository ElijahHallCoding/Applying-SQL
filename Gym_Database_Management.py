from connect_mysql import connect_database

# Task 1: Add a Member
def add_member(id, name, age):
    """
    Adds a new member to the 'Members' table.
    This will also handle duplicate ID and constraint violations.
    """
    conn = connect_database()
    if conn is not None: 
        try:
            cursor = conn.cursor()
            sql_query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            cursor.execute(sql_query, (id, name, age))
            conn.commit()
            print(f"Member {name} added successfully.")
        except Exception as e:
            print(f"Error while adding member: {e}")
        finally:
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")
            

# Task 2: Add a Workout Session
def add_workout_session(session_id, member_id, session_date, session_time, activity):
    """
    Adds a new workout session to the 'WorkoutSessions' table.
    Handles invalid member ID and constraint violations.
    """
    conn = connect_database()
    if conn is not None: 
        try:
            cursor = conn.cursor()
            # Check if the member exists
            cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
            member = cursor.fetchone()
            if member is None:
                raise ValueError(f"Member ID {member_id} does not exist.")
            
            sql_query = """
                INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql_query, (session_id, member_id, session_date, session_time, activity))
            conn.commit()
            print("Workout session added successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error while adding workout session: {e}")
        finally:
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")

# Task 3: Updating Member Information
def update_member_age(member_id, new_age):
    """
    Updates the age of an existing member.
    Checks if the member exists before updating.
    """
    conn = connect_database()
    if conn is not None: 
        try:
            cursor = conn.cursor()
            # Check if the member exists
            cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
            member = cursor.fetchone()
            if member is None:
                raise ValueError(f"Member ID {member_id} does not exist.")
            
            sql_query = "UPDATE Members SET age = %s WHERE id = %s"
            cursor.execute(sql_query, (new_age, member_id))
            conn.commit()
            print(f"Member ID {member_id}'s age updated to {new_age}.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error while updating member age: {e}")
        finally:
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    """
    Deletes a workout session based on session ID.
    Handles cases where the session ID does not exist.
    """
    conn = connect_database()
    if conn is not None: 
        try:
            cursor = conn.cursor()
            # Check if the session exists
            cursor.execute("SELECT * FROM WorkoutSessions WHERE session_id = %s", (session_id,))
            session = cursor.fetchone()
            if session is None:
                raise ValueError(f"Session ID {session_id} does not exist.")
            
            sql_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(sql_query, (session_id,))
            conn.commit()
            print(f"Workout session ID {session_id} deleted successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error while deleting workout session: {e}")
        finally:
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")

#  Function Calls
def main():
    print("Adding a member...")
    add_member(5, 'New Member', 29)
    
    print("Adding a workout session...")
    add_workout_session(5, 5, '2024-08-30', '10:00 AM', 'Pilates')
    
    print("Updating member age...")
    update_member_age(5, 30)
    
    print("Deleting a workout session...")
    delete_workout_session(5)

if __name__ == "__main__":
    main()