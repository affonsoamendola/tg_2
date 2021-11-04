from flask import flash, redirect, render_template, url_for, current_app
from werkzeug.utils import secure_filename

from .forms import UploadForm

from . import home
from ..models import SpectraEntry

from .. import db

from os.path import join, dirname, realpath

@home.route('/')
def homepage():
	return render_template("home/index.html", title="BeaconDB")

@home.route('/dashboard')
def dashboard():
	recent_additions = SpectraEntry.query.all()

	return render_template("home/dashboard.html", recent_additions=recent_additions, title="BeaconDB - Dashboard")

@home.route('/upload', methods=['GET', 'POST'])
def upload():
	form = UploadForm()

	if(form.validate_on_submit()):
		filename = secure_filename(form.file.data.filename)

		form.file.data.save(join(dirname(realpath(__file__)), "file_storage", filename))

		#db.session.add(entry)
		#db.session.commit()

		flash("Upload Successful!")

	return render_template("home/upload.html", form=form, title="BeaconDB - Upload Spectra")