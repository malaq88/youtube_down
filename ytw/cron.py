import os
import schedule
import threading

def limpar_pasta_destino():
    output_folder = 'video_folder'  # Especifique o caminho completo da pasta de destino
    for file_name in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

def agendar_limpeza_pasta_destino():
    schedule.every(1).hour.do(limpar_pasta_destino)

    while True:
        schedule.run_pending()

def iniciar_agendamento():
    thread = threading.Thread(target=agendar_limpeza_pasta_destino)
    thread.daemon = True
    thread.start()