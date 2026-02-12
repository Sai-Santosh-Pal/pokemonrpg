#!/usr/bin/env python3
"""
PokemonRPG Setup Verification Script
Checks that all files, imports, and assets are properly configured
"""

import sys
import os
from os.path import join, exists, isdir, dirname, abspath

def check_directory_structure():
    """Verify all required directories exist"""
    print("\n=== Checking Directory Structure ===")
    workspace_root = dirname(abspath(__file__))
    required_dirs = {
        'code': 'Python source files',
        'graphics': 'Game graphics and sprites',
        'audio': 'Game audio files',
        'data': 'Game map and data files',
        'data/maps': 'Tiled map files',
        'data/tilesets': 'Tileset definitions',
        'graphics/characters': 'Character sprites',
        'graphics/monsters': 'Monster sprites',
        'graphics/fonts': 'Game fonts',
        'graphics/icons': 'UI icons',
        'graphics/ui': 'UI elements',
        'graphics/attacks': 'Attack animations',
        'graphics/backgrounds': 'Battle backgrounds',
        'graphics/objects': 'Object sprites',
        'graphics/tilesets': 'Tileset graphics',
        'graphics/other': 'Other graphics',
    }
    
    all_exist = True
    for dir_name, description in required_dirs.items():
        dir_path = join(workspace_root, dir_name)
        exists_status = "✓" if isdir(dir_path) else "✗"
        print(f"{exists_status} {dir_name:30} - {description}")
        if not isdir(dir_path):
            all_exist = False
    
    return all_exist

def check_python_files():
    """Verify all required Python files exist"""
    print("\n=== Checking Python Files ===")
    workspace_root = dirname(abspath(__file__))
    code_dir = join(workspace_root, 'code')
    
    required_files = [
        'main.py',
        'settings.py',
        'game_data.py',
        'entities.py',
        'sprites.py',
        'groups.py',
        'support.py',
        'battle.py',
        'dialog.py',
        'monster.py',
        'monster_index.py',
        'evolution.py',
        'timer.py',
        'debug.py',
    ]
    
    all_exist = True
    for filename in required_files:
        file_path = join(code_dir, filename)
        exists_status = "✓" if exists(file_path) else "✗"
        print(f"{exists_status} {filename}")
        if not exists(file_path):
            all_exist = False
    
    return all_exist

def check_root_files():
    """Verify entry point files exist"""
    print("\n=== Checking Entry Points ===")
    workspace_root = dirname(abspath(__file__))
    
    required_files = {
        'run_game.py': 'Main entry point (new)',
        'PokemonRPG.spec': 'PyInstaller spec',
        'requirements.txt': 'Python dependencies',
    }
    
    all_exist = True
    for filename, description in required_files.items():
        file_path = join(workspace_root, filename)
        exists_status = "✓" if exists(file_path) else "✗"
        print(f"{exists_status} {filename:30} - {description}")
        if not exists(file_path):
            all_exist = False
    
    return all_exist

def check_imports():
    """Verify Python modules can be imported"""
    print("\n=== Checking Module Imports ===")
    workspace_root = dirname(abspath(__file__))
    code_dir = join(workspace_root, 'code')
    
    # Add code dir to path
    if code_dir not in sys.path:
        sys.path.insert(0, code_dir)
    
    os.chdir(workspace_root)
    
    modules_to_check = [
        'settings',
        'game_data',
        'support',
        'timer',
        'sprites',
        'entities',
        'groups',
        'monster',
        'battle',
        'dialog',
        'monster_index',
        'evolution',
    ]
    
    all_imported = True
    for module_name in modules_to_check:
        try:
            __import__(module_name)
            print(f"✓ {module_name}")
        except ImportError as e:
            print(f"✗ {module_name} - {str(e)}")
            all_imported = False
        except Exception as e:
            print(f"⚠ {module_name} - Warning: {type(e).__name__}: {str(e)}")
    
    return all_imported

def check_requirements():
    """Verify required packages are installed"""
    print("\n=== Checking Python Dependencies ===")
    
    required_packages = {
        'pygame': 'Game engine',
        'pytmx': 'Tiled map loader',
    }
    
    all_installed = True
    for package_name, description in required_packages.items():
        try:
            __import__(package_name)
            print(f"✓ {package_name:20} - {description}")
        except ImportError:
            print(f"✗ {package_name:20} - {description} [NOT INSTALLED]")
            all_installed = False
    
    return all_installed

def main():
    """Run all checks"""
    print("╔════════════════════════════════════════╗")
    print("║  PokemonRPG Setup Verification        ║")
    print("╚════════════════════════════════════════╝")
    
    workspace_root = dirname(abspath(__file__))
    print(f"\nWorkspace: {workspace_root}")
    
    checks = [
        ("Directory Structure", check_directory_structure),
        ("Python Files", check_python_files),
        ("Entry Points", check_root_files),
        ("Python Dependencies", check_requirements),
        ("Module Imports", check_imports),
    ]
    
    results = []
    for check_name, check_func in checks:
        try:
            result = check_func()
            results.append((check_name, result))
        except Exception as e:
            print(f"\n⚠ Error during {check_name} check: {e}")
            results.append((check_name, False))
    
    # Summary
    print("\n" + "═" * 50)
    print("SUMMARY")
    print("═" * 50)
    
    all_passed = True
    for check_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status:8} - {check_name}")
        if not result:
            all_passed = False
    
    print("═" * 50)
    
    if all_passed:
        print("\n✓ All checks passed! You can run the game with:")
        print(f"   python run_game.py")
    else:
        print("\n✗ Some checks failed. Please fix the issues above.")
        print("   Install missing packages with: pip install -r requirements.txt")
    
    return 0 if all_passed else 1

if __name__ == '__main__':
    sys.exit(main())
