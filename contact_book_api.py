from flask import Flask, request

from contact_book import ContactBook

app = Flask(__name__)
contact_book = ContactBook("/home/anmol/development/misc/Programs/contact_book.csv")


@app.route('/api/is_name_in_contact_book', methods=["GET"])
def is_name_in_contact_book():
    res = contact_book.is_name_in_contact_book(request.json["name"])

    return {"status": res}


@app.route("/api/add_contact", methods=["POST"])
def add_contact():
    data = request.json
    try:
        contact_book.add_contact(data["name"], data["contact_number"], data["email_id"], data["address"])
        return {"status": "OK"}, 200
    except Exception:
        return {"error": "Some error occurred"}, 400


if __name__ == '__main__':
    app.run(debug=True)
