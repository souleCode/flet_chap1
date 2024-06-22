import flet as ft


def main(page: ft.Page):
    page.add(ft.Text("Hello, Flet!"))
    page.title = "Bienvenue"
    text = ft.Text(
        value="Mon premier application flutter sous pyton!", color='yellow')
    page.controls.append(text)
    page.update()


ft.app(target=main)
