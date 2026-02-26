"""
PokemonRPG - Web entry point (used by pygbag)
"""

import asyncio
import sys
import os
from os.path import join, dirname, abspath

# Add code directory to path
ROOT = dirname(abspath(__file__))
CODE_DIR = join(ROOT, 'code')
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

os.chdir(ROOT)

from game import Game

async def main():
    game = Game()
    await game.run()

asyncio.run(main())
