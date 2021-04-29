# Google Search Automation Project

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [How to Run](#run)

<a name="introduction"></a>
## Introduction

This project contains UI testing framework to verify Google Search functionality.

<a name="getting-started"></a>
## Getting Started

### Prerequisite
- Gitbash

### Requirements
- Python 3.9
  
Libraries:
- Selenium 
- Pytest
- Pytest-html
- IDE (recommended Pycharm)

<a name="run"></a>
## How to Run

You can run the test cases from the IDE or from a cmd console using the following commands:

_pytest TestCases/[testfile.py]_

[testfile.py] = indicate the file which contains tests

Also you can run the test cases with the generation of a report with results using the following command:

_pytest --html=Reports/report.html TestCases/[testfile.py]_
