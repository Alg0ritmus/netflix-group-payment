# TO DO:

1) csrf token -> mozes ho ziskat z cookies... better for security
file:///C:/Users/Patrik/Desktop/portfolio/DJANGO/reference/autorization.pdf#page=106&zoom=100,0,0

2) zmen URL admin/ na nieco ako @dmin77_  -> zabran automatizovany bruteforce utokom

3) enable django SECURE_SSL_REDIRECT & HSTS (restriction ze na moju stranku sa da pristupovat iba cez https)

4) logguj vsetko (audit loggs)

5) Deal with CORS (install cross-origin header ci jak):
file:///C:/Users/Patrik/Desktop/portfolio/DJANGO/reference/autorization.pdf#page=110&zoom=100,0,0

6) JWT nie je oficialne podporovany djangom (not secure)
ale existuju nejake kniznice... pozor!!! JWT uchovavaj v HttpOnly cookies nie localStorage (localStorage -> vulnerabilities XSS)


TO STUDY:
CORS
CSRF token
XSS attacks



---------------
python manage.py changepassword admin

password:
paSSw0rD_1 
