import socket
import flet as ft

def main(page: ft.Page):
    page.title = "Escáner de Puertos"
    page.window_width = 320
    page.window_height = 500
    page.window_resizable = False

    def scan_ports(e):
        ip = ip_input.value
        result_list.controls.clear()
        page.update()
        for puerto in range(1, 1025):  # Escanear menos puertos para mayor rapidez
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.50)
            result = sock.connect_ex((ip, puerto))
            if result == 0:
                result_list.controls.append(ft.Text(f"Puerto Abierto: {puerto}", color=ft.colors.GREEN))
            else:
                result_list.controls.append(ft.Text(f"Puerto Cerrado: {puerto}", color=ft.colors.RED))
            sock.close()
            page.update()

    ip_input = ft.TextField(label="Ingrese la dirección IP:", width=250)
    scan_button = ft.ElevatedButton(text="Escanear", on_click=scan_ports)
    result_list = ft.ListView(expand=True, height=400, width=280)

    page.add(
        ft.Column(
            [
                ft.Container(
                    content=ip_input,
                    padding=ft.padding.all(10),
                    border=ft.border.all(1, ft.colors.BLUE),
                    border_radius=8,
                ),
                ft.Container(
                    content=scan_button,
                    padding=ft.padding.symmetric(vertical=5),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    content=result_list,
                    padding=ft.padding.all(10),
                    border=ft.border.all(1, ft.colors.BLUE),
                    border_radius=8,
                    height=400,
                    width=280,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )
    )

ft.app(target=main)
