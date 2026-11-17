# --- 1. IMPORTAÇÃO DAS BIBLIOTECAS ---
import turtle    # Biblioteca nativa para criar uma janela e desenhar formas/pontos na tela
import colorsys  # Biblioteca para converter cores do formato HSV (matiz/brilho) para RGB
import math      # Biblioteca de matemática (fornece seno, cosseno, pi, etc.)
import random    # Biblioteca para sortear números aleatórios

# --- 2. CONFIGURAÇÕES INICIAIS ---
random.seed(7)  # Fixa o sorteio aleatório: garante que a galáxia saia sempre igual toda vez que rodar
TILT = 0.45     # Define o ângulo de inclinação da galáxia na tela (em radianos)

# --- 3. PREPARANDO A JANELA (TELA) ---
screen = turtle.Screen()     # Cria a janela gráfica onde o desenho vai aparecer
screen.setup(780, 480)       # Define o tamanho da janela: 780 pixels de largura por 480 de altura
screen.bgcolor("#03030b")    # Pinta o fundo da janela com um azul bem escuro (cor do espaço)
screen.colormode(1.0)        # Avisa o Python que as cores RGB vão usar valores decimais de 0.0 a 1.0
screen.tracer(35)            # Atualiza a tela a cada 35 pontos desenhados (deixa a animação bem mais rápida)

# --- 4. PREPARANDO O PINCEL ---
t = turtle.Turtle()          # Cria o "pincel" que vai desenhar os pontos na tela
t.hideturtle()               # Esconde a setinha do pincel para não atrapalhar o visual
t.speed(0)                   # Coloca a velocidade de movimento do pincel no máximo possível
t.penup()                    # Levanta o pincel do papel (ele anda pela tela sem riscar linhas entre os pontos)

# --- 5. FUNÇÕES DE APOIO (COR E POSIÇÃO) ---
def glow(h, v=1.0):
    # Gera cores luminosas no sistema HSV e converte para RGB (que a tela entende)
    return colorsys.hsv_to_rgb(h % 1, 0.7, v)  # h = cor, 0.7 = saturação, v = brilho

def place(x, y):
    # Transforma coordenadas planas (2D) em uma perspectiva inclinada (efeito 3D)
    y *= 0.55                              # Achata a altura (Y) para o círculo parecer um disco visto de lado
    c, s = math.cos(TILT), math.sin(TILT)  # Calcula o cosseno e seno do ângulo de inclinação
    t.goto(x * c - y * s, x * s + y * c)   # Move o pincel para a nova posição já rotacionada

# --- 6. CAMADAS DA GALÁXIA ---
def stars():
    # Camada 1: Desenha 140 estrelas brancas distantes no fundo do espaço
    for _ in range(140):                        # Repete o bloco abaixo 140 vezes
        x = random.randint(-385, 385)           # Sorteia uma posição horizontal dentro da largura da janela
        y = random.randint(-235, 235)           # Sorteia uma posição vertical dentro da altura da janela
        t.goto(x, y)                            # Move o pincel diretamente para a posição sorteada
        t.dot(random.randint(1, 3), "white")    # Desenha um ponto branco de tamanho entre 1 e 3 pixels

def dust():
    # Camada 2: Cria uma névoa/poeira cósmica azulada concentrada perto do centro
    for _ in range(700):                        # Repete o bloco abaixo 700 vezes
        r = random.gauss(0, 120)                # Sorteia a distância do centro (concentra mais pontos no meio)
        a = random.uniform(0, 6.283)            # Sorteia um ângulo completo ao redor do círculo (0 a 2*pi)
        place(r * math.cos(a), r * math.sin(a)) # Converte distância/ângulo em X e Y e aplica a inclinação 3D
        t.dot(random.randint(2, 4), glow(0.7, 0.3)) # Desenha pontos azulados (0.7) com brilho fraco (0.3)

def arms(count):
    # Camada 3: Constrói os 4 braços espirais principais da galáxia
    for i in range(count):                      # Avança passo a passo do centro até a borda (900 vezes)
        for k in range(4):                      # Para cada passo, desenha 1 estrela em cada um dos 4 braços
            d = i / count                       # Calcula o progresso atual: 0.0 (centro) até 1.0 (ponta)
            a = k * math.pi / 2 + d * 5.5       # Separa os 4 braços em 90° e curva conforme se afasta
            r = 10 + d * 290                    # Define o raio: começa perto do centro (10) e vai até 300
            s = 4 + d * 26                      # Define a dispersão: estrelas mais espalhadas nas pontas
            x = r * math.cos(a) + random.gauss(0, s) # Calcula X na espiral + um desvio natural aleatório
            y = r * math.sin(a) + random.gauss(0, s) # Calcula Y na espiral + um desvio natural aleatório
            place(x, y)                         # Move o pincel para a posição final com inclinação 3D
            hue = 0.13 - d * 0.55               # Muda a cor do dourado (centro) até o azul/roxo (bordas)
            v = random.uniform(0.6, 1)          # Sorteia o brilho de cada estrela para dar profundidade
            size = random.randint(2, 4)         # Sorteia o tamanho da estrela (2 a 4 pixels)
            t.dot(size, glow(hue, v))           # Desenha a estrela colorida na tela

def core():
    # Camada 4: Preenche o núcleo central com 260 estrelas douradas bem juntas
    for _ in range(260):                        # Repete o bloco abaixo 260 vezes
        r = random.gauss(0, 26)                 # Raio pequeno para manter as estrelas agrupadas no miolo
        a = random.uniform(0, 6.283)            # Sorteia um ângulo aleatório em 360 graus
        place(r * math.cos(a), r * math.sin(a)) # Posiciona o pincel com inclinação 3D
        t.dot(random.randint(2, 5), glow(0.12)) # Desenha pontos dourados (0.12) com brilho máximo

def sparkle():
    # Camada 5: Adiciona 40 estrelas maiores e mais brilhantes sobre a galáxia
    for _ in range(40):                         # Repete o bloco abaixo 40 vezes
        r = random.gauss(0, 150)                # Sorteia distância ao longo da galáxia
        a = random.uniform(0, 6.283)            # Sorteia um ângulo aleatório
        place(r * math.cos(a), r * math.sin(a)) # Posiciona o pincel com inclinação 3D
        t.dot(random.randint(5, 8), "white")    # Desenha pontos brancos maiores (5 a 8 pixels) para destaque

# --- 7. EXECUÇÃO DO DESENHO (ORDEM DAS CAMADAS) ---
stars()                 # 1º: Desenha o céu estrelado no fundo
dust()                  # 2º: Desenha a poeira cósmica
arms(900)               # 3º: Desenha os 4 braços espirais (900 x 4 = 3.600 estrelas)
core()                  # 4º: Desenha o núcleo dourado denso
sparkle()               # 5º: Desenha as estrelas brilhantes de destaque
t.goto(0, 0)            # Vai exatamente para o centro da tela (origem 0, 0)
t.dot(26, "#fff3c4")    # Desenha o ponto central super luminoso (bojo galáctico)

screen.update()         # Garante que os últimos pontos restantes sejam mostrados na tela
turtle.done()           # Mantém a janela aberta até você clicar no X para fechar
