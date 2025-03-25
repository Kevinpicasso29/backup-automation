import os
import shutil
import datetime
import schedule
import time

# Função para realizar o backup
def perform_backup(source_dir, backup_dir):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_folder = os.path.join(backup_dir, f"backup_{timestamp}")
    
    try:
        # Criar o diretório de backup
        os.makedirs(backup_folder)
        print(f"Backup iniciado em {backup_folder}")
        
        # Copiar os arquivos do diretório fonte para o diretório de backup
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            backup_item = os.path.join(backup_folder, item)

            if os.path.isdir(source_item):
                shutil.copytree(source_item, backup_item)
            else:
                shutil.copy2(source_item, backup_item)
        
        print(f"Backup concluído em {backup_folder}")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função para agendar o backup diário
def schedule_daily_backup(source_dir, backup_dir):
    schedule.every().day.at("02:00").do(perform_backup, source_dir, backup_dir)  # Agendamento para 2h da manhã

    while True:
        schedule.run_pending()
        time.sleep(60)

# Função principal para iniciar o processo
if __name__ == "__main__":
    source_directory = "caminho/do/diretorio/origem"  # Caminho do diretório que será copiado
    backup_directory = "caminho/do/diretorio/backup"  # Caminho do diretório de backup

    print("Iniciando o agendamento de backups...")
    schedule_daily_backup(source_directory, backup_directory)



# Explicação do Código
#O script faz backup de arquivos de um diretório de origem (source_directory) para um diretório de destino (backup_directory).

#O backup é feito uma vez por dia, usando a biblioteca schedule, com horário configurado para 2h da manhã.

#Cada backup é armazenado em uma pasta com timestamp, para garantir que os backups sejam organizados e não sobrescrevam os anteriores.

#O código utiliza shutil para copiar arquivos e diretórios.
