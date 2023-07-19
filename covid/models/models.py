# -*- coding: utf-8 -*-

from odoo import models, fields, api

class covid_19(models.Model):
    _name = 'covid.covid_19'

    source = fields.Char(string ='Source', required = True)
    date = fields.Datetime(string = 'Date Time', required = True, default = fields.Datetime.now())
    country_id = fields.Many2one('res.country', required = True)
    infected = fields.Integer(string = 'Infected in Day', required = True, default = 0)
    recovered = fields.Integer(string = 'Recovered in Day', required = True, default = 0)
    deseaced = fields.Integer(string ='Deseaced in Day', required = True, default = 0)
    total_infected = fields.Integer(string = 'Total Infected per Country', compute = 'set_total_infected')
    total_recovered = fields.Integer(string = 'Total Recovered per Country', compute = 'set_total_recovered')
    total_deseaced = fields.Integer(string = 'Total Deseaced per Country', compute = 'set_total_deseaced')
    total_deseaced_global = fields.Integer(string = 'Total Deseaced in the World', compute = 'set_total_deseaced_global')
    total_recovered_global = fields.Integer(string = 'Total Recovered in the World', compute = 'set_total_recovered_global')
    total_infected_global = fields.Integer(string = 'Total Infected in the World', compute = 'set_total_infected_global')

    # Contador Pais
    def set_total_infected(self):
        for data in self:
            domain = [
                        ('country_id','=',data.country_id.id),
                        ('date','<',data.date)
                    ]
            records = self.search (domain)
            Infecteds = records.mapped('infected')
            data.total_infected = sum(Infecteds)+data.infected

    def set_total_recovered(self):
        for data in self:
            domain = [
                        ('country_id','=',data.country_id.id),
                        ('date','<',data.date)
                    ]
            records = self.search (domain)
            Recovereds = records.mapped('recovered')
            data.total_recovered = sum(Recovereds)+data.recovered

    def set_total_deseaced(self):
        for data in self:
            domain = [
                        ('country_id','=',data.country_id.id),
                        ('date','<',data.date)
                    ]
            records = self.search (domain)
            Deseaceds = records.mapped('deseaced')
            data.total_deseaced = sum(Deseaceds)+data.deseaced

    # Contador Global

    def set_total_infected_global(self):
        for data in self:
            domain = [
                        ('date','<',data.date)
                    ]
            records = self.search (domain)
            Infected_world = records.mapped('infected')
            data.total_infected_global = sum(Infected_world)+data.infected

    def set_total_recovered_global(self):
        for data in self:
            domain = [
                        ('date','<',data.date)
                    ]
            records = self.search (domain)
            Recovereds_world = records.mapped('recovered')
            data.total_recovered_global = sum(Recovereds_world)+data.recovered

    def set_total_deseaced_global(self):
        for data in self:
            domain = [
                        ('date','<',data.date)
                    ]
            records = self.search (domain)
            Deseaceds_world = records.mapped('deseaced')
            data.total_deseaced_global = sum(Deseaceds_world)+data.deseaced

    #     @api.depends('value')
    #     def _value_pc(self):
    #         self.value2 = float(self.value) / 100