import flet as ft

#from views.home import homeView
from testerseite import testerseiteView
from testerseite2 import testerseite2View

class router:

    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": testerseite2View(page),
            "/testerseite":testerseiteView(page)
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self,route):
        self.body.content = self.routes[route.route]
        self.body.update()    
        

