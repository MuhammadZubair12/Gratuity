// Copyright (c) 2023, Muhammad Zubair and contributors
// For license information, please see license.txt

frappe.ui.form.on('Salary Slip To Journal Entries', {
	// refresh: function(frm) {

	// }
	get_employee_salaries: function (frm) {
		if (frm.doc.select_date && frm.doc.company && frm.doc.status) {
			frappe.call({
				method: "gratuity_control.gratuity_control.doctype.salary_slip_to_journal_entries.salary_slip_to_journal_entries.get_salaries_slip",
				args: {
					posting_date: frm.doc.select_date,
					company: frm.doc.company,
					status: frm.doc.status
				}
			}).then((r) => {
				console.log("Response", r)
			})
		} else {
			alert("Please select all filters")
		}
	},
	generate_journal_entries: function (frm) {
		frappe.call({
			method: "gratuity_control.gratuity_control.doctype.salary_slip_to_journal_entries.salary_slip_to_journal_entries.generate_journal_entries",
			args: {
				posting_date: frm.doc.select_date
			}
		}).then((r) => {
			console.log("Response", r)
		})
	}
});
