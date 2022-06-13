
def img_gray_plot (img):
    diccionario = {}

    intensidades = img.flatten()
    lista = intensidades.tolist()

    for elemento in lista:
        clave = elemento
        valor = lista.count(clave)
        diccionario[clave] = valor

    df = pd.DataFrame([[key, diccionario[key]] for key in diccionario.keys()], columns=['Numero', 'Repeticiones'])
    fig = px.bar(df, x='Numero', y='Repeticiones')

    return fig.show()

def img_rgb_plot (img):
    r = img[:,:,0].flatten()
    g = img[:,:,1].flatten()
    b = img[:,:,2].flatten()

    # Group data together
    hist_data = [r, g, b]

    colors = ['red', 'green', 'blue']
    group_labels = ['Red', 'Green', 'Blue']

    # Create distplot with custom bin_size
    # fig = ff.create_distplot(hist_data, group_labels, bin_size=255, colors=colors)
    fig = ff.create_distplot(hist_data, group_labels, show_hist=True, colors=colors)
    
    return fig.show()