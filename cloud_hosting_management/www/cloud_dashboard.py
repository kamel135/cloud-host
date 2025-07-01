# cloud_dashboard.py

import frappe
from frappe import _

def get_context(context):
    user = frappe.session.user
    customer = frappe.get_value("Cloud Customer", {"user": user}, "name")

    servers = frappe.get_all("Cloud Server", filters={"customer": customer}, fields=["name", "server_name", "status", "ip_address"])
    subscriptions = frappe.get_all("Cloud Subscription", filters={"customer": customer}, fields=["plan", "start_date", "end_date", "status"])
    invoices = frappe.get_all("Hosting Invoice", filters={"customer": customer}, fields=["name", "status", "amount", "due_date"])
    tickets = frappe.get_all("Support Ticket", filters={"customer": customer}, fields=["subject", "status", "creation"])

    context.customer_name = customer
    context.servers = servers
    context.subscriptions = subscriptions
    context.invoices = invoices
    context.tickets = tickets
    return context
