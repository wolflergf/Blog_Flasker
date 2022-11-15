from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "huansijpmpkijinhqwd"


# Create a form Class
class NameForm(FlaskForm):
    name = StringField("What's your name:", validators=[DataRequired()])
    submit = SubmitField("Sumit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


# Create Name Page
@app.route("/name", methods=["POST", "GET"])
def name():
    name = None
    form = NameForm()
    # Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successful")
    return render_template("name.html",
                           name=name,
                           form=form)


if __name__ == "__main__":
    app.run(debug=True)
