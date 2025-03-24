import os
import time
import pygame
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

load_dotenv()

AUDIO_FOLDER = './audios'
SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION")

def tocar_audio(caminho_audio: str):
    if not os.path.exists(caminho_audio):
        print(f"[ERRO] Arquivo não encontrado: {caminho_audio}")
        return

    try:
        pygame.mixer.init()
        pygame.mixer.music.load(caminho_audio)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print(f"[ERRO] Falha ao tocar áudio {caminho_audio}: {e}")

def tocar_varios_audios(lista_audios: list):
    for nome_arquivo in lista_audios:
        caminho = os.path.join(AUDIO_FOLDER, nome_arquivo)
        tocar_audio(caminho)

def reproduzir_fluxo_inicial():
    saudacao = "identificacao_empresa_e_saudacao.wav"
    tocar_audio(os.path.join(AUDIO_FOLDER, saudacao))

def reproduzir_opcoes():
    lista_opcoes = [
        "opcoes.wav",
        "opcao_1.wav",
        "opcao_2.wav",
        "opcao_3.wav",
        "opcao_4.wav"
    ]

    tocar_varios_audios(lista_audios = lista_opcoes)
   
def reconhecer_audio_usuario(timeout_segundos=10) -> str:
    """
    Escuta o microfone por até `timeout_segundos` segundos e retorna a primeira fala reconhecida.
    Caso não reconheça nenhuma fala, retorna None.
    """
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    speech_config.speech_recognition_language = "pt-BR"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    recognized_text = None
    done = False

    def handle_final_result(evt):
        nonlocal recognized_text, done
        if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            recognized_text = evt.result.text
        done = True

    recognizer.recognized.connect(handle_final_result)
    recognizer.start_continuous_recognition()

    print(f"Aguardando resposta do usuário por até {timeout_segundos} segundos...")
    start_time = time.time()
    while not done and time.time() - start_time < timeout_segundos:
        time.sleep(0.1)

    recognizer.stop_continuous_recognition()
    if recognized_text:
        print(f"Texto reconhecido: {recognized_text}")
    else:
        print("Nenhuma fala reconhecida dentro do tempo limite.")

    return recognized_text

def identificar_opcao(texto: str) -> int:
    texto = texto.lower()

    # Palavras-chave por opção
    op1 = ["consulta", "consultar", "saldo", "conta"]
    op2 = ["simular", "simulação", "simula", "compra", "internacional"]
    op3 = ["falar", "fala", "atendente", "atendentes", "suporte"]
    op4 = ["sair", "saindo", "encerrar"]

    if any(p in texto for p in op1):
        return 1
    elif any(p in texto for p in op2):
        return 2
    elif any(p in texto for p in op3):
        return 3
    elif any(p in texto for p in op4):
        return 4
    else:
        return 0 # Não reconhecido

def main():
    print("Iniciando o chat conversacional...")
    reproduzir_fluxo_inicial()

    opcao_reconhecida = 0

    while opcao_reconhecida == 0:
        reproduzir_opcoes()
        texto_usuario = reconhecer_audio_usuario(timeout_segundos=10)

        if not texto_usuario:
            tocar_audio(os.path.join(AUDIO_FOLDER, "opcao_nao_identificada.wav"))
            continue

        print(f"Usuário disse: {texto_usuario}")
        opcao_reconhecida = identificar_opcao(texto_usuario)

        if opcao_reconhecida == 0:
            print("Nenhuma opção válida identificada.")
            tocar_audio(os.path.join(AUDIO_FOLDER, "opcao_nao_identificada.wav"))
        elif opcao_reconhecida == 4:
            tocar_audio(os.path.join(AUDIO_FOLDER, "opcao_selecionada_4.wav"))
            print("Encerrando o atendimento.")
            return
        else:
            caminho_audio = os.path.join(AUDIO_FOLDER, f"opcao_selecionada_{opcao_reconhecida}.wav")
            tocar_audio(caminho_audio)
            opcao_reconhecida = 0  # Reset para voltar ao menu

    print("Atendimento encerrado.")

if __name__ == "__main__":
    main()
