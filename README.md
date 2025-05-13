# Mood-Based Playlist Recommender

## Overview
This is a Python application that recommends a song based on your mood and preferred language. The user enters a mood, and the app will detect the mood based on the input text and recommend a song in the selected language (English, Spanish, French, Tamil, Hindi, or Malayalam). It also provides an attractive, user-friendly graphical interface built with `Tkinter`.

## Features
- **Mood Detection**: Uses TextBlob to analyze the input text and classify the mood as happy, sad, or relaxed.
- **Multi-language Support**: Provides songs in multiple languages (English, Spanish, French, Tamil, Hindi, Malayalam).
- **Graphical User Interface (GUI)**: Built with Tkinter, the interface is stylish and user-friendly with a pastel theme.
- **Custom Font**: Uses the "Lobster" font for a sleek and modern look.
- **Random Song Recommendation**: The app recommends a song randomly from a predefined list based on the detected mood and selected language.

## Requirements
- Python 3.x
- `Tkinter` library (usually comes pre-installed with Python)
- `textblob` library

### Install Dependencies
To install the required dependencies, run the following command:

```bash
pip install textblob
