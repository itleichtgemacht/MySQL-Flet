import flet as ft
import os
#from mysql.connector import MySQLConnection, Error
import mysql_functions as mf
    
def testerseiteView(page):

    def DoReadVerzeichnis():
        aktVerz = os.path.abspath(__file__)
        path = 'views\\'
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
 
    # ### AH
    # Erstelle Tabelle aus MySQL DB
    # ###
    list_view_table_books = ft.ListView(height=400, expand=1, spacing=0, padding=0)#, auto_scroll=True)
    def DoTable():

        table_books = ft.DataTable(
            heading_row_color=ft.colors.GREY_200,
            sort_ascending=True,
            border_radius=10,
            vertical_lines=ft.border.BorderSide(3, "blue"),
            horizontal_lines=ft.border.BorderSide(1, "green"),
            #fixed_rows={'headers': True},
            columns=[
                ft.DataColumn(ft.Text("Titel"), numeric=True),
                ft.DataColumn(ft.Text("ISBN")),
                ft.DataColumn(ft.Text("Author")),
            ],
            
        )

        list_view_table_books.controls.append(table_books)
        #all_books = mf.fetch_all_books()
        all_books = mf.find_all_books()
        #print('all_books:', all_books)



        for row in all_books:
            print('row: ', row)
            for spalten in row:
                    table_books.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Row([
                                    ft.IconButton("ADD_OUTLINED", icon_color="green", data=row, tooltip="Hinweistext hier"),
                                    ft.Text(spalten[0]),
                                ])),
                                ft.DataCell(ft.Text(spalten[1])),
                                ft.DataCell(ft.Text(spalten[2])),

                            ]
                        )
                    )
            list_view_table_books.update()


    def TuWas(e):
        DoTable()
        DoReadVerzeichnis()
        #page.update()
        





    resDesign = ft.Container(
                    height=450,
                    content=ft.Column(
                        controls=[
                            
                            ft.ResponsiveRow(
                                [
                                ft.Container(
                                    ft.Row([
                                        ft.Text("Lade Daten: ", weight=ft.FontWeight.BOLD),
                                        ft.IconButton(icon=ft.icons.DRIVE_FOLDER_UPLOAD, bgcolor="blue300", on_click=TuWas),
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
                                    list_view_table_books,
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