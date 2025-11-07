# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[
        ('C:/Program Files/STMicroelectronics/STM32Cube/STM32CubeProgrammer/bin/CubeProgrammer_API.dll', '.'),
        ('C:/api-ms-win-core-path-l1-1-0.dll', '.'),
        ('C:/Users/BlufushkaPC/AppData/Local/Programs/Python/Python39/python39.dll', '.'),
        ('CubeProgrammer_API.dll', '.'),
        ('python39.dll', '.'),
        ('AksonTerminal.exe', '.'),
    ],
    datas=[
        ('board1_window.py', '.'),
        ('board2_window.py', '.'),
        ('board3_window.py', '.'),
        ('board4_window.py', '.'),
        ('ai_sid.txt', '.'),
        ('ai_sid_dicts.txt', '.'),
        ('ai_mid.txt', '.'),
        ('ai_mid_dicts.txt', '.'),
        ('di_sid.txt', '.'),
        ('di_sid_dicts.txt', '.'),
        ('di_mid.txt', '.'),
        ('di_mid_dicts.txt', '.'),
        ('dicts_log.txt', '.'),
        ('terminal.py', '.'),
        ('terminal2.py', '.'),
        ('AksonIMG.png', '.'),
        ('AksonICON.ico', '.'),
        ('app.manifest', '.'),
    ],
    hiddenimports=['tabulate'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='Конфигуратор АКСОН build_0.1.4',
    manifest='app.manifest',
    debug=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=False,
    onefile=True,
    icon='AksonICON.ico'
)
