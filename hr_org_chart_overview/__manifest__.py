

{
    "name": "HR Org Chart Overview",
    "version": "16.0.0.1",
    "category": "Human Resources",
      'author': 'Prixgen Tech Solutions Pvt. Ltd.',
    'company': 'Prixgen Tech Solutions Pvt. Ltd.',
    'website': 'https://www.prixgen.com',
    "installable": True,
    "application": False,
    "summary": "Organizational Chart Overview",
    "depends": ["web","hr"],
    "data": ["views/hr_views.xml"],
    "qweb": ["static/src/xml/hr_org_chart_overview.xml"],
    "assets":{
      'web.assets_backend':[
        'hr_org_chart_overview/static/src/js/hr_org_chart_overview.js',
        'hr_org_chart_overview/static/src/lib/orgchart/html2canvas.min.js',
        'hr_org_chart_overview/static/src/lib/orgchart/jspdf.min.js',
        'hr_org_chart_overview/static/src/lib/orgchart/jquery.orgchart.js',
        'hr_org_chart_overview/static/src/lib/orgchart/jquery.orgchart.css',
        'hr_org_chart_overview/static/src/scss/hr_org_chart_style.scss',
      ],
    },

}
