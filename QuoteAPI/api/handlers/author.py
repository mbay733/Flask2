from http import HTTPStatus
from api import app, db
from api.models.author import AuthorModel # type: ignore
from flask import abort, jsonify, request
from api.schemas.author import author_schema, authors_schema

@app.get("/authors")
def get_authors():
    authors_db = db.session.scalars(db.select(AuthorModel)).all()
    return jsonify(authors_schema.dump(authors_db)), 200


@app.route('/authors', methods=['POST'])
def create_author():
    author_data = request.json
    author = AuthorModel(**author_data)
    db.session.add(author)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(503, f'Database error: {str(e)}')
    return jsonify(author.to_dict()), 201
                   
        
@app.route("/authors/<int:author_id>", methods=['GET'])
def get_author_by_id(author_id: int):
    author = db.get_or_404(AuthorModel, author_id)
    # instance -> dict -> json
    return jsonify(author.to_dict()), 200   

@app.route("/authors/<int:author_id>", methods=["PUT"])
def edit_author(author_id):
    author: AuthorModel = db.get_or_404(AuthorModel, author_id)

    data: dict = request.json

    if len(data) == 0:
        return "No valid data to update", HTTPStatus.BAD_REQUEST

    try:
        for key, value in data.items():
            if not hasattr(author, key):
                raise Exception(f"Invalid key: {key}. Valid: author")
            setattr(author, key, value)
        db.session.commit()
        return author.to_dict(), 200
    except Exception as e:
        return str(e), HTTPStatus.BAD_REQUEST
    

@app.route("/authors/<int:author_id>", methods=["DELETE"])
def delete_author(author_id: int):
    author = db.get_or_404(AuthorModel, author_id)
    db.session.delete(author)
    try:
        db.session.commit()
        return f"Author with id {author_id} deleted"
    except Exception as e:
        db.session.rollback()
        abort(503, f"Database error: {str(e)}")    