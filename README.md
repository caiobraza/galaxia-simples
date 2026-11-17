# 🌌 Galáxia Espiral em Python (`turtle`)

Arte generativa que simula visualmente uma **Galáxia Espiral** em perspectiva 3D, com degradê de cores do núcleo às bordas, poeira cósmica e fundo estrelado, desenvolvida utilizando apenas bibliotecas nativas do Python.

## 📸 Resultado

<img width="1920" height="1080" alt="galaxy" src="https://github.com/user-attachments/assets/4d48b431-74a7-4f5a-a594-4bcae1a2d101" />


---

## ✨ Como funciona

A galáxia é construída em **5 camadas** sobrepostas para dar profundidade e realismo:

1. **Fundo Estrelado:** Espalha 140 estrelas distantes de tamanhos variados pela tela.
2. **Poeira Cósmica:** Cria uma névoa azulada concentrada próxima ao centro usando distribuição gaussiana.
3. **Braços Espirais:** Gera 4 braços simétricos que se curvam do centro para fora, mudando gradualmente de cor (do dourado quente no núcleo ao azul/violeta nas extremidades).
4. **Núcleo Galáctico:** Preenche a região central com alta densidade de estrelas douradas e um bojo luminoso.
5. **Estrelas de Destaque:** Adiciona pontos brancos maiores e mais brilhantes sobre a estrutura da galáxia.

---

## 🛠️ Tecnologias e Bibliotecas

Nenhuma instalação externa é necessária. O projeto utiliza apenas módulos padrão do **Python 3**:

* **`turtle`**: Criação da janela gráfica, renderização dos pontos e controle de frames (`tracer`) para animação rápida e fluida.
* **`math`**: Trigonometria (`sin`, `cos`, `pi`) para calcular as espirais e aplicar a inclinação em perspectiva 3D.
* **`colorsys`**: Conversão de cores **HSV para RGB** para gerar a transição suave de cores e brilho.
* **`random`**: Distribuição normal (`gauss`) e sorteios para criar variações naturais nas estrelas e na poeira.

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Baixe o arquivo `.py` deste repositório ou clone o projeto:
   ```bash
3. git clone [(https://github.com/caiobraza/galaxia-simples.git)]
