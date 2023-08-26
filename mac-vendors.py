#!/python33/python
from mac_vendor_lookup import MacLookup
import PySimpleGUI as sg
import re

#dependencias
#python3 -m pip install PySimpleGUI
#python3 -m pip install mac_vendor_lookup


def is_valid(str):
#regural expression
  regex = ("^([0-9A-Fa-f]{2}[:-])" +"{5}([0-9A-Fa-f]{2})|" +"([0-9a-fA-F]{4}\\." +"[0-9a-fA-F]{4}\\." +"[0-9a-fA-F]{4})$")
  match = re.compile(regex)
  if (str == None):
    return False
  if(re.search(match, str)):
    return True
  else:
    return False


layout = [
    [sg.Text("Consultar MAC Address")],
    [sg.InputText(key="mac_addr")],
    [sg.Button("Consultar"), sg.Button("Cancelar")],
    [sg.Text("",key="Vendor")],
    [sg.Text("Felipe Lira")],

    ]

janela = sg.Window("Consulta de Endereço MAC", layout)


while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        exit(0)
    if evento == "Consultar":
        mac_addr = valores["mac_addr"]
        mac_addr = mac_addr.upper()
        mac_addr = mac_addr.replace(' ',':').replace('-',':')

        if(is_valid(mac_addr)):
            try:
                vendor = MacLookup().lookup(mac_addr)
                janela["Vendor"].update(f"Vendor: {vendor}")

            except:
                janela["Vendor"].update("ERRO AO CONSULTAR")                
        else:
            print("Erro")
            janela["Vendor"].update("FORMATO INVALIDO")



janela.close()
