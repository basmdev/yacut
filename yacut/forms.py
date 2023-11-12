from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp


class YacutForm(FlaskForm):
    original_link = StringField(
        "Длинная ссылка",
        validators=[
            DataRequired(message="Обязательное поле"),
            URL(message="Введите корректный URL"),
        ],
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=[
            Regexp("^[a-zA-Z0-9]*$", message="Только латинские буквы и цифры"),
            Length(
                1, 16, message="Длина ссылки не может быть больше 16 символов"
            ),
            Optional(),
        ],
    )
    submit = SubmitField("Создать")
