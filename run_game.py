#!/usr/bin/env python3
"""
PokemonRPG - Desktop entry point (used by PyInstaller)
"""

import sys
import os
import asyncio
from os.path import join, dirname, abspath

# Detect if running as a PyInstaller bundle
if getattr(sys, 'frozen', False):
    WORKSPACE_ROOT = sys._MEIPASS
else:
    WORKSPACE_ROOT = dirname(abspath(__file__))

CODE_DIR = join(WORKSPACE_ROOT, 'code')
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

# Change working directory to workspace root for asset loading
os.chdir(WORKSPACE_ROOT)

# Now import and run the game
from game import Game

game = Game()
asyncio.run(game.run())
