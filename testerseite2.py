# ### AH
# CRUD - Beispiel mit MySQL DB (books)
# - CRUD Source Code zur DB Abfrage ist in folgende Py-Dateien ausgelagert:
#   ./MySQLconfig/app.ini:          Parameter für den MySQL DB Connect
#   ./mysql_functions.py:           SQL funktionen CRUD
#   ./MySQLconfig/passwortMD.py:    Erstellt ein verschlüsselted Passwort
#   ./pip.txt:                      Installierte Package's zum Release Zeitpunkt

# =====
# Design wird unter ResponsiveRow erstellt, somit werden die Spalten an die Fenstergröße angepasst
# 
# ###
# Author:   Armin Hünniger
# Stand:    08.02.2024
# ###

#


import flet as ft
#import os
#from mysql.connector import MySQLConnection, Error
import mysql_functions as mf
import functools


    
def testerseite2View(page):


    def page_resize(e):
        if page.width < 576: pwValue = "xs - <576px"
        if page.width >= 576: pwValue = "xs - ≥576px < 768"
        if page.width >= 768: pwValue = "md - ≥768px < 992"
        if page.width >= 992: pwValue = "lg - ≥992px < 1200"
        if page.width >= 1200: pwValue = "xl - ≥1200px < 1400"
        if page.width >= 1400: pwValue = "xxl - ≥1400px max"
        
        pw.value = f"{page.width} px (Responsive Wert: {pwValue})"
        pw.update()
    page.on_resize = page_resize

    pw = ft.Text(bottom=20, right=50)
    page.overlay.append(pw) 



    # ### AH
    # Definiert Header Zeile der Tabelle
    # Author:   Armin Hünniger
    # Stand:    07.02.2024
    # ###
    tblHeader = ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text("Aktion: ", weight=ft.FontWeight.BOLD),
                            padding=5,
                            bgcolor="Yellow100",
                            col={"sm": 6, "md": 2, "xl": 2},
                        ),
                        ft.Container(
                            ft.Text("Titel: ", weight=ft.FontWeight.BOLD),
                            padding=5,
                            bgcolor="Yellow200",
                            col={"sm": 6, "md": 4, "xl": 4},
                        ),
                        ft.Container(
                            ft.Text("ISBN: ", weight=ft.FontWeight.BOLD),
                            padding=5,
                            bgcolor="Yellow300",
                            col={"sm": 6, "md": 2, "xl": 2},
                        ),
                        ft.Container(
                            ft.Text("Author: ", weight=ft.FontWeight.BOLD),
                            padding=5,
                            #margin=10,
                            bgcolor="Yellow400",
                            col={"sm": 6, "md": 4, "xl": 4},
                        ),
                    ],
                )       

    # ### AH
    # Definiert Fuß Zeile der Tabelle
    # Author:   Armin Hünniger
    # Stand:    07.02.2024
    # ###
    tblFooter = ft.ResponsiveRow(
                    [
                        ft.Container(
                            ft.Text("(c) Armin Hünniger 02.2024 ", weight=ft.FontWeight.BOLD),
                            padding=5,
                            bgcolor="blue00",
                            col={"sm": 6, "md": 6, "xl": 6},
                        ),
                        ft.Container(
                            ft.Text(" ", weight=ft.FontWeight.BOLD),
                            padding=5,
                            bgcolor="blue400",
                            col={"sm": 6, "md": 6, "xl": 6},
                        ),
                    ],
                )       


    # ### AH
    # Definiert Body Zeile der Tabelle
    # Author:   Armin Hünniger
    # Stand:    07.02.2024
    # ###
    tblBody = ft.Column( controls=[ ], )
    
    # ### AH
    # Definiert Fomular zum Ändern der ausgewählten Zeile
    # Author:   Armin Hünniger
    # Stand:    07.02.2024
    # ###
    tbID=ft.TextField(label="ID",hint_text="ID des buches",border=ft.InputBorder.UNDERLINE,read_only=True)
    tbTitel=ft.TextField(label="Titel des buches", border=ft.InputBorder.UNDERLINE)
    tbISBN=ft.TextField(label="ISBN", border=ft.InputBorder.UNDERLINE)

    def btnNeueZeile(e):
        formEdit.visible=True
        print("btnNeueZeile: on_click")
        tbID.value='0'
        page.update()
            
    def btnUpdateRow(e):
        print(f"{tbID.value} {tbTitel.value} {tbISBN.value}")
        mf.update_by_id(tbID.value,tbTitel.value,tbISBN.value)
        tbID.value=""
        tbTitel.value=""
        tbISBN.value=""
    

    def btnRefreschZeile(e):
        tbID.value=""
        tbTitel.value=""
        tbISBN.value=""
        page.update()


    formEdit =  ft.ResponsiveRow(
                    [
                        ft.Container(ft.Row([
                                            ft.IconButton("ADD", icon_color="green", tooltip="Daten hinzufügen", on_click=btnNeueZeile),
                                            ft.IconButton("EDIT", icon_color="green", tooltip="Änderungen übernehmen (Neu bzw. Ändern)", on_click=btnUpdateRow),
                                            ft.IconButton("REFRESH", icon_color="green", tooltip="Änderungen verwerfen", on_click=btnRefreschZeile),
                                        ]),
                                        padding=5,
                                        bgcolor="Green100",
                                        col={"sm": 6, "md": 2, "xl": 2},
                                    ),
                        ft.Container(tbID,
                                        padding=5,
                                        bgcolor="Green400",
                                        col={"sm": 6, "md": 2, "xl": 2},
                                    ),
                        ft.Container(tbTitel,
                                        padding=5,
                                        bgcolor="Green200",
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                        ft.Container(tbISBN,
                                        padding=5,
                                        bgcolor="Green300",
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                    ], height=60,
                )
    #formEdit.visible=False
                
    # ### AH
    # Tabellen Funktionen
    # Author:   Armin Hünniger
    # Stand:    07.02.2024
    # ###
    
    
    
    
    def btnEditRow(e,d):
        #print(f"{e}. Zeile wurde ausgewählt")
        data = mf.find_by_id(e)
        for row in data:
            for spalten in row:
                print(f"{spalten[0]} --> {spalten[1]}")

                tbID.value=spalten[0]
                tbTitel.value=spalten[1]
                tbISBN.value=spalten[2]
                
                page.update()


    def btnDeleteRow(e,d):
        data = mf.find_by_id(e)
        for row in data:
            for spalten in row:
                tbID.value=spalten[0]
                tbTitel.value=spalten[1]
                tbISBN.value=spalten[2]
                page.update()
        mf.delete_by_id(tbID.value)
       
    def loadRows(daten):
        __datas = daten
        for row in __datas:
            #print('row: ', row)
            for spalten in row:
                #print(spalten[0])
                #a=spalten[0]
                #print(a)
                edBtn = ft.IconButton("EDIT", icon_color="green", 
                                        tooltip="Daten ändern", 
                                        on_click=functools.partial(btnEditRow, spalten[0]),
                                    )
                
                delBtn = ft.IconButton("DELETE", icon_color="red", 
                                        tooltip="Daten löschen", 
                                        on_click=functools.partial(btnDeleteRow, spalten[0]),
                                    )
                
                
                tblRow = ft.ResponsiveRow(
                    [
                        ft.Container(ft.Row([
                                            edBtn,
                                            delBtn,
                                           
                                        ], 
                                            #vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        ),
                                        #padding = ft.padding.only(left=10),
                                        #margin = ft.margin.only(left=10),
                                        #padding = 5,
                                        bgcolor="Yellow100",
                                        col={"sm": 6, "md": 2, "xl": 2},
                                    ),

                        #ft.Container(ft.Text(spalten[0]),visible=False ),
                        ft.Container(ft.Text(spalten[1]),
                                        #padding = ft.padding.only(left=10),
                                        #margin =ft. margin.only(left=10),
                                        padding = 5,
                                        bgcolor="Yellow200",
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                        ft.Container(ft.Text(spalten[2]),
                                        #padding = ft.padding.only(left=10),
                                        #margin = ft.margin.only(left=10),
                                        padding = 5,
                                        bgcolor="Yellow300",
                                        col={"sm": 6, "md": 2, "xl": 2},
                                    ),
                        ft.Container(ft.Text(spalten[3]),
                                        #padding = ft.padding.only(left=10),
                                        #margin =ft. margin.only(left=10),
                                        padding = 5,
                                        bgcolor="Yellow400",
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                    ], height=35
                )
                tblBody.controls.append(tblRow)

        tblBody.update()



        

    def TuWas(e):
        data = mf.find_all_books()
        loadRows(data)

    resDesign = ft.Container(
                    height=450,
                    content=ft.Column(
                        controls=[
                            ft.ResponsiveRow(
                                [
                                    ft.Container(
                                        ft.Row([
                                            ft.Text("Tu Was: ", weight=ft.FontWeight.BOLD),
                                            ft.IconButton(icon=ft.icons.DRIVE_FOLDER_UPLOAD, bgcolor="blue300", on_click=TuWas),
                                        ]),
                                        padding=5,
                                        bgcolor="Grey100",
                                        col={"md": 12},
                                    ),
                                ],
                            ),                
                                        
                            ft.ResponsiveRow(
                                [
                                    ft.Container(
                                        ft.Column(
                                            controls=[
                                                # hier noch zwei Columns formEdit
                                                ft.Column(controls=[formEdit,]),
                                                ft.Column(controls=[tblHeader,]),
                                                ft.Column(scroll=ft.ScrollMode.ALWAYS,expand=True,controls=[tblBody,]),
                                                ft.Column(controls=[tblFooter,]),
                                        ],),
                                        
                                        padding=5,
                                        bgcolor="Yellow50",
                                        col={"md": 12},
                                    ),
                                ],
                                height = 500,
                            ),         
                                               
                            
                        
                    ] # Controls von Column
                ) # Column von Container
            ) # Container


    testerseite2 = ft.SafeArea(
        
        ft.Container(
            #height=450,
            content=ft.Column(
                controls=[
                    resDesign,
                    
                ]
            ) 
        )
    ) 

    return testerseite2