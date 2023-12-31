from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    _file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(_file),
        "linhas_do_arquivo": (_file),
    }

    instance.enqueue(data)

    sys.stdout.write(str(data))
    return data


def remove(instance):
    if not instance or instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    file_delete = instance.dequeue()
    file_path = file_delete["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {file_path} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        info_data = instance.search(position)
        sys.stdout.write(str(info_data))
        return str(info_data)
    except IndexError:
        sys.stderr.write("Posição inválida")
