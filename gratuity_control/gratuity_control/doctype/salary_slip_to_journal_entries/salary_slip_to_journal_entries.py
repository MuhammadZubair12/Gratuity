# Copyright (c) 2023, Muhammad Zubair and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SalarySlipToJournalEntries(Document):
	pass
@frappe.whitelist()
def get_salaries_slip(**args):
	start_date = args.get('start_date')
	end_date = args.get('end_date')
	status = args.get('status')
	company = args.get('company')
	sal = frappe.db.sql("""select employee,employee_name,posting_date,status,company,total_deduction,gross_pay,start_date,end_date,salary_structure,bank_name,bank_account_no,rounded_total,\
	department,payroll_entry,payroll_frequency,mode_of_payment,total_working_days,payment_days,currency,name from `tabSalary Slip` where status=%s and posting_date >= %s and posting_date <= %s""",(status,start_date,end_date))
	doc = frappe.get_doc("Salary Slip To Journal Entries")
	doc.salary_slip_details = []
	for sa in sal:
		check = frappe.db.exists('Salary Slip Details', dict(salary_slip_id = sa[20]))
		if check:
			pass
		else:
			row = doc.append("salary_slip_details",{})
			row.employee = sa[0]
			row.employee_name = sa[1]
			row.posting_date = sa[2]
			row.status = sa[3]
			row.company = sa[4]
			row.total_deduction = sa[5]
			row.gross_pay = sa[6]
			row.start_date = sa[7]
			row.end_date = sa[8]
			row.salary_structure = sa[9]
			row.bank_name = sa[10]
			row.bank_account_no = sa[11]
			row.rounded_total = sa[12]
			row.department = sa[13]
			row.payroll_entry = sa[14]
			row.payroll_frequency = sa[15]
			row.mode_of_payment = sa[16]
			row.total_working_days = sa[17]
			row.payment_days = sa[18]
			row.currency = sa[19]
			row.salary_slip_id = sa[20]
	doc.save()
@frappe.whitelist()
def generate_journal_entries(**args):
	a = 5
	account = args.get('account')
	debit_account = args.get('debit_account')
	reference_number = args.get('reference_number')
	doc = frappe.db.sql(""" select employee,salary_slip_id,posting_date,rounded_total,bank_name,bank_account_no from `tabSalary Slip Details` """)
	je = frappe.new_doc("Journal Entry")
	if doc:
		je.voucher_type = "Bank Entry"
		je.posting_date = doc[0][2]
		je.cheque_no = reference_number
		je.cheque_date = doc[0][2]
		for t in doc:
			je.append(
				"accounts",
				{
					"account": account,
					"party_type": "Employee",
					"party": t[0],
					"credit_in_account_currency": t[3]
				},
			)
			je.append(
				"accounts",
				{
					"account":debit_account,
					"party_type": "Employee",
					"party": t[0],
					"debit_in_account_currency": t[3]
				},
			)
		frappe.db.delete("Salary Slip Details")
		je.save()
		return "ok"
	else:
		return "none"