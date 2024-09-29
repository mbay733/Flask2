from api import app
from flask import jsonify
from werkzeug.exceptions import HTTPException


@app.errorhandler(HTTPException)
def handle_exeption(e):
    """Функция для перехвата HTTP ошибок и возврата в виде JSON."""
    return jsonify({"message": str(e)}), e.code