import smtplib

import requests
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
Bootstrap(app)

# notify
my_mail = "mluzuriagam2@gmail.com"
rc_mail = ["mluzuriagam@gmail.com", "jmluzuriagam@gmail.com"]
my_password = os.environ['google_key']


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
    body = StringField("Mensaje", validators=[DataRequired("Debe incluir este campo")])
    submit = SubmitField("Submit Post")


@app.route("/")
def index():
    return render_template("index.html", success=True)


@app.route("/<success>")
def index2(success):
    print(success)
    return render_template("index.html", success=success)


@app.route("/form", methods=["GET", "POST"])
def contact_form():
    form = CreatePostForm()
    if form.validate_on_submit():
        msg = f"Nombre: {form.data['name']} /" \
              f"Email: {form.data['email']} / " \
              f"Celular: {form.data['phone']} / " \
              f"Mensaje: {form.data['body']}"
        try:
            print("Trying")
            for recipient in rc_mail:
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_mail, password=my_password)
                    connection.sendmail(from_addr=my_mail, to_addrs=recipient,
                                        msg=f"Subject:Alerta Contacto Cliente\n\n{msg.encode('utf-8')}")
            print("Success")
            return redirect(url_for("index2", success="True"))
        except:
            try:
                print("Trying to sent alert")
                for recipient in rc_mail:
                    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                        connection.starttls()
                        connection.login(user=my_mail, password=my_password)
                        connection.sendmail(from_addr=my_mail, to_addrs=recipient,
                                            msg=f"Subject:Alerta Error Pagina\n\nError en formulario de envio")
                print("Success sending alert")
                return redirect(url_for("index2", success="False"))
            except:
                print("No Success")
                return redirect(url_for("index2", success="False"))
    return render_template("form.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
