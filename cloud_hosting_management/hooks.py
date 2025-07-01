app_name = "cloud_hosting_management"
app_title = "Cloud Hosting Management"
app_publisher = "kamel"
app_description = "Cloud Hosting Service Manager"
app_email = "kamelelnemr1@gmail.com"
app_license = "mit"


app_icon = "octicon octicon-cloud"  # أو أي أيقونة تناسبك من octicons
app_color = "blue"  # لون أيقونة الموديول في الشريط الجانبي (اختياري)

# Apps
# ------------------
fixtures = [
    {
        "dt": "Workspace",
        "filters": [["title", "=", "Cloud Hosting Dashboard"]]
    }
]

# cloud_hosting/hooks.py
#####################
fixtures = [
    {
        "doctype": "Web Page",
        "filters": [
            ["route", "in", ["/cloud-dashboard"]]
        ]
    },
    {
        "doctype": "Portal Menu Item",
        "filters": [
            ["route", "=", "/cloud-dashboard"]
        ]
    }
]



####################
fixtures = [
    {"dt": "DocType", "filters": [["name", "in", [
        "Cloud Plan",
        "Cloud Datacenter",
        "Cloud Payment"
    ]]]}
]



fixtures = [
    {
        "dt": "Custom DocPerm",
        "filters": [
            ["parent", "in", [
                "Cloud Server",
                "Cloud Plan",
                "Cloud Datacenter",
                "Cloud Payment"
            ]]
        ]
    },
    {
        "dt": "Role",
        "filters": [
            ["role_name", "in", ["Cloud Admin", "Customer"]]
        ]
    }
]
################
portal_menu_items = [
    {
        "title": "Cloud Dashboard",
        "route": "/cloud-dashboard",
        "reference_doctype": "Cloud Customer",
        "role": "Customer"
    }
]
#########################

fixtures = [
     {
        "doctype": "Portal Menu Item",
        "filters": [
            ["route", "=", "/cloud-dashboard"]
        ]
      },
    {
        "doctype": "Web Page",
        "filters": [
            ["route", "=", "/cloud-dashboard"]
        ]
    }
]


###########################

fixtures = [
    {"dt": "DocType", "filters": [["name", "in", [
        "Cloud Payment",
        "Cloud Datacenter",
        "Cloud Plan",
        "Cloud Customer",
        "Cloud Subscription",
        "Performance Monitoring",
        "Hosting Invoice",
        "Cloud Server",
        "Support Ticket",
        "Hosting Plan"
    ]]]},
]

###################










########################
# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "cloud_hosting_management",
# 		"logo": "/assets/cloud_hosting_management/logo.png",
# 		"title": "Cloud Hosting Management",
# 		"route": "/cloud_hosting_management",
# 		"has_permission": "cloud_hosting_management.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cloud_hosting_management/css/cloud_hosting_management.css"
# app_include_js = "/assets/cloud_hosting_management/js/cloud_hosting_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/cloud_hosting_management/css/cloud_hosting_management.css"
# web_include_js = "/assets/cloud_hosting_management/js/cloud_hosting_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "cloud_hosting_management/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "cloud_hosting_management/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "cloud_hosting_management.utils.jinja_methods",
# 	"filters": "cloud_hosting_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "cloud_hosting_management.install.before_install"
# after_install = "cloud_hosting_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "cloud_hosting_management.uninstall.before_uninstall"
# after_uninstall = "cloud_hosting_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "cloud_hosting_management.utils.before_app_install"
# after_app_install = "cloud_hosting_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "cloud_hosting_management.utils.before_app_uninstall"
# after_app_uninstall = "cloud_hosting_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cloud_hosting_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cloud_hosting_management.tasks.all"
# 	],
# 	"daily": [
# 		"cloud_hosting_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"cloud_hosting_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cloud_hosting_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"cloud_hosting_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "cloud_hosting_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cloud_hosting_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "cloud_hosting_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["cloud_hosting_management.utils.before_request"]
# after_request = ["cloud_hosting_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["cloud_hosting_management.utils.before_job"]
# after_job = ["cloud_hosting_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"cloud_hosting_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

def create_cloud_hosting_dashboard():
    import frappe

    workspace_name = "Cloud Hosting Dashboard"

    if not frappe.db.exists("Workspace", workspace_name):
        workspace = frappe.get_doc({
            "doctype": "Workspace",
            "module": "Cloud Hosting Management",
            "title": workspace_name,
            "label": workspace_name,
            "icon": "octicon octicon-server",
            "pinned": 1,
            "sections": [
                {
                    "title": "Main",
                    "items": [
                        {"type": "doctype", "name": "Cloud Subscription"},
                        {"type": "doctype", "name": "Hosting Invoice"},
                        {"type": "doctype", "name": "Support Ticket"},
                        {"type": "doctype", "name": "Performance Monitoring"},
                    ]
                }
            ]
        })
        workspace.insert()
        frappe.db.commit()
        print(f"Workspace '{workspace_name}' created.")
    else:
        print(f"Workspace '{workspace_name}' already exists.")
after_install = "cloud_hosting_management.hooks.create_cloud_hosting_dashboard"
