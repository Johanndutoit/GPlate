#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import schemas as schema # Just nicer to remember
import webapp2
import os
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users

# Configure the Directory where we store our "views" / Templates
#
view_dir = os.path.join(os.path.dirname(__file__), 'views')

class DashboardHandler(webapp2.RequestHandler):
	"""
	Acts as the Frontpage when users are not signed in and the dashboard when they are.
	"""
	def get(self):
		user = users.get_current_user()

		if user:
			locales = {}
			self.response.out.write(template.render(os.path.join(view_dir, 'user', 'dashboard.html'), locales))
		else:
			locales = {}
			self.response.out.write(template.render(os.path.join(view_dir, 'homepage.html'), locales))

class ConnectHandler(webapp2.RequestHandler):
	"""
	Handles the Authentication of the Users to the service
	We use the App Engine User Service for this.

	So it's just a redirect actually
	"""
	def get(self):

		self.redirect(users.create_login_url('/'))

class LogoutHandler(webapp2.RequestHandler):
	"""
	Logs users out and redirects them back to the frontpage.

	So it's just a redirect actually
	"""
	def get(self):

		self.redirect(users.create_logout_url("/"))

class RegisterLicenseHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Register a New License')

class ManageLicenseHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Manage a License')

class ViewLicenseHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('View a License that you have permission for.')

class RegisterAccessLicenseHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Give a User Access for a set amount of time and occurences.')

class ManageAccessLicenseHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Manage a Users Access')

class RemoveAccessLicenseHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('Removes a Users Access')

app = webapp2.WSGIApplication([('/', DashboardHandler),
								('/signin', ConnectHandler),
								('/logout', LogoutHandler)],
                              debug=True)
