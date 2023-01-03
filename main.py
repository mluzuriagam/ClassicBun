import smtplib
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_ckeditor import CKEditor, CKEditorField
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# notify
my_mail = "mluzuriagam2@gmail.com"
rc_mail = ["mluzuriagam@gmail.com", "jmluzuriagam@gmail.com"]
my_password = os.environ['google_key']
print(my_password)


def notify(msg):
    for recipient in rc_mail:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_mail, password=my_password)
            connection.sendmail(from_addr=my_mail, to_addrs=recipient,
                                msg=f"Subject:<b>Alerta Contacto Cliente</b>\n\n{msg}")


##WTForm
class CreatePostForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired("Debe incluir este campo")])
    email = StringField("Correo",
                        validators=[DataRequired("Debe incluir este campo"), Email("Correo de formato invalido")])
    phone = StringField("Teléfono(Opcional)")
    body = CKEditorField("Mensaje", validators=[DataRequired("Debe incluir este campo")])
    submit = SubmitField("Submit Post")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form", methods=["GET", "POST"])
def contact_form():
    form = CreatePostForm()
    if form.validate_on_submit():
        msg = f"Nombre:{form.data['name']}\nEmail:{form.data['email']}\nTeléfono:{form.data['phone']}\nMensaje:{form.data['body']}\n"
        print(msg)
        try:
            notify(msg)
            return redirect(url_for("index"))
        except:
            pass
            return redirect(url_for("index"))
    return render_template("form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
