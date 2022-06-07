
def img_gray_to_dataframe(img):
    '''
    Pasamos de una matriz con valores de entre 0 y 255 a un dataframe con los valores unicos y sus repeticiones
    para poder plotearlo con plotly de manera mucho mas sencilla y con zoom
    '''
    diccionario = {}

    intensidades = img.flatten()
    lista = intensidades.tolist()

    for elemento in lista:
        clave = elemento
        valor = lista.count(clave)
        diccionario[clave] = valor

    df = pd.DataFrame([[key, diccionario[key]] for key in diccionario.keys()], columns=['Numero', 'Repeticiones'])

    return df