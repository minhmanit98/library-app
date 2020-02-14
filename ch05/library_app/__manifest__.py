{'name': 'Library Management Application5',
 'description': 'Library books, members and book borrowing.',
 'author': 'Daniel Reis',
 'depends': ['base'],
 'data': [
    'security/library_security.xml',
    'security/ir.model.access.csv',
    'views/library_menu.xml',
    'views/book_view.xml',
    'views/book_list_template.xml',
 ],
 'demo': [
    'data/res.partner.csv',
    'data/library.book.csv',
    'data/book_demo.xml',
 ],
 'application': True,
 'installable': True,
}
