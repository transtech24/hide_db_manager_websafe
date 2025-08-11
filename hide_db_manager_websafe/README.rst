
Hide Manage Databases Link
==========================

Hide Manage Databases Link hides the "Manage Databases" link from the Odoo 16 login screen while allowing scheduled modules (for example OCA's auto_backup) to operate normally even when `list_db = True` and also block access to web/database/manager.

Key points
----------
- Compatible with Odoo 16 Community and Enterprise.
- License: OPL-1
- Price: $13 USD

Installation
------------
1. Copy the unzipped folder `hide_db_manager_websafe` into your Odoo addons path.
2. Restart Odoo server.
3. In Odoo: Apps -> remove 'Apps' filter -> Update App List.
4. Install "Hide Manage Databases Link".

Usage
-----
- The module is passive: once installed it hides the link on the login page and throws up 404 error if user tries to access web/database/manager.
- To restore the link, uninstall the module or remove it from your addons path and restart the server.

Support
-------
Contact: dennisalabi@gmail.com
