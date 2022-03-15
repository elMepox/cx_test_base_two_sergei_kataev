{
    "name": "Sales Order Lines Numeration",
    "summary": "Sales Order Lines Numeration",
    "version": "11.0.1.0.0",
    "category": "Sale",
    "author": "Sergei Kataev, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
         "sale_management",
    ],
    "data": [
        "views/sale_order_line.xml",
        "report/sale_order_report.xml",
    ],
}