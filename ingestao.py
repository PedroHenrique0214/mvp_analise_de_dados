import requests, zipfile, io
import os

# Criar uma pasta para salvar os arquivos
os.makedirs("dados_leitos", exist_ok=True)

anos = range(2016, 2026)

for ano in anos:
    try:
        print(f"Baixando dados de {ano}...")
        url = f"https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/Leitos_SUS/xml/Leitos_{ano}.xml.zip"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Não foi possível baixar o ano {ano}.")
            continue

        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            arquivo_xml = z.namelist()[0]
            with z.open(arquivo_xml) as xml_file:
                conteudo = xml_file.read()

                # Salvar o XML em disco
                caminho_saida = f"dados_leitos/Leitos_{ano}.xml"
                with open(caminho_saida, "wb") as f:
                    f.write(conteudo)

        print(f"✅ {ano} salvo com sucesso.")

    except Exception as e:
        print(f"Erro ao processar o ano {ano}: {e}")
