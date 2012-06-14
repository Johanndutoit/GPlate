
"""
Handles our Schemas for use by the service.

From here we define how what the objects look like.
"""

import datetime
from google.appengine.ext import db
from google.appengine.api import users
import dal

"""
Define our Schemas.
"""

class License(db.Model):
	"""Models an individual License with it's details and how we will store it."""
	owner = db.UserProperty()
	name = db.StringProperty()
	content = db.StringProperty(multiline=True)
	uid = db.StringProperty(multiline=True)
	secret = db.StringProperty(multiline=True)
	created = db.DateTimeProperty(auto_now_add=True)
	lastupdated = db.DateTimeProperty(auto_now_add=True)

# Assign some DAL Methods
License.by_user = dal.licenses_by_user
License.by_uid = dal.license_by_uid

class LicenseAccessToken(db.Model):
	"""The structure of a License Use Case"""
	user = db.UserProperty()
	token = db.StringProperty()
	created = db.DateTimeProperty(auto_now_add=True)
	accessed = db.DateTimeProperty()
	expire = db.DateTimeProperty()
	lastupdated = db.DateTimeProperty(auto_now_add=True)

# Assign some DAL Methods
LicenseAccessToken.by_user = dal.licenses_by_user
LicenseAccessToken.by_license = dal.licenses_by_user
LicenseAccessToken.by_id = dal.licenses_by_user

class LicenseUse(db.Model):
	"""The structure of a License Use Case"""
	user = db.UserProperty()
	comment = db.StringProperty(multiline=True)
	created = db.DateTimeProperty(auto_now_add=True)
	lastupdated = db.DateTimeProperty(auto_now_add=True)

# Assign some DAL Methods
LicenseUse.by_user = dal.licenses_by_user
LicenseUse.by_license = dal.licenses_by_user
LicenseUse.by_id = dal.licenses_by_user

class History(db.Model):
	"""Models a History Item. In Other words a Event Log Item."""
	user = db.UserProperty()
	message = db.StringProperty(multiline=True)
	created = db.DateTimeProperty(auto_now_add=True)
	lastupdated = db.DateTimeProperty(auto_now_add=True)

# Assign some DAL Methods
History.by_user = dal.licenses_by_user
History.by_license = dal.licenses_by_user

