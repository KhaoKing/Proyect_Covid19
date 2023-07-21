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

    def print_report(self):
        cont19 = self.env['covid.covid_19']
        domain = [
                    ('date','>=',self.start_date),
                    ('date','<=',self.end_date)
                    ]
        if self.country_ids:
            domain.append(('country_id','in',self.country_ids.ids))
        contField=[
                'source',
                'date',
                'country_id',
                'infected',
                'recovered',
                'deseaced',
        ]

        contRecords=cont19.search_read(domain, contField)
        data_containt={
                'contRecords' : contRecords,
                'start_date' : self.start_date,
                'end_date' : self.end_date,
                'country_ids' : self.country_ids,
                    }
        
        return self.env.ref('covid.dates_report_external').report_action(self, data=data_containt)
