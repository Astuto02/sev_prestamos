# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\backend.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\banco.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\bd_prestamos.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\caja.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\clientes.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\cobros.xlsx', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\estado_cuotas.xlsx', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\estilos.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\flotante.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\funcionalidad.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\imagen_recuperada.png', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\index.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\ingresos.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\ingresos.xlsx', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\main.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\main.spec', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\movimientos.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\operando.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\otras_operaciones.xlsx', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\otros.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\prestamo.xlsx', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\prestamo_consulta.xlsx', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\prestamos_bd.db', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\pruebas.py', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\users.db', '.'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\img', 'img/'), ('C:\\Users\\Astut\\Desktop\\project\\sev_prestamo', 'sev_prestamo/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Astut\\Desktop\\project\\sev_prestamo\\img\\micro-bank.ico'],
)
