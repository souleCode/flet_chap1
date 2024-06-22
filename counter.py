import flet as ft
from time import sleep


def main(page: ft.Page):
    page.title = "Counter"
    text = ft.Text(value="Counter App")
    page.add(text)

    for i in range(1, 11):
        text.value = "Counter" + str(i)
        page.update()
        sleep(1)

    pass


ft.app(target=main)
