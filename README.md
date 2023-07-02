# MarkedUp
![Alt text](MarkedUp_Logo.png)

## Introduction
A desktop stock viewer that utilizes the excellent TwelveData API as the data source. It provides all relavent information for over 20,000 stocks with a clean, easy to use user interface:

![Alt text](dark_mode.png)

## Goals
The goal was to create a great looking stock viewer that utilized a reputable API as it's source. It was a great way for me to improve my skills with common Python tools such as `pandas`, `plotly`, and `PyQt5`.

## External Libraries
The following python libraries are used in this project:

<div align="center">

| Library        | Used For                                                            |
| -------------- | ------------------------------------------------------------------- |
| `pandas`       | Managing stock data retrieved from the TwelveData API               |
| `PyQt5`        | Creating the entire user interface.                                 |
| `plotly`       | Graphing the interactive candlestick chart.                         |
| `twelvedata`   | Getting stock data to display.                                      |
| `os`           | Checking file system paths and files in the application directory.  |
| `json`         | Creating and managing json files.                                   |
| `sys`          | Interacting with operating system for desktop application creation. |
| `datetime`     | Create and manage dates and times.                                  |
| `relativedata` | Calculate dates relative to the given date.                         |
| `threading`    | Run functions on multiple threads (multithreading).                 |
| `qdarkstyle`   | Styling user interface with KDE-like Breeze colour themes.          |

</div>

## Code Files
The program source code has been broken down into 3 files. Admittedly, I should probably split the `gui.py` file into seperate files because it is too large (600+ lines):

<div align="center">

| File            | Contains Code For                                             |
| --------------- | ------------------------------------------------------------- |
| `gui.py`        | Creating the user interface.                                  |
| `connection.py` | Connecting and analyzing the data from the TwelveData API     |
| `main.py`       | Cleaning up temporary files and then starting the application |

</div>

## Initial Setup
Upon startup for the first time, the program will create the following files:

<div align="center">

| File                    | Contains                                                                                                  |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| `all_stocks.json`       | Stock Identification Information for all stocks from TwelveData API. Used for autocomplete functionality. |
| `saved_favourites.json` | Favourite Stocks Information. Originally starts off empty.                                                |

</div>

The `all_stocks.json` file in particular causes the first time launch of the application to take longer than consecutive launches, because it is loading a file with around over 100,000 lines!

## Features
I designed MarkedUp to have all the possible features I would want in a stock viewer, and such that anyone could easily use it to view data.

### Data Table

### Plotly Candlestick Chart

### Favourites List

### Stock Search Autocomplete

### Multithreading

### User Interface

### Light Mode

![Alt text](light_mode.png)

## Features to Implement in the Future