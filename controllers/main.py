# -*- coding: utf-8 -*-
try:
    from odoo import http
    from odoo.http import request
except ImportError:
    # Fail gracefully if imports fail
    http = None
    request = None

if http:
    class HideDBManagerController(http.Controller):
        @http.route('/web/database/manager', type='http', auth='none', csrf=False)
        def block_db_manager(self, **kw):
            # Always return Odoo's 404 page using the request helper
            return request.not_found()