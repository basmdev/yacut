from flask import jsonify, request, url_for

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id, is_valid_custom_id


@app.route("/api/id/", methods=["POST"])
def add_short_url():
    data = request.get_json()
    site = url_for("index_view", _external=True)
    if not data:
        raise InvalidAPIUsage("Отсутствует тело запроса")

    if "url" not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!', 400)

    custom_id = data.get("custom_id") or get_unique_short_id()

    if URLMap.query.filter_by(short=custom_id).first() is not None:
        raise InvalidAPIUsage(
            "Предложенный вариант короткой ссылки уже существует."
        )

    if not is_valid_custom_id(custom_id):
        raise InvalidAPIUsage(
            "Указано недопустимое имя для короткой ссылки", 400
        )

    if len(custom_id) > 16:
        raise InvalidAPIUsage(
            "Длина короткой ссылки не должна превышать 16 символов", 400
        )

    short_url = URLMap(short=custom_id)
    short_url.from_dict({"original": data["url"]})

    db.session.add(short_url)
    db.session.commit()

    return (
        jsonify(
            {"url": short_url.original, "short_link": site + short_url.short}
        ),
        201,
    )


@app.route("/api/id/<short_id>/", methods=["GET"])
def get_short_url(short_id):
    short_url = URLMap.query.filter_by(short=short_id).first()
    if short_url is None:
        raise InvalidAPIUsage("Указанный id не найден", 404)
    return jsonify({"url": short_url.original}), 200
