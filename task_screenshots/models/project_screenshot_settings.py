from odoo import fields, models, api


class ProjectScreenshotSettingsHost(models.Model):
    _name = 'project.screenshot.settings.domain'
    _description = 'ProjectScreenshotSettingsHost'

    name = fields.Char(
        string='Domain')

    _sql_constraints = [
        ('domain_uniq', 'unique(name)', 'Domain must be unique!'),
    ]


class ProjectScreenshotSettings(models.Model):
    _name = 'project.screenshot.settings'
    _description = 'ProjectScreenshotSettings'

    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project')
    source_domain_id = fields.Many2one(
        comodel_name='project.screenshot.settings.domain',
        string='Source domain',
        required=True)
    replacement_domain_id = fields.Many2one(
        comodel_name='project.screenshot.settings.domain',
        string='Replacement domain',
        required=True)

    _sql_constraints = [
        ('project_source_uniq', 'unique(project_id, source_domain_id)', 'Project and Source domain must be unique!'),
    ]



