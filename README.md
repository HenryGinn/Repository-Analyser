# Catalogue Analyser

## Contents

1. [Overview](#overview)
1. [Repository Analyser](#repository-analyser)
1. [To Do List](#to-do-list)

## Overview

This program collects statistics and produces infographics about all python projects within a folder. A project counts as the contents of any folder that contains a README document, or any folder with files in it (not including files further down in the folder structure)

It produces a results folder with two sub folders. The first of these contains a file for each statistic tracked, and in each file, only the statistics for the whole repository will be shown. The second folder will have the results for each of each repository in detail, and these will be organised within the same folder structure as the original catalogue.

## Repository Analyser

The statistics are organised into groups. Each group is implemented by writing a class for that group, and adding the class to a list in the Files class, and it needs to produce a list of statistic objects from the contents of a file.

- LineCount. This gives the total number of lines, the number of blank lines, and the number of non-blank lines
- MethodLength. This gives the percentage of the methods and functions in each file that are of lengths 1, 2, ..., n+.
- IndentationLevel. This gives the percentage of non blank lines in a file that have an indentation level of 1, 2, ..., n+.

## To Do List

