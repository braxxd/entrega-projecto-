import subprocess
import flet as ft

def ejecutar_lexer(input_code):
    # Inicia el proceso del lexer
    proceso = subprocess.Popen(
        ["./lexer.exe"], 
        stdin=subprocess.PIPE,  
        stdout=subprocess.PIPE,  
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",  # Forzar UTF-8
        errors="replace"
    )

    # Enviar el código al lexer y capturar la salida
    salida, error = proceso.communicate(input_code)

    # Depuración: Mostrar salida del lexer
    print(f"Salida del lexer: {salida}")
    print(f"Error del lexer: {error}")

    # Corregir posibles problemas de codificación

    return salida if salida else error  # Retorna la salida del lexer o el error si no hay salida


def main(page):
    page.title = "Lexer en Flet"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Crear un campo de texto para ingresar código
    input_field = ft.TextField(label="Introduce tu código", multiline=True, height=200)

    # Crear un label para mostrar los resultados del lexer
    resultado_label = ft.Text(value="Resultado aparecerá aquí", size=15, color=ft.colors.BLACK)

    def on_execute_click(e):
        input_code = input_field.value.strip()  # Obtener el código y quitar espacios en blanco

        if not input_code:  
            resultado_label.value = "Por favor, ingrese código para analizar."
            page.update()
            return

        # Mostrar mensaje de ejecución
        resultado_label.value = "Ejecutando lexer..."
        page.update()

        try:
            # Ejecutar lexer y obtener resultado
            resultado = ejecutar_lexer(input_code)

            # Depuración en consola
            print(f"Resultado del lexer:\n{resultado}")

            # Mostrar resultado en la interfaz
            resultado_label.value = resultado if resultado else "No se generó ningún resultado."
        
        except Exception as ex:
            resultado_label.value = f"Error al ejecutar el lexer: {str(ex)}"
            print(f"Error en on_execute_click: {ex}")

        # Actualizar la interfaz
        page.update()

    def on_clear_click(e):
        input_field.value = ""  # Limpiar el campo de entrada
        resultado_label.value = "Resultado aparecerá aquí"  # Restablecer el label
        page.update()  

    execute_button = ft.ElevatedButton("Ejecutar", on_click=on_execute_click)
    clear_button = ft.ElevatedButton("Limpiar", on_click=on_clear_click)

    # Crear la columna con los controles
    column = ft.Column(
        controls=[
            input_field,
            execute_button,
            clear_button,
            resultado_label  # Agregar el label con el resultado
        ],
        spacing=10
    )

    page.add(column)

ft.app(target=main)