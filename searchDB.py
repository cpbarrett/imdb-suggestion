import cgi

form = cgi.FieldStorage()
search_term = form.getvalue('search_box')
print(search_term)
