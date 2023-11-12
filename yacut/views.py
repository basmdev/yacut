from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import YacutForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route("/", methods=["GET", "POST"])
def index_view():
    form = YacutForm()
    if form.validate_on_submit():
        original_url = form.original_link.data
        site = url_for("index_view", _external=True)
        short_id = form.custom_id.data or get_unique_short_id()
        existing_short_id = URLMap.query.filter_by(short=short_id).first()
        if existing_short_id:
            flash("Предложенный вариант короткой ссылки уже существует.")
        else:
            url_map = URLMap(original=original_url, short=short_id)
            db.session.add(url_map)
            db.session.commit()
            flash(
                f"""Ваша новая ссылка готова: <a href="{site + short_id}">{site + short_id}</a>"""
            )
        return render_template(
            "index.html",
            original_url=original_url,
            short_url=short_id,
            form=form,
        )

    return render_template("index.html", form=form)


@app.route("/<short_url>")
def redirect_to_long(short_url):
    url_map = URLMap.query.filter_by(short=short_url).first_or_404()

    return redirect(url_map.original)
