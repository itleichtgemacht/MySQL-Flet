import flet as ft
import os

    
def testerseiteView(page):

    def DoReadVerzeichnis(e):
        aktVerz = os.path.abspath(__file__)
        path = '\\'
        files = os.listdir(path)
        #alleDateiNamen.controls.append("Liste:")
        for file in files:
            print(aktVerz + file)
            checkbox = ft.Checkbox(value=False, fill_color="blue300")
            DateiName = ft.Text(value=file,size=20, color="blue300")
            DateiNameReihe = ft.Row(controls=[checkbox, DateiName])
            alleDateiNamen.controls.append(DateiNameReihe)
        alleDateiNamen.update()

    alleDateiNamen = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True, height=400)
 
    resDesign = ft.Container(
                    height=450,
                    content=ft.Column(
                        controls=[
                            
                            ft.ResponsiveRow(
                                [
                                ft.Container(
                                    ft.Row([
                                        ft.Text("Lade Daten: ", weight=ft.FontWeight.BOLD),
                                        ft.IconButton(icon=ft.icons.DRIVE_FOLDER_UPLOAD, bgcolor="blue300", on_click=DoReadVerzeichnis),
                                    ]),
                                    padding=5,
                                    bgcolor="Grey100",
                                    col={"md": 2},
                                ),
                                ft.Container(
                                    alleDateiNamen,
                                    padding=5,
                                    bgcolor="blue100",
                                    col={"md": 4},
                                ),
                                ft.Container(
                                    
                                    padding=5,
                                    bgcolor="blue50",
                                    col={"md": 6},
                                ),
                            ],
                        ),
                            
                    ] # Controls von Column
                ) # Column von Container
            ) # Container




    testerseite= ft.SafeArea(
        
        ft.Container(
            height=450,
            content=ft.Column(
                controls=[
                    resDesign,
                ]
            ) 
        )
    ) 

    return testerseite