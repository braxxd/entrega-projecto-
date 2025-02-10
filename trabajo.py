import subprocess
import flet as ft

def ejecutar_lexer(input_code):
  
    proceso = subprocess.Popen(
        ["./lexer.exe"], 
        stdin=subprocess.PIPE,  
        stdout=subprocess.PIPE,  
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",  
        errors="replace"
    )

    
    salida, error = proceso.communicate(input_code)

    print(f"Salida del lexer: {salida}")
    print(f"Error del lexer: {error}")

    

    return salida if salida else error  


def main(page):
    page.title = "Lexer en Flet"
    page.vertical_alignment = ft.MainAxisAlignment.START

 
    input_field = ft.TextField(label="Introduce tu código", multiline=True, height=200)

    
    resultado_label = ft.Text(value="Resultado aparecerá aquí", size=15, color=ft.colors.BLACK)

    def on_execute_click(e):
        input_code = input_field.value.strip()  

        if not input_code:  
            resultado_label.value = "Por favor, ingrese código para analizar."
            page.update()
            return

       
        resultado_label.value = "Ejecutando lexer..."
        page.update()

        try:
          
            resultado = ejecutar_lexer(input_code)

          
            print(f"Resultado del lexer:\n{resultado}")

           
            resultado_label.value = resultado if resultado else "No se generó ningún resultado."
        
        except Exception as ex:
            resultado_label.value = f"Error al ejecutar el lexer: {str(ex)}"
            print(f"Error en on_execute_click: {ex}")

        page.update()

    def on_clear_click(e):
        input_field.value = ""  
        resultado_label.value = "Resultado aparecerá aquí"  
        page.update()  

    execute_button = ft.ElevatedButton("Ejecutar", on_click=on_execute_click)
    clear_button = ft.ElevatedButton("Limpiar", on_click=on_clear_click)

    
    column = ft.Column(
        controls=[
            input_field,
            execute_button,
            clear_button,
            resultado_label  
        ],
        spacing=10
    )

    page.add(column)

ft.app(target=main)