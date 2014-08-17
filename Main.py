##!/usr/bin/env python

import gtk
import LoginUser
import DbConnect

class About:

	def on_btnClose_button_press_event(self, button, data=None):
		self.dlg.hide()

	def __init__(self):
		self.gladefile = "About.glade"

	def run(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file(self.gladefile)
		self.builder.connect_signals(self)
		self.dlg = self.builder.get_object("AboutDialog")
		self.result = self.dlg.run()

class LoginUser:

	# Dialog LoginUser
	def on_LoginDialog_destroy(self, object, data=None):
		self.logged_in = False
		self.dlg.hide()

	def on_btnLogin_clicked(self, button, data=None):

		conn = DbConnect.user()
		username = self.entryUser.get_text()
		password = self.entryPass.get_text()
		role = conn.dbLogin(username,password)

		if role:
			self.logged_in = True
			self.dlg.hide()
		else:
			print "Username or password is incorrect!"

	def on_btnCancel_clicked(self, button, data=None):
		self.logged_in = False
		self.dlg.hide()

	def __init__(self):
		self.gladefile = "LoginUser.glade"

	def run(self):
		self.logged_in = False
		self.builder = gtk.Builder()
		self.builder.add_from_file(self.gladefile)
		self.builder.connect_signals(self)
		self.dlg = self.builder.get_object("LoginDialog")
		self.entryUser = self.builder.get_object('txtUsername')
		self.entryPass = self.builder.get_object('txtPassword')
		self.result = self.dlg.run()

		return self.result,self.logged_in

class MainFrame:

	# Dialog About
	def on_open_about_activate(self, menuitem, data=None):
		dialog = About()
		result = dialog.run()

	# Main Frame
	def on_window1_destroy(self, object, data=None):
		gtk.main_quit()

	def on_gtk_quit_activate(self, menuitem, data=None):
		gtk.main_quit()

	def __init__(self):
		self.gladefile = "Main.glade"
		self.builder = gtk.Builder()
		self.builder.add_from_file(self.gladefile)
		self.builder.connect_signals(self)
		self.window = self.builder.get_object("Main")
		self.dlg = self.builder.get_object("LoginDialog")

		login = LoginUser()
		result,authenticated = login.run()

		if authenticated and result == 0:
			self.window.show()
		else:
										gtk.main_quit()

if __name__ == "__main__":
	main = MainFrame()
	gtk.main()
