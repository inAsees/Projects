from flask import Flask, request
from contact_book_core import ContactBook

app = Flask(__name__)
contact_book = ContactBook(r"C:\Users\DELL\Desktop\test files\contact_book.csv")


@app.route("/api/add_contact", methods=["POST"])
def add_contact():
    data = request.json
    if contact_book.is_name_in_contact_book(data["name"]):
        return {"status": "Name already exits,try different name."}, 400

    try:
        contact_book.add_contact(data["name"], data["contact_number"], data["email_id"], data["address"])
        return {"status": "Contact added successfully"}, 200
    except Exception:
        return {"error": "Some error occurred"}, 400


@app.route('/api/edit_contact', methods=["POST"])
def edit_contact():
    data = request.json
    if not contact_book.is_name_in_contact_book(data["name"]):
        return {"status": "Name does not exist."}, 400

    try:
        contact_book.edit_contact(data["name"], data["new_name"], data["new_contact_number"], data["new_email_id"],
                                  data["new_address"])
        return {"status": "Contact updated successfully"},200
    except Exception:
        return {"error": "Some error occurred"}, 400


@app.route('/api/delete_contact', methods=["POST"])
def delete_contact():
    data = request.json
    if not contact_book.is_name_in_contact_book(data["name"]):
        return {"status": "Name does not exist."}, 400
    contact_book.delete_contact(data["name"])
    return {"status": "Contact deleted successfully."},200


@app.route('/api/search_contact', methods=["POST"])
def search_contact():
    data = request.json
    if not contact_book.is_name_in_contact_book(data["name"]):
        return {"status": "Name does not exists."}, 400
    contact = contact_book.search_contact(data["name"])
    return contact[0],200


@app.route('/api/display_contact_book', methods=["GET"])
def display_contact_book():
    contact = contact_book.display_contact_book()
    return {"contacts": contact}


if __name__ == '__main__':
    app.run(debug=True)
