
from google.appengine.ext import db

def licenses_by_access(user_id,own=False):
	"""
	Returns a Collection of Licenses that the user has access to.

	Be it their own or not.

	The flag, specifies whether the query should include the licenses of the users
	themselves. 
	"""
	licenses = db.GqlQuery("SELECT * FROM License WHERE owner IS :1 ORDER BY name", user_id)
	return licenses

def licenses_by_user(user_id):
	"""
	Returns a Collection of Licenses belonging to the user. 

	So Licenses where the user is the owner
	"""
	licenses = db.GqlQuery("SELECT * FROM License WHERE owner IS :1 ORDER BY name", user_id)
	return licenses

def license_by_uid(uid):
	"""
	Returns a License by it's UID
	"""
	licenses = db.GqlQuery("SELECT * FROM License WHERE uid IS :1 ORDER BY name", uid)
	return licenses