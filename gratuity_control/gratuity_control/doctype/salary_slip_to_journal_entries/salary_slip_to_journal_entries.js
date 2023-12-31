// Copyright (c) 2023, Muhammad Zubair and contributors
// For license information, please see license.txt

frappe.ui.form.on('Salary Slip To Journal Entries', {
	refresh: function(frm) {
		document.querySelectorAll("[data-fieldname='get_employee_salaries']")[1].style.backgroundColor ="#00daff";
		document.querySelectorAll("[data-fieldname='get_employee_salaries']")[1].style.color ="white";
		document.querySelectorAll("[data-fieldname='get_employee_salaries']")[1].style.fontWeight ="bold";

		document.querySelectorAll("[data-fieldname='generate_journal_entries']")[1].style.backgroundColor ="#4ece0f";
		document.querySelectorAll("[data-fieldname='generate_journal_entries']")[1].style.color ="white";
		document.querySelectorAll("[data-fieldname='generate_journal_entries']")[1].style.fontWeight ="bold";

		frm.add_custom_button(__("Journal Entry"), function() {
			window.location.href="/app/journal-entry"
		
		});
	},

	get_employee_salaries: function (frm) {
		if (frm.doc.start_date && frm.doc.end_date && frm.doc.company && frm.doc.status) {
			frappe.call({
				method: "gratuity_control.gratuity_control.doctype.salary_slip_to_journal_entries.salary_slip_to_journal_entries.get_salaries_slip",
				args: {
					start_date: frm.doc.start_date,
					end_date: frm.doc.end_date,
					company: frm.doc.company,
					status: frm.doc.status
				}
			}).then((r) => {
				// console.log("Response", r)
			})
		} else {
			alert("Please select all filters")
		}
	},
	generate_journal_entries: function (frm) {
		frappe.call({
			method: "gratuity_control.gratuity_control.doctype.salary_slip_to_journal_entries.salary_slip_to_journal_entries.generate_journal_entries",
			args: {
				start_date: frm.doc.start_date,
				account: frm.doc.account,
				debit_account: frm.doc.debit_account,
				reference_number: frm.doc.reference_number
			}
		}).then((r) => {
			if(r.message == "none") {
				frappe.show_alert({
					message:__('Hi, Please first Pull Employee Salary Slips'),
					indicator:'red'
				}, 5);
			} else if(r.message == "ok") {
				frappe.show_alert({
					message:__('Hi, Banke Entries Generated Successfully agianst Salries Slips'),
					indicator:'green'
				}, 5);
				setTimeout(() => {
					location.reload()
				}, 5000);
				
				
				
			}
			// console.log("Response", r)
		})
	}
});
