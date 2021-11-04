from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired

from ..models import SpectraEntry

class UploadForm(FlaskForm):
	file = 	 FileField("File", validators=[FileRequired()])

