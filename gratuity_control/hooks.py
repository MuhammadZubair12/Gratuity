from . import __version__ as app_version

app_name = "gratuity_control"
app_title = "Gratuity Control"
app_publisher = "Muhammad Zubair"
app_description = "Want to calculate exact experience"
app_email = "zubairmazhar23@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gratuity_control/css/gratuity_control.css"
# app_include_js = "/assets/gratuity_control/js/gratuity_control.js"

# include js, css files in header of web template
# web_include_css = "/assets/gratuity_control/css/gratuity_control.css"
# web_include_js = "/assets/gratuity_control/js/gratuity_control.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gratuity_control/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "gratuity_control.utils.jinja_methods",
#	"filters": "gratuity_control.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "gratuity_control.install.before_install"
# after_install = "gratuity_control.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gratuity_control.uninstall.before_uninstall"
# after_uninstall = "gratuity_control.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gratuity_control.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"gratuity_control.tasks.all"
#	],
#	"daily": [
#		"gratuity_control.tasks.daily"
#	],
#	"hourly": [
#		"gratuity_control.tasks.hourly"
#	],
#	"weekly": [
#		"gratuity_control.tasks.weekly"
#	],
#	"monthly": [
#		"gratuity_control.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "gratuity_control.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "gratuity_control.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "gratuity_control.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"gratuity_control.auth.validate"
# ]
