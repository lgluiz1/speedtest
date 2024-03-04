import flet as ft
from time import sleep
from speedtest import Speedtest


def main(page: ft.Page):
    page.title = "LGSpeedTest"
    page.bgcolor ="#000000"
    page.fonts = {"Honk": "./assets/fonts/Honk.ttf",
                  "Inconsolata": "https://fonts.googleapis.com/css2?family=Inconsolata:wght@200..900&display=swap",
                  "Anta": "https://fonts.googleapis.com/css2?family=Anta&display=swap"}
    page.padding = 30
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"


    
    linha_inicial = ft.Text("Pressione para inicia teste...", size=10)
    linha_01 = ft.Text(value="", size=15,color="#000000")
    linha_02 = ft.Text(value="", size=15,color="#000000")
    linha_03 = ft.Text(value="", size=15,color="#2F4A20")
    pb_1 = ft.ProgressBar(width=300,opacity=0, bgcolor="#0000ff", color="#ffff")
    linha_04 = ft.Text(value="", size=15,color="#2F4A20")
    linha_05 = ft.Text(value="", size=15,color="#2F4A20")
    linha_06 = ft.Text(value="", size=15,color="#000000")
    pb_2 = ft.ProgressBar(width=300,opacity=0, bgcolor="#0000ff", color="#ffff")
    linha_07 = ft.Text(value="", size=15,color="#2F4A20")
    linha_08 = ft.Text(value="", size=15,color="#2F4A20")
    linha_9 = ft.Text(value="")
    credts = ft.Row(controls=[linha_9], alignment="center")
    
    terminal = ft.Column([linha_inicial,linha_01,linha_02,linha_03,pb_1,linha_04,linha_05,linha_06,pb_2,linha_07,linha_08,credts])
    

    


    def resetar(e):
        linha_01.value = ""
        linha_02.value = ""
        linha_03.value = ""
        pb_1.opacity = 0
        linha_04.value = ""
        linha_05.value = ""
        linha_06.value = ""
        pb_2.opacity = 0
        linha_07.value = ""
        linha_08.value = "" 
        inicia.text = ""
        linha_9.value= ""     
        page.update()
        
        # Chamando a função iniciar após a redefinição e atualização da interface
        iniciar(e)

    def iniciar(e):
        linha_inicial.value = ""
        inicia.text = ""
        inicia.on_click = ""
        inicia.icon =""
        inicia.width = 0
        reseta.width = 0
        reseta.text = ""
        reseta.icon = ""
        # Define o texto "Aguarde" uma vez
        page.update()
        layout.width = 700
        layout.height = 400
        aguarda.width = 150
        aguarda.text = "Aguarda"
        aguarda.icon = "Autorenew"
        page.update()
        linha_01.value ="Aguarde Estamos Iniciando a Verificação da Sua Rede"
        page.update()
        st = Speedtest()
        st.get_best_server()
        if st == "Forbidden":
            aguarda.text = "ERRO"
        # Obtém os detalhes do servidor utilizado
        server_details = st.results.dict()        
        linha_02.value = f"Você esta conectado na {server_details['server']['sponsor']}, Localizado em {server_details['server']['country']}, na cidade de {server_details['server']['name']}"
        page.update()
        sleep(2)
        linha_03.value = f"Iniciando Teste de Download da Sua Conexão"
        sleep(1)
        pb_1.opacity = 1
        pb_1.color = "#ffffff"
        page.update()
        download = st.download()
        pb_1.color = "#0000ff"
        page.update()
        linha_04.value = f"Seus Velocidade De Download e {download / 1_000_000:.2f} Mbs"
        page.update()
        sleep(2)
        linha_05.value = "Iniciando os testes para verificação do Upload"
        sleep(1)
        linha_06.value = "Iniciando verificaçao do Upload"
        page.update()
        sleep(2)
        pb_2.opacity = 1
        pb_2.color = "#ffffff"
        page.update()
        upload = st.upload()
        pb_2.color = "#0000ff"
        page.update()
        sleep(2)
        linha_07.value = f"Seus Velocidade De Upload e {upload / 1_000_000:.2f} Mbs"
        page.update()
        linha_08.value = f"Teste Finalizado Sua Velocidade de Download e {download / 1_000_000:.2f}Mbs e seu Upload {upload / 1_000_000:.2f}Mbs"
        page.update()
        aguarda.text = ""  # Remove o texto do botão
        aguarda.width = 0   # Define a largura do botão como 0, tornando-o invisível
        aguarda.icon = ""   # Remove o ícone do botão
        reseta.width = 180
        reseta.text = "Refazer Teste"
        reseta.icon = "Restart"
        page.update()
        sleep(2)
        linha_9.value = "Desenvolvido Por @LGLUIZ1"
        page.update()
            

    logo = ft.Row(controls=[ft.Image(src="./assets/img/logo.png")], alignment=ft.MainAxisAlignment.CENTER)
    inicia = ft.ElevatedButton(text="Inicia Teste", icon="Speed",width=150, on_click=iniciar)
    reseta = ft.ElevatedButton(text="", icon="",width=0, on_click=resetar)
    aguarda = ft.ElevatedButton(text="", icon="",width=0,)
    botoes = ft.Row(controls=[inicia,reseta,aguarda], alignment="center")
    

    
    
    layout = ft.Container(
        content=terminal,
        bgcolor=ft.colors.WHITE,
        width=200,
        height=100,
        border_radius= 30,
        padding=30,
        animate=ft.animation.Animation(2000,"bounceOut")
        
        
    )
    
    
    page.add(logo,layout,botoes)
ft.app(target=main)