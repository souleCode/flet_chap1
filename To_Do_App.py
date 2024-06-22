import flet as ft


def main(page: ft.page):
    page.title = "To_Do_App"
    input_text = ft.TextField(
        hint_text="Que voulez vous faire Monsieur/Madame", width=250)

    # Button clicked founction
    def button_clicked(e):
        page.add(
            ft.Checkbox(label=input_text.value),
        )

    page.add(
        ft.Row([
            input_text,
            ft.ElevatedButton(text="Ajouter", on_click=button_clicked)
        ]

        )
    )


ft.app(main)
