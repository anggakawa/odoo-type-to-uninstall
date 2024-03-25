{
    "name": "Type to Uninstall",
    'version': '1.0',
    "license": "LGPL-3",
    "summary": "Add type to uninstall features to Odoo",
    "description": """
        This module introduces a safety mechanism to the Odoo uninstall process, preventing accidental or unintended module removals. 
        Users must confirm their intention to uninstall by explicitly typing the module's technical name.
    """,
    "author": "anggakawa",
    "website": "https://github.com/anggakawa/odoo-type-to-uninstall",
    "depends": ["base"],
    "data": [
        'wizard/uninstall_form.xml',
    ],
    "installable": True,
}
