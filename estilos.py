import os

def obtener_estilos():
    img_minus = os.path.join('img/minus.png')
    imprimir = os.path.join('img/printer.png')
    salir = os.path.join('img/logout.png')
    banca = os.path.join('img/bank.png')
    movimientos = os.path.join('img/money_review.png')
    otorgados = os.path.join('img/transaction-success.png')
    disponibles = os.path.join('img/finanzas.png')
    depositos = os.path.join('img/cash.png')
    retiros = os.path.join('img/retiro_cash.png')
    capital = os.path.join('img/investment.png')
    intereses = os.path.join('img/interest-rate.png')
    recargos = os.path.join('img/recargos.png')
    ingreso = os.path.join('img/ingreso.png')
    caja = os.path.join('img/cash-machine.png')
    clientes = os.path.join('img/handshake.png')
    prestamo = os.path.join('img/transfer.png')
    img_update = os.path.join('img/update.png')
    img_save = os.path.join('img/diskette.png')
    img_delete = os.path.join('img/delete.png')
    ojo = os.path.join('img/eye.png')
    volver = os.path.join('img/volver.png')
    img_user = os.path.join('img/profile.png')
    permisos = os.path.join('img/padlock.png')
    backup = os.path.join('img/folder.png')
    ajustes = os.path.join('img/settings.png')
    img_publi = os.path.join('img/micro-bank.png')


    estilos = f'''
    *{{
        margin:0px;
    }}

    QTableWidget::item{{
      background-color:rgb(100,200,216);
    }}
    QTableWidget::item:alternate{{
      background-color:#d2e4f2;
    }}
    QTableWidget::item:selected{{
      background-color:rgb(167,216,216);
    }}

    #titulo_principal{{
      font-size:28px;
      font-weight: bold;
      color:rgb(9,123,2);
      text-align:center;
    }}

    #btn_banca{{
      border:none;
      margin:0px 40px;
      width: 64px;
      height:64px;
      background-image: url('{banca}');
      background-position: top center;
      background-repeat: no-repeat;
      font-weight: bold;
      font-size:15px;
      color:green;
      padding-bottom: 5px;
      text-align: bottom;
      padding-top:20px;
    }}
    #btn_movi{{
      border:none;
      margin:0px 40px;
      width: 64px;
      height:64px;
      background-image: url('{movimientos}');
      background-position: top center;
      background-repeat: no-repeat;
      font-weight: bold;
      font-size:15px;
      color:green;
      padding-bottom: 5px;
      text-align: bottom;
      padding-top:20px;
    }}
    #btn_ingresos{{
      border:none;
      margin:0px 40px;
      width: 64px;
      height:64px;
      background-image: url('{ingreso}');
      background-position: top center;
      background-repeat: no-repeat;
      font-weight: bold;
      font-size:15px;
      color:green;
      padding-bottom: 5px;
      text-align: bottom;
      padding-top:20px;
    }}
    #btn_caja{{
      border:none;
      margin:0px 40px;
      width: 64px;
      height:64px;
      background-image: url('{caja}');
      background-position: top center;
      background-repeat: no-repeat;
      font-weight: bold;
      font-size:15px;
      color:green;
      padding-bottom: 5px;
      text-align: bottom;
      padding-top:20px;
    }}
    #btn_clientes{{
      border:none;
      margin:0px 40px;
      width: 64px;
      height:64px;
      background-image: url('{clientes}');
      background-position: top center;
      background-repeat: no-repeat;
      font-weight: bold;
      font-size:15px;
      color:green;
      padding-bottom: 5px;
      text-align: bottom;
      padding-top:20px;
    }}
    #btn_prestamo{{
      border:none;
      margin:0px 40px;
      width: 64px;
      height:64px;
      background-image: url('{prestamo}');
      background-position: top center;
      background-repeat: no-repeat;
      font-weight: bold;
      font-size:15px;
      color:green;
      padding-bottom: 5px;
      text-align: bottom;
      padding-top:20px;
    }}
    #img_pub{{
      background-image: url('{img_publi}');
      background-repeat: no-repeat;

    }}

    #cerrar_btn_pop{{
        width: 24px;
        height:24px;
        image: url('{salir}');
        border: 1px  solid black;
        border-radius:5px;

     }}
    #salir{{
      margin: 0 25px;
      width: 24px;
      height:32px;
      image: url('{salir}');
      border: 1px solid black;
      border-radius:5px;
     }}

    #user_img{{
      margin-left: 75px;
      width: 64px;
      height:64px;
      image: url('{img_user}');
      border:none;
     }}
    #users{{
      margin: 0 25px;
      width: 24px;
      height:32px;
      image: url('{img_user}');
      border: 1px solid black;
      border-radius:5px;
     }}
    #permisos{{
      margin: 0 25px;
      width: 24px;
      height:32px;
      image: url('{permisos}');
      border: 1px solid black;
      border-radius:5px;
     }}
    #backup{{
      margin: 0 25px;
      width: 24px;
      height:32px;
      image: url('{backup}');
      border: 1px solid black;
      border-radius:5px;
     }}
    #config{{
      margin: 0 25px;
      width: 24px;
      height:32px;
      image: url('{ajustes}');
      border: 1px solid black;
      border-radius:5px;
     }}

    #bottom{{
      border-top:2px solid rgb(123,96,100)
    }}

     
    QDialog{{
        background-color: rgb(167,216,216);
        border-radius:16px;
        border-top:1px solid black;
        
        
    }}
    #entradas{{
        background-color: rgb(100,200,216);
        border-radius:16px;
        border:1px solid black;
        
      }}

    #imprimir{{
      width: 32px;
      height:32px;
      image:url('{imprimir}');
      border: 1px solid rgb(100,200,216);
      border-radius:12px;
    }}

    #titulo_flotante{{
        color:rgb(53,146,39);
        font-size:30px;
        font-weight:bold;
     }}

    #btn_capital{{
        padding: 10px 5px;
        font-weight: bold;
        border: 1px solid black;
        border-radius:5px;
    }}

    #otorgados{{
      height: 16px;
      background-image: url('{otorgados}');
      background-position: left;
      background-repeat: no-repeat;
      text-align: right;
      padding-left:30px;
    }}

    #disponibles{{
      height: 16px;
      background-image: url('{disponibles}');
      background-position: left;
      background-repeat: no-repeat;
      text-align: right;
      padding-left:30px;
    }}

    #depositos{{
      height: 16px;
      background-image: url('{depositos}');
      background-position: left;
      background-repeat: no-repeat;
      text-align: right;
      padding-left:30px;
    }}

    #retiros{{
      height: 16px;
      background-image: url('{retiros}');
      background-position: left;
      background-repeat: no-repeat;
      text-align: right;
      padding-left:30px;
    }}
    #capital_rec{{
      height: 16px;
      background-image: url('{capital}');
      background-position: left;
      background-repeat: no-repeat;
      text-align: right;
      padding-left:30px;
    }}
    #intereses{{
      height: 16px;
      background-image: url('{intereses}');
      background-position: left;
      background-repeat: no-repeat;
      text-align: right;
      padding-left:30px;
    }}
    #recargos{{
      height: 16px;
      background-image: url('{recargos}');
      background-position: left;
      background-repeat: no-repeat;
      text-align: right;
      padding-left:30px;
    }}

    #nuevo_prestamo{{
        background: rgb(19,204,33);
        border-radius: 5px;
        padding: 2px 5px;
        margin:5px;
        font-weight:bold;

    }}
    QPushButton#otros{{
      padding:3px;
      border: 1px solid rgb(100,200,216);
      background-color:rgb(167,216,216);
      font-weight:bold;
      border-top-left-radius: 10px;
      border-bottom-right-radius: 10px;

    }}

    #presta_consultar{{
        background: rgb(49,40,215);
        border-radius: 5px;
        padding: 2px 5px;
        margin:5px;
        font-weight:bold;

    }}

    QLineEdit#especiales{{
      border:none;
      background-color:rgb(167,216,216);
    }}
    QComboBox{{
      border:none;
      background-color:rgb(167,216,216);
    }}

    #orden{{
        color:red;
        font-size:bold;
        font-weight:14px;
    }}

    #buscar_client{{
      height:50px;
      width:50px;
    }}

    #derecha_ref{{
      border: 1px solid black;
    }}

    #upd_tabla{{
      width:32px;
      height:32px;
      image:url({img_update})
    }}

    #save_prest{{
      width:32px;
      height:32px;
      image:url({img_save})
    }}
    #volver{{
      width:32px;
      height:32px;
      image:url({volver})
    }}
    #ver_tabla_user{{
      width:32px;
      height:32px;
      image:url({ojo})
    }}

    #refe_op{{
      color:red;
      font-weight:bold;
      font-size:15px;
    }}

    #stack{{
      border: 1px black solid;
    }}

    #usuarios{{
      margin:0px 40px;
      width: 64px;
      height:64px;
      background-image: url('{img_user}');
      background-position: top center;
      background-repeat: no-repeat;
      font-weight: bold;
      border-radius: 25px;
      padding-bottom: 10px;
      text-align: bottom;
      border: 1px solid rgb(0, 0, 0);
      padding-top:5px;
    }}

     #alarma{{
      color:red;
      font-weight:bold;
      font-size:13;
    }}

    #user{{
      border-radius: 5px;
      border: 1px solid rgb(45, 198, 209);
      margin: 0px 20px;
    }}
    #pass{{
      border-radius: 5px;
      border: 1px solid rgb(45, 198, 209);
      color:black;
      margin: 0px 20px;
    }}

    #login{{
    border-radius: 5px;
    border: 1px solid rgb(45, 198, 209);
    margin: 5px 40px;
    padding:10px;
    font-size:15px;
    font-weight:bold;
    }}

    #wid_login{{
      border: 1px solid green;
      border-radius: 15px;
    }}






        '''
    return estilos