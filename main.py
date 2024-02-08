
# ### AH
# Emoji's: https://emojipedia.org/
# ###

import flet as ft
from router import router
from navbar import navbar

def main(page: ft.Page):
    page.title="TEST: MySQL"
    page.windows_width=800
    page.windows_height=600
    page.navigation_bar = navbar(page)
    navbarRouter = router(page)
    page.on_route_change = navbarRouter.route_change


   
    ueberschrift = ft.ResponsiveRow([
        ft.Text("TEST: MySQL", size=40, text_align=ft.TextAlign.CENTER, color="blue300"),
        ft.Divider()
    ])

    page.add(
        ueberschrift,
        navbarRouter.body
    )
    page.go('/')

ft.app(main)
