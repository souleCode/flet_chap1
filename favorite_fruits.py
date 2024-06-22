import flet as ft


def main(page: ft.page):

    page.add(
        ft.Row(controls=[
            ft.Text("Mon fruit préféré:\n")
        ]
        ),
        ft.Row(controls=[
            ft.Text("Pomme"),
            ft.Text("Mangue"),
            ft.Text("Olive")
        ]
        ),

        # columns
        ft.Column(controls=[
            ft.Text("\n\nMes plantes preferée:\n")
        ]
        ),
        ft.Column(controls=[
            ft.Text("Goyavier"),
            ft.Text("Manguier"),
            ft.Text("Datier")
        ]
        ),
    )


ft.app(main)
