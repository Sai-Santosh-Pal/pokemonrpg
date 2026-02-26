# -*- mode: python ; coding: utf-8 -*-
#
# PyInstaller spec file for Pokemon RPG
# This file controls how PyInstaller builds the Windows executable
from PyInstaller.utils.hooks import collect_submodules, collect_all
import os

a = Analysis(
    ['run_game.py'],
    pathex=[os.path.abspath('code')],
    binaries=[],
    datas=[
        ('data', 'data'),
        ('graphics', 'graphics'),
        ('audio', 'audio'),
    ],
    hiddenimports=[
        'pygame',
        'pytmx',
        'pytmx.util_pygame',
        'main',
        'settings',
        'game_data',
        'sprites',
        'entities',
        'groups',
        'dialog',
        'monster_index',
        'battle',
        'timer',
        'evolution',
        'support',
        'monster',
        'debug',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=['pkg_resources', 'setuptools'],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PokemonRPG',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PokemonRPG',
)
