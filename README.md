# Wallpaper Engine for Ubuntu

A simple Python script to automatically change your desktop wallpaper on Ubuntu at regular intervals using images from a specified directory.

## Features
- Automatically selects a random image from a specified folder
- Changes the wallpaper at a user-defined interval (in minutes)
- Supports PNG, JPG, GIF, and JPEG image formats

## Prerequisites
Make sure you have the following installed on your Ubuntu system:

- Python 3
- `gsettings` (comes pre-installed with GNOME desktop environments)
- `schedule` Python package

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/Wallpaper-Engine-for-Ubuntu.git
   cd Wallpaper-Engine-for-Ubuntu
   ```

2. Install dependencies:
   ```sh
   pip install schedule
   ```

## Usage

1. Open the script file and modify the `path` variable to point to your image directory:
   ```python
   path = "your/file/path"  # Change this to the absolute path of your images
   ```

2. Set the wallpaper change interval by modifying `time_to_change`:
   ```python
   time_to_change = 1  # Replace 1 with the number of minutes or keep it one minutes your choice
   ```

3. Run the script:
   ```sh
   python3 wallpaper_engine.py
   ```

## How It Works
- The script scans the specified directory for images.
- It randomly selects an image and sets it as the wallpaper using `gsettings`.
- The process repeats every `time_to_change` minutes using the `schedule` module.

## Running on Startup
To ensure the script runs on startup, you can add it to your startup applications:

1. Open **Startup Applications** in Ubuntu.
2. Click **Add** and enter the following details:
   - **Name**: Wallpaper Engine
   - **Command**: `/usr/bin/python3 /path/to/wallpaper_engine.py`
   - **Comment**: Automatically change wallpaper
3. Save and restart your computer to verify it runs at startup.

## Contributing
Feel free to contribute by submitting issues or pull requests!




