import flet as ft

def navbar(page):

    def seitenAufruf(index):
        if index == 0:
            page.go('/')
        elif index == 1:
            page.go('/testerseite')

    # ### AH
    # ICON Browser:
    # https://gallery.flet.dev/icons-browser/
    # ###
    navbar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_OUTLINED, 
                                    selected_icon=ft.icons.HOME, label="Tester Seite 2"),
            ft.NavigationDestination(icon=ft.icons.AUDIOTRACK, label="Tester Seite"),
        ],
        on_change=lambda _: seitenAufruf(navbar.selected_index), 
        bgcolor=ft.colors.TEAL_50)
    return navbar