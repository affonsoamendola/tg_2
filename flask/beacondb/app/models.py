from app import db

class SpectraEntry(db.Model):
	__tablename__ = "spectra_entries"

	id = 			db.Column(db.Integer,    	primary_key=True)
	file =  		db.Column(db.String(60),	index=False,	unique=True)
	mjd = 			db.Column(db.Float,      	index=True, 	unique=False)
	target_name = 	db.Column(db.String(60), 	index=True, 	unique=False)
	observator  = 	db.Column(db.String(60), 	index=True, 	unique=False)
	observatory = 	db.Column(db.String(60), 	index=True, 	unique=False)
