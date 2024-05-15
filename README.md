# Image scanner - Standalone

An image editing app written in Python using OpenCV.<br>
Description: an improvement of my [Image scanner](https://github.com/ElenaChes/Python-Image-scanner), a standalone app that takes an photo of a paper, and outputs an edited image with the paper properly aligned as though it was scanned.

<details>
  <summary><h3>Content</h3></summary>

- [Dependencies](#dependencies)
- [Installation](#installation)
  - [Using the executable](#using-the-executable)
  - [Running the raw code](#running-the-raw-code)
  - [Creating an executable from the code](#creating-an-executable-from-the-code)
- [Usage](#usage)

</details>
<hr>

# Dependencies

1. Python 3.7.0

The app could work with different versions, but this is the one that was tested.

# Installation

## Using the executable

1. Download the folder `Image Scanner`.

> [!TIP]
> Create a shortcut for `Image Scanner/Image Scanner.exe` outside the folder to easily access the app.

## Running the raw code

1. Create a new directory, for example `scanner`, and place `imageScanner.py` and `scanner.ico` inside of it.
2. Open the directory in your Terminal:

```
cd scanner
```

3. Create a virtual environment:

```
python -m venv opencv-env
```

4. Activate the environment :

```
.\opencv-env\Scripts\activate
```

5. Install needed packages:

```
pip install opencv-contrib-python matplotlib
```

## Creating an executable from the code

To create `Image Scanner/Image Scanner.exe` the following command was used:

```
pyinstaller --onedir --icon=scanner.ico --add-data="scanner.ico;." --windowed --name="Image Scanner" imageScanner.py
```

> While `scanner.ico` is the icon used for the app.

If you don't want to use an icon you can remove the following line from `imageScanner.py`:

```
root.iconbitmap("scanner.ico")
```

And create an executable using:

```
pyinstaller --onedir --windowed --name="Image Scanner" imageScanner.py
```

# Usage

1. Run `Image Scanner/Image Scanner.exe` (or `imageScanner.py`).
2. Choose an image to edit.
3. Choose a location to export the new image to and name it.

> [!NOTE]
> Common causes for failing to process the image:
> - The paper isn't visible in its entirety in the input image.
> - The paper and the background color aren't distinct enough in the input image.
