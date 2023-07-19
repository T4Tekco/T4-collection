# -*- coding: utf-8 -*-
{
    "name": "T4Tek Theme",
    "summary": """
        T4Tek Theme""",
    "author": "T4Tek Team",
    "website": "https://t4tek.tk",
    "category": "T4Collection/Theme",
    "version": "16.0.0.0.1",
    "depends": ["base", "web", "mail"],
    "data": [
        "views/webclient_templates.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "t4_theme/static/src/scss/t4_theme_variable.scss",
            "t4_theme/static/src/scss/navbar.scss",
            "t4_theme/static/src/js/**/*",
        ],
    },
}  # type: ignore
