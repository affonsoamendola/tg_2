from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import SpectraEntry

class UploadForm(FlaskForm):
	file = 			StringField("File Name", validators=[DataRequired()])
	mjd = 			FloatField("MJD", validators=[DataRequired()])
	target_name = 	StringField("Target Name", validators=[DataRequired()])
	observator  = 	StringField("Observator Name", validators=[DataRequired()])
	observatory = 	StringField("Observatory Name", validators=[DataRequired()])

	submit = SubmitField("Upload")
