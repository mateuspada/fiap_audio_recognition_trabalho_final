# 🤖 Chat Conversacional com Reconhecimento de Voz

Este projeto simula um atendimento automatizado por voz, utilizando áudios pré-gravados, reconhecimento de fala com o **Azure Speech SDK**, reprodução via **pygame**, e lógica de decisão por palavras-chave.

## 🎯 Objetivo

Criar um sistema interativo que:
- Reproduz áudios de boas-vindas e opções.
- Escuta a resposta do usuário via microfone.
- Reconhece a fala e identifica palavras-chave.
- Executa ações com base na intenção detectada.
- Retorna ao menu caso a opção seja inválida ou não identificada.

---

## 🧠 Tecnologias Utilizadas

- Python 3.12
- [Azure Cognitive Services - Speech to Text](https://learn.microsoft.com/pt-br/azure/cognitive-services/speech-service/)
- [`pygame`](https://www.pygame.org/news)
- [`python-dotenv`](https://saurabh-kumar.com/python-dotenv/)

---

## 🗂️ Estrutura do Projeto

```
📁 projeto/
├── audios/                          # Arquivos de áudio (.wav)
│   ├── identificacao_empresa_e_saudacao.wav
│   ├── opcoes.wav
│   ├── opcao_1.wav
│   ├── opcao_2.wav
│   ├── opcao_3.wav
│   ├── opcao_4.wav
│   ├── opcao_nao_identificada.wav
│   ├── opcao_selecionada_1.wav
│   ├── opcao_selecionada_2.wav
│   ├── opcao_selecionada_3.wav
│   └── opcao_selecionada_4.wav
├── arquitetura/
│   └── Diagrama - Audio Recognition.png
├── .env                             # Variáveis de ambiente (chave da Azure)
├── main.py                          # Código principal do projeto
└── requirements.txt                 # Dependências do projeto
```

---

## ▶️ Como Executar

1. **Clone o repositório** e acesse a pasta do projeto.

2. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

3. **Configure sua chave do Azure Speech** no arquivo `.env`:

```env
AZURE_SPEECH_KEY=sua-chave-aqui
AZURE_SPEECH_REGION=sua-regiao-aqui
```

4. **Execute o sistema**:

```bash
python main.py
```

---

## 🔄 Fluxo Conversacional

1. Toca o áudio de saudação.
2. Apresenta as 4 opções disponíveis.
3. Escuta o usuário por até 10 segundos.
4. Compara a fala com palavras-chave e seleciona a ação:

| Opção | Palavras-chave relacionadas                         | Áudio Tocada                         |
|-------|------------------------------------------------------|--------------------------------------|
| 1     | consulta, consultar, saldo, conta                    | `opcao_selecionada_1.wav`           |
| 2     | simular, simulação, compra, internacional            | `opcao_selecionada_2.wav`           |
| 3     | falar, atendente, suporte                            | `opcao_selecionada_3.wav`           |
| 4     | sair, saindo, encerrar                               | `opcao_selecionada_4.wav` _(encerra)_

Caso a opção não seja reconhecida, o áudio `opcao_nao_identificada.wav` é tocado e o menu é repetido.

---

## 🧱 Arquitetura da Solução

![Arquitetura do Projeto](./arquitetura/Diagrama%20-%20Audio%20Recognition.png)

---

## 📝 Observações

- Os arquivos de áudio devem estar em formato `.wav` e na pasta correta.
- O reconhecimento de voz funciona melhor em ambientes silenciosos.
- O sistema pode ser expandido com interface gráfica, suporte a mais idiomas e conexões com APIs reais.

---

## 📦 Requisitos

**`requirements.txt`**
```
azure-cognitiveservices-speech==1.43.0
pygame==2.6.1
python-dotenv==1.0.1
```

---

## 👨‍🏫 Projeto para o MBA

Desenvolvido como parte do trabalho prático da disciplina de Audio Recognition.
