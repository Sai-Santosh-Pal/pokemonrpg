# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules, collect_data_files
from PyInstaller.utils.hooks import collect_all
import sys
import os

# Anchor all paths to the spec file's directory
SPEC_DIR = os.path.dirname(os.path.abspath(SPECPATH if 'SPECPATH' in dir() else __file__))
CODE_DIR = os.path.join(SPEC_DIR, 'code')

# Collect all submodules and dependencies
datas = [
    ('audio', 'audio'),
    ('graphics', 'graphics'),
    ('data', 'data'),
]
binaries = []
hiddenimports = [
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
]

# Collect pygame and pytmx
tmp_ret = collect_all('pygame')
datas += tmp_ret[0]
binaries += tmp_ret[1]
hiddenimports += tmp_ret[2]

tmp_ret = collect_all('pytmx')
datas += tmp_ret[0]
binaries += tmp_ret[1]
hiddenimports += tmp_ret[2]

a = Analysis(
    [os.path.join(SPEC_DIR, 'run_game.py')],
    pathex=[CODE_DIR, SPEC_DIR],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'numpy', 'scipy', 'pkg_resources', 'setuptools'],
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
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
