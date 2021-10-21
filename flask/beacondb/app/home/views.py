from flask import flash, redirect, render_template

from .forms import UploadForm

from . import home
from ..models import SpectraEntry

@home.route('/')
def homepage():
	return render_template("home/index.html", title="BeaconDB")

@home.route('/dashboard')
def dashboard():
	return render_template("home/dashboard.html", title="BeaconDB - Dashboard")

@home.route('/upload', methods=['GET', 'POST'])
def upload():
	form = UploadForm()

	if(form.validate_on_submit()):
		entry = SpectraEntry(	file=form.file.data,
								mjd=form.mjd.data,
								target_name=form.target_name.data,
								observator=form.observator.data,
								observatory=form.observatory.data )

		db.session.add(entry)
		db.session.commit()

		flash("Upload Successful!")

		return redirect(url_for('home.dashboard'))

	return render_template("home/upload.html", form=form, title="BeaconDB - Upload Spectra")