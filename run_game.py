#!/usr/bin/env python3
"""
PokemonRPG - Main entry point
This script can be run from the workspace root directory to start the game.
"""

import sys
import os
from os.path import join, dirname, abspath

# Get the workspace root directory
WORKSPACE_ROOT = dirname(abspath(__file__))
CODE_DIR = join(WORKSPACE_ROOT, 'code')

# Add the code directory to the Python path
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

# Change working directory to workspace root for asset loading
os.chdir(WORKSPACE_ROOT)

# Now import and run the game
try:
    from main import Game
    
    game = Game()
    game.run()
except ImportError as e:
    print(f"Import Error: {e}")
    print(f"Workspace Root: {WORKSPACE_ROOT}")
    print(f"Code Dir: {CODE_DIR}")
    print(f"Python Path: {sys.path}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
