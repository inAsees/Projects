from typing import Optional
import mysql.connector as connection
from mysql.connector import MySQLConnection


class ContactBook:
    def __init__(self):
        self._connection = self._get_db_connection()

    def add_contact(self, name: str, contact_number: str, email_id: str, address: str) -> bool:
        if self._is_name_in_contact_book(name):
            return True
        cur = self._connection.cursor(buffered=True)
        query = "INSERT INTO contact_book.contacts(name,contact_number,email_id,address) values(%s,%s,%s,%s)"
        val = (name, contact_number, email_id, address)
        cur.execute(query, val)
        self._connection.commit()

    def search_contact(self, name: str) -> Optional[list[tuple]]:
        if not self._is_name_in_contact_book(name):
            return None
        cur = self._connection.cursor(buffered=True)
        cur.execute("SELECT * FROM contact_book.contacts WHERE Name = %s", (name,))
        return cur.fetchall()

    def edit_contact(self, name: str, new_name: Optional[str], new_contact_number: Optional[str],
                     new_email_id: Optional[str],
                     new_address: Optional[str]) -> bool:
        if not self._is_name_in_contact_book(name):
            return True
        cur = self._connection.cursor(buffered=True)
        cur.execute("SELECT * FROM contact_book.contacts WHERE name = %s", (name,))
        row = cur.fetchall()
        if new_name is not None:
            cur.execute("UPDATE contact_book.contacts SET name = %s WHERE name = %s", (new_name, name))
        if new_contact_number is not None:
            cur.execute("UPDATE contact_book.contacts SET contact_number = %s WHERE contact_number = %s",
                        (new_contact_number, row[0][2]))
        if new_email_id is not None:
            cur.execute("UPDATE contact_book.contacts SET email_id = %s WHERE email_id = %s",
                        (new_email_id, row[0][3]))
        if new_address is not None:
            cur.execute("UPDATE contact_book.contacts SET address = %s WHERE address = %s",
                        (new_address, row[0][4]))
        self._connection.commit()

    def delete_contact(self, name: str) -> bool:
        if not self._is_name_in_contact_book(name):
            return True
        cur = self._connection.cursor(buffered=True)
        cur.execute("DELETE FROM contact_book.contacts where name = %s", (name,))
        self._connection.commit()

    def display_contact_book(self) -> Optional[list[tuple]]:
        cur = self._connection.cursor(buffered=True)
        cur.execute("SELECT * FROM contact_book.contacts ORDER BY name")
        contacts_list = cur.fetchall()
        if len(contacts_list) == 0:
            return None
        return contacts_list

    def _is_name_in_contact_book(self, name: str) -> bool:
        cur = self._connection.cursor(buffered=True)
        cur.execute("SELECT * FROM contact_book.contacts WHERE Name = %s", (name,))
        if len(cur.fetchall()) == 0:
            return False
        return True

    @staticmethod
    def _get_db_connection() -> Optional[MySQLConnection]:
        try:
            conn = connection.connect(host="127.0.0.1", username="root", password="mysql", use_pure=True,
                                      database="contact_book")
        except Exception as e:
            print(e)
            return None
        return conn
