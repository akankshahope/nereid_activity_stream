# -*- coding: utf-8 -*-
"""
    activity stream

    Customer Portal Home

    :copyright: (c) 2012-2013 by Openlabs Technologies & Consulting (P) Limited
    :license: GPLv3, see LICENSE for more details.
"""
from decimal import Decimal
import pytz
import hashlib
import base64
import urllib
from datetime import timedelta

from wtforms import (Form, TextField, SelectField, TextAreaField,
    BooleanField, validators)
from nereid import login_required, render_template

from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import Pool


class NereidUser(ModelSQL, ModelView):
    _name = "nereid.user"
    activity_stream = fields.One2Many('activity.stream1', 'actor',
        'Activity Stream'
    )


class ActivityStream(ModelSQL, ModelView):
    "Activity Stream"
    _name = 'activity.stream1'

    """
     Model created for Activity Stream.
    """
    actor = fields.Many2One('nereid.user', 'Nereid Users',
        required= True, select=True
    )
    verb = fields.Char("Verb")
    object = fields.Reference("Object", selection='models_get',
        select=True
    )
    target = fields.Many2One('nereid.user',
        'Target', required= True
    )
    create_date = fields.DateTime('Published On', readonly=True, select=True)

    def models_get(self):
        pool = Pool()
        model_obj = pool.get('ir.model')
        model_ids = model_obj.search([])
        res = []
        for model in model_obj.browse(model_ids):
            res.append([model.model, model.name])
        return res

ActivityStream()
