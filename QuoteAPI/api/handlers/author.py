from api import app, db
from api.models.author import AuthorModel # type: ignore
from flask import abort, jsonify, request


@app.route("/authors", methods=['GET'])
def get_authors():
    raise NotImplemented("Метод не реализован")


@app.route("/authors", methods=['POST'])
def create_author():
    author_data = request.json
    author = AuthorModel(author_data.get('name', "Petr"))
    db.session.add(author)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(503, f"Database error: {str(e)}")
    # instance -> dict -> json
    return jsonify(author.to_dict()), 201
                   
        
@app.route("/authors/<int:author_id>", methods=['GET'])
def get_author_by_id(author_id: int):
    author = db.get_or_404(AuthorModel, author_id)
    # instance -> dict -> json
    return jsonify(author.to_dict()), 200   