from django.utils.deprecation import MiddlewareMixin # bypass , permite conectar con una accion el utils, ocuparemos el modelo customsetttings...

class CustomSessionMiddleware(MiddlewareMixin): #para comprobar que la acion sea correcta 
    def process_request(self, request):
        if not request.session.get('visits'):
            request.session['visits'] = 0
        request.session['visits'] += 1