import flet as ft

def main(page: ft.Page):
  page.title = "Simulador de Juros Composto"
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.vertical_alignment = ft.MainAxisAlignment.CENTER

  def calcular_juros_composto(e):
    inicial = float(valor_inicial.value.replace(",", "."))
    mensal = float(valor_mensal.value.replace(",", "."))
    juros = float(taxa_juros.value.replace(",", ".")) / 100
    time = float(tempo.value)

    valor_total = inicial + (mensal * time)
    valor_total *= (1 + juros) ** time

    resultado.value = f"R$ {valor_total:.2f}".replace(".", ",")
    resultado.visible = True
    page.update()
    
  text_titulo = ft.Text("Simulador de Juros Composto", size=30, weight=ft.FontWeight.BOLD)
  text_valor_inicial = ft.Text("Valor inicial:", size=20)
  valor_inicial = ft.TextField(label="0,00", width=200)
  text_valor_mensal = ft.Text("Valor mensal:", size=20)
  valor_mensal = ft.TextField(label="0,00", width=200)
  text_taxa_juros = ft.Text("Taxa de juros(Anual):", size=20)
  taxa_juros = ft.TextField(label="0,00", width=200)
  text_tempo = ft.Text("Tempo (Anos):", size=20)
  tempo = ft.TextField(label="0", width=200)
  botão = ft.ElevatedButton("Calcular", width=200, on_click=calcular_juros_composto)
  text_resultado = ft.Text("Resultado:", size=20)
  resultado = ft.Text("0, 00", size=20, weight=ft.FontWeight.BOLD, visible=False)

  page.add(
    text_titulo,
    text_valor_inicial,
    valor_inicial,
    text_valor_mensal,
    valor_mensal,
    text_taxa_juros,
    taxa_juros,
    text_tempo,
    tempo,
    text_resultado,
    resultado,
    botão,
  ) 

ft.app(target=main)