# Image Scanner - Standalone

<p>
  <img src="https://img.shields.io/badge/Python-grey?logo=python">
  <img src="https://img.shields.io/badge/OpenCV-grey?logo=opencv">
</p>

<img align="right" style="width:200px; height:auto;" src="/scanner.ico">

An image "scanning" app written in Python using OpenCV.<br>
An improved version of my [Image scanner](https://github.com/ElenaChes/Python-Image-scanner), a standalone app that takes a photo of a paper and outputs an edited image with the paper properly aligned as though it was scanned.

<details>
  <summary><h3>Content</h3></summary>

- [Dependencies](#dependencies)
- [Installation](#installation)
  - [Using the Executable](#using-the-executable)
  - [Running the Raw Code](#running-the-raw-code)
  - [Creating an Executable from the Code](#creating-an-executable-from-the-code)
- [Usage](#usage)

</details>
<hr>

<p align="center">
<img style="width:600px; height:auto;" src="https://github.com/ElenaChes/Python-Image-scanner-Standalone/assets/54331769/b9f7e9f6-048d-4d6c-93f9-91b4c0a0ff9f"><br>
<sub>image.jpg ⇨ image_scanned.png</sub>
</p>

# Dependencies

1. Python 3.7.0

The app may work with other versions, but this is the version that was used during development.

# Installation

## Using the Executable

1. Download `Image Scanner.zip` and extract its contents into a folder.

> [!TIP]
> Create a shortcut for `Image Scanner/Image Scanner.exe` outside the folder for easier access.

## Running the Raw code

1. Create a new directory, for example `scanner`, and place `imageScanner.py` and `scanner.ico` inside of it.
2. Open the directory in your terminal:

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

5. Install required packages:

```
pip install opencv-contrib-python matplotlib
```

## Creating an Executable from the Code

To create `Image Scanner/Image Scanner.exe`, use the following command:

```
pyinstaller --onedir --icon=scanner.ico --add-data="scanner.ico;." --windowed --name="Image Scanner" imageScanner.py
```

> [!NOTE]
> The `scanner.ico` is the icon used for the app.<br>
> If you don't want to use an icon you can remove the following line from `imageScanner.py`:
>
> ```python
> root.iconbitmap("scanner.ico")
> ```
>
> And create an executable using:
>
> ```
> pyinstaller --onedir --windowed --name="Image Scanner" imageScanner.py
> ```

# Usage

1. Run `Image Scanner/Image Scanner.exe` (or `imageScanner.py`).
2. Choose an image to edit.
3. Choose a location to export the new image to and name it.

> [!NOTE]
> Common causes for failing to process the image:
>
> - The paper isn't visible in its entirety in the input image.
> - The paper and the background colors aren't distinct enough.
