def exists_word(word, instance):
    for index in range(len(instance)):
        _file = instance.search(index)
        info_data = {
            "palavra": word,
            "arquivo": _file["nome_do_arquivo"],
            "ocorrencias": [],
        }
        linha = 0

        for index in _file["linhas_do_arquivo"]:
            if word.lower() in index.lower():
                linha += 1
                info_data["ocorrencias"].append(
                  {
                    "linha": linha
                  }
                )

        search_info = []

        if len(info_data["ocorrencias"]) > 0:
            search_info.append(info_data)
    return search_info


def search_by_word(word, instance):
    for index in range(len(instance)):
        _file = instance.search(index)
        info_data = {
            "palavra": word,
            "arquivo": _file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        linha = 0

        for index in _file["linhas_do_arquivo"]:
            if word.lower() in index.lower():
                linha += 1
                info_data["ocorrencias"].append(
                    {
                      "linha": linha,
                      "conteudo": index,
                    }
                )

        search_info = []

        if len(info_data["ocorrencias"]) > 0:
            search_info.append(info_data)

    return search_info
