# Pokemon RPG - Build Guide

## Project Overview
Pokemon RPG is a Pygame-based RPG game featuring Pokemon battles, exploration, and evolution mechanics. This guide explains how to build the project for Windows.

## Dependencies
- Python 3.11+
- pygame 2.5.2
- pytmx 3.32.5
- PyInstaller 6.1.0 (for building)

## Local Build Instructions

### Prerequisites
1. Install Python 3.11 or later from [python.org](https://www.python.org/)
2. Clone this repository

### Setup
```bash
# Navigate to project directory
cd pokemonrpg

# Install dependencies
pip install -r requirements.txt
```

### Running the Game
```bash
cd code
python main.py
```

### Building Windows Executable Locally
```bash
# Using the spec file (recommended)
pyinstaller PokemonRPG.spec

# Or using command line
pyinstaller --onefile --windowed --name="PokemonRPG" \
  --add-data "data:data" \
  --add-data "graphics:graphics" \
  --add-data "audio:audio" \
  code/main.py
```

The executable will be created in the `dist/` folder.

## Automated Builds with GitHub Actions

This project uses GitHub Actions to automatically build Windows executables on every push and pull request.

### Features
- **Automated Builds**: Windows executable is built automatically on push to master/production branches
- **Artifacts**: Built executable is uploaded as a build artifact for download
- **Release Integration**: Tags are automatically built and released

### Workflow Details
The `.github/workflows/build-windows.yml` workflow:
1. Triggers on pushes to master/production branches and pull requests
2. Sets up Python 3.11 on a Windows environment
3. Installs all dependencies from requirements.txt
4. Builds an executable using PyInstaller
5. Uploads the executable as an artifact
6. (Optional) Creates a GitHub release if a tag is pushed

### Accessing Built Artifacts
1. Go to the Actions tab in your GitHub repository
2. Click on the latest build workflow
3. Scroll down to the Artifacts section
4. Download the "PokemonRPG-Windows" artifact

### Creating a Release
To create a release with the Windows executable:
```bash
git tag v1.0.0
git push origin v1.0.0
```

This will automatically trigger a build and create a GitHub release with the executable attached.

## Project Structure
```
pokemonrpg/
├── code/                 # Game source code
│   ├── main.py          # Entry point
│   ├── battle.py        # Battle mechanics
│   ├── entities.py      # Player/NPC entities
│   ├── monster.py       # Monster class
│   └── ...
├── data/                # Game data
│   ├── maps/            # Tiled map files (.tmx)
│   └── tilesets/        # Tileset definitions
├── graphics/            # Game assets
│   ├── monsters/        # Monster sprites
│   ├── characters/      # Character sprites
│   ├── ui/              # UI elements
│   └── ...
├── audio/               # Sound and music files
├── requirements.txt     # Python dependencies
├── PokemonRPG.spec      # PyInstaller configuration
└── .github/workflows/   # GitHub Actions workflows
```

## Troubleshooting

### Build fails with missing assets
Ensure the `data`, `graphics`, and `audio` directories are included in the `--add-data` parameters in the workflow or spec file.

### PyInstaller icon issue
If the icon path is invalid, remove the `--icon` parameter from the build command.

### Game doesn't run after build
- Ensure all dependencies are listed in requirements.txt
- Check that file paths use relative paths (not absolute)
- Verify all game assets are included in the `--add-data` parameters

## Development
For development, run the game directly:
```bash
cd code
python main.py
```

No build required during development - just modify and reload!
