from odoo import api, fields, models
from odoo.exceptions import UserError

class DateReportWizard(models.TransientModel):
    _name = 'covid19.date.report.wizard'
    _description = 'Report of Covid on Date Specific'

start_date= fields.Date('Start Date', required =True)
end_date= fields.Date('End Date', required = True)
country_ids = fields.Many2many(
                                "res.country",
                                string = "Countries",
                                help = "Countries you want generate the report"
                                )

def print_report (self):
    print ('Vamos Bien')
    print ('Vamos Bien')
    print ('Vamos Bien')
    print ('Vamos Bien')
    return True