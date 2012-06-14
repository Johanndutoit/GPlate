
from google.appengine.ext import db

def licenses_by_user(user_id):
	licenses = db.GqlQuery("SELECT * FROM License WHERE owner IS :1 ORDER BY name", user_id)
	return licenses