# requests,bs4
import requests
from bs4 import BeautifulSoup

def grabarMonedas(monedas):
    """
    convierte una lista de diccionarios en una cada string
    """
    strMonedas = ""
    for l in monedas:
        for clave,valor in l.items():
            strMonedas += valor
            if clave != 'venta':
                strMonedas += ';'
            else:
                strMonedas += '\n'
    return strMonedas

url = requests.get("https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx")
if(url.status_code == 200):
    html = BeautifulSoup(url.text,"html.parser")
    tabla = html.find_all('table',{'id':'ctl00_cphContent_rgTipoCambio_ctl00'})
    #print(tabla)
    lstTipoCambio = []
    for i in range(7):
        filas = html.find_all('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__'+str(i)})
        for fila in filas:
            moneda = fila.find('td',{'class':'APLI_fila3'})
            compra = fila.find('td',{'class':'APLI_fila2'})
            venta = fila.find('td',{'class':'APLI_fila2'}).findNext('td')
            #print(moneda.get_text()," - ",compra.get_text()," - ",venta.get_text())
            dicTipoCambio = {
                'moneda':moneda.get_text(),
                'compra':compra.get_text(),
                'venta':venta.get_text()
            }
            lstTipoCambio.append(dicTipoCambio)
    
    print(lstTipoCambio)
    strMonedas = grabarMonedas(lstTipoCambio)
    fw = open('monedas.csv','w')
    fw.write(strMonedas)
    fw.close()
else:
    print("error al abrir la pagina : " + str(url.status_code))
