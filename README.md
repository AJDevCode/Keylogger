# Keylogger


## Description
The Keylogger is a Python program that utilizes the Pynput library to extract information from user key inputs when active. The program then stores the data in a text file locally. This only works locally on the machine and does not send or receive data from other machines. 

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)


## Prerequisites
Before you begin, ensure you have the following requirements:

- **Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

- **Pynput Library**: Install the Pynput library using the following command:
  ```bash
  pip install Pynput
  ```
## Installation
Follow these steps to set up the Keylogger program:

### Step 1: Clone the Repository
``` bash
git clone https://github.com/AJDevCode/Keylogger.git
```
### Step 2: Install Dependencies
``` bash
py -m pip install pynput
```
## Usage
To run the Keylogger program, execute the following command:
```bash
python Keylogger.py
```
Clicking keys captures the user's input and stores it in a text file. To use this file for testing purposes, you must exclude this from your Windows Defender. This only works locally on the machine and does not send or receive data from other machines. 

## Features
The Keylogger program offers the following key features:

- Utilizes the Pynput library for keyboard detection.

- Captures all keys entered by the user.

- Outputs results to the terminal and saves them in a text file.

## Technologies Used
- Python

- Pynput Library
