# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

from pathlib import Path
import pandas as pd


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    carpeta_test = Path("files/input/test")
    datos_test = []
    for subcarpeta in carpeta_test.iterdir():
        if subcarpeta.is_dir():
            target = subcarpeta.name
            for archivo in subcarpeta.glob("*.txt"):  
                with archivo.open("r", encoding="utf-8") as f:
                    linea = f.readline().strip()
                    print(f"{archivo.name}: {linea}")

                    if '-' in linea:
                        frase = linea.rsplit('-', -1)[-1].strip()
                    else:
                        frase = linea

                    datos_test.append({""
                    "phrase": frase,
                    "target": target})

    carpeta_train = Path("files/input/train")
    datos_train = []
    for subcarpeta in carpeta_train.iterdir():
        if subcarpeta.is_dir():
            target = subcarpeta.name
            for archivo in subcarpeta.glob("*.txt"):  
                with archivo.open("r", encoding="utf-8") as f:
                    linea = f.readline().strip()
                    print(f"{archivo.name}: {linea}")

                    if '-' in linea:
                        frase = linea.rsplit('-', -1)[-1].strip()
                    else:
                        frase = linea

                    datos_train.append({""
                    "phrase": frase,
                    "target": target})
            

    test_dataset = pd.DataFrame(datos_test)
    train_dataset = pd.DataFrame(datos_train)
    train_dataset["phrase"] = train_dataset["phrase"].str.strip('"\'')
    test_dataset["phrase"] = test_dataset["phrase"].str.strip('"\'')


    test_dataset.to_csv("files/output/test_dataset.csv", index=False, encoding="utf-8")
    train_dataset.to_csv("files/output/train_dataset.csv", index=False, encoding="utf-8")
  
   




pregunta_01()
