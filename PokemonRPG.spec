# -*- mode: python ; coding: utf-8 -*-
#
# PyInstaller spec file for Pokemon RPG
# This file controls how PyInstaller builds the Windows executable
from PyInstaller.utils.hooks import collect_submodules, collect_all
import os

# Anchor all paths to the spec file's directory
SPEC_DIR = os.path.dirname(os.path.abspath(SPECPATH if 'SPECPATH' in dir() else __file__))
CODE_DIR = os.path.join(SPEC_DIR, 'code')

a = Analysis(
    [os.path.join(SPEC_DIR, 'run_game.py')],
    pathex=[CODE_DIR, SPEC_DIR],
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
