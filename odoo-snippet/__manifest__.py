# -*- coding: utf-8 -*-
{
    "name": "Snippet",
    "summary": """
        tutorial snippets""",
    "description": """
        ok
    """,
    "author": "vyngt",
    "website": "https://github.com/vyngt",
    "category": "Uncategorized",
    "version": "16.0.1.0.0",
    "depends": ["base", "website"],
    "data": [
        'security/ir.model.access.csv',
        "views/snippets/data.xml",
        "views/snippets/snippets.xml",
        "views/snippets/data_company.xml",
        "views/snippets/data_user.xml",
        "views/snippets/carousel.xml",
        "views/back_end/menu.xml",
    ],
    "odoo_snippet.awesome":[
        "odoo-snippet/static/lib/fontawesome/css/all.css"
    ],
    "odoo_snippet.bootstrap":[
        "odoo-snippet/static/lib/bootstrap/css/bootstrap.min.css",
        "odoo-snippet/static/lib/bootstrap/js/bootstrap_assets.js",
    ],
}
