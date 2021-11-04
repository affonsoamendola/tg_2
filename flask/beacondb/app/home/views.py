from flask import flash, redirect, render_template, url_for, current_app, request, send_file, safe_join
from werkzeug.utils import secure_filename

from .forms import UploadForm

from . import home
from ..models import SpectraEntry

from .. import db

from astropy.io import fits

from os.path import join, dirname, realpath

from sys import stderr

@home.route('/')
def homepage():
	return render_template("home/index.html", title="BeaconDB")

@home.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
	if(request.method == 'POST'):
		try:
			return send_file(safe_join(dirname(realpath(__file__)), "file_storage", request.form["download_button"]))
		except	FileNotFoundError:
			abort(404)

	recent_additions = SpectraEntry.query.all()

	return render_template("home/dashboard.html", recent_additions=recent_additions, title="BeaconDB - Dashboard")

@home.route('/upload', methods=['GET', 'POST'])
def upload():
	form = UploadForm()

	if(form.validate_on_submit()):
		filename = secure_filename(form.file.data.filename)

		absolute_path = safe_join(dirname(realpath(__file__)), "file_storage", filename)

		form.file.data.save(absolute_path)
		
		entry = SpectraEntry()
		
		hdulist = fits.open(absolute_path)

		entry.file = filename
 
		entry.target_name = hdulist[0].header['OBJNAME']
		entry.observator = hdulist[0].header['OBSERVER']

		entry.ra = hdulist[0].header['RA']
		entry.dec = hdulist[0].header['DEC']

		entry.mjd = hdulist[0].header['JD-OBS']

		entry.site = hdulist[0].header['BSS_SITE']

		hdulist.close()

		db.session.add(entry)
		db.session.commit()

		flash("Upload Successful!")

	return render_template("home/upload.html", form=form, title="BeaconDB - Upload Spectra")