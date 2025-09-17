import webbrowser
import os

def vista_html(df):
    # Estilos CSS para la tabla de salida del main.py
    estilos = """
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: lightgray;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px auto;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            background: white;
            border-radius: 8px;
            overflow: hidden;
        }
        th {
            background-color: #007BFF;
            color: white;
            padding: 12px;
            text-align: center;
        }
        td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }
        
    </style>
    """
    # Html para la visualización de la tabla
    html = f"""
    <html>
    <head>
        <title>Vuelos</title>
        {estilos}
    </head>
    <body>
        <h1>Tabla de vuelos asignados</h1>
        {df.to_html(index=False, escape=False)}
    </body>
    </html>
    """

    # Guardar en archivo
    file_path = "vuelos.html"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Archivo {file_path} generado correctamente.")
    webbrowser.open(f"file://{os.path.abspath(file_path)}")