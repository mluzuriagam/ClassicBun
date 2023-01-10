from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from mail import EmailSender
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
Bootstrap(app)

# notify
my_mail = "mluzuriagam2@gmail.com"
rc_mail = ["mluzuriagam@gmail.com", "jmluzuriagam@gmail.com"]
my_password = os.environ['google_key']
mail_sender = EmailSender(fromaddr=my_mail, password=my_password)


##WTForm
class CreatePostForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired("Debe incluir este campo")])
    email = StringField("Correo",
                        validators=[DataRequired("Debe incluir este campo"), Email("Correo de formato invalido")])
    phone = StringField("Teléfono(Opcional)")
    body = StringField("Mensaje", validators=[DataRequired("Debe incluir este campo")])
    submit = SubmitField("Submit Post")


class CreatePostForm2(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired("Debe incluir este campo")])
    email = StringField("Correo",
                        validators=[DataRequired("Debe incluir este campo"), Email("Correo de formato invalido")])
    phone = StringField("Teléfono(Opcional)")
    body = StringField("Mensaje", validators=[DataRequired("Debe incluir este campo")])
    CV = FileField("Suba aquí su CV")
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
    msg = f"Nombre: {form.data['name']} /" \
          f"Email: {form.data['email']} / " \
          f"Celular: {form.data['phone']} / " \
          f"Mensaje: {form.data['body']}"
    if form.validate_on_submit():
        try:
            print("Trying")
            for address in rc_mail:
                mail_sender.send_mail(toaddr=address, subject="Alerta de Venta", body=msg)
            return redirect(url_for("index2", success="True"))
        except:
            print("No Success")
            return redirect(url_for("index2", success="False"))
    return render_template("form.html", form=form)


@app.route("/form2", methods=["GET", "POST"])
def work_with_us():
    form = CreatePostForm2()
    msg = f"Nombre: {form.data['name']} /" \
          f"Email: {form.data['email']} / " \
          f"Celular: {form.data['phone']} / " \
          f"Mensaje: {form.data['body']}"
    if form.validate_on_submit():
        try:
            print("Trying")
            for address in rc_mail:
                mail_sender.send_mail(toaddr=address, subject="Solicitud de Trabajo", body=msg, attachment=form.data['CV'],
                                      filename=form.data['CV'].filename)
            return redirect(url_for("index2", success="True"))
        except:
            print("No Success")
            return redirect(url_for("index2", success="False"))
    return render_template("form2.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
