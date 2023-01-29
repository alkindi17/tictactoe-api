## Tic-Tac-Toe API

# Introduction
This API allows you to play Tic-Tac-Toe. You and someone can play together, or you can play against a computer, either against one that uses random algorithm, or a computer that is impossible to win against which uses the minimax algorithm.

I implemented this API on a react WebApp, try it out [here](https://alkindi17.github.io/tictactoe/) or visit the [github page](https://github.com/alkindi17/tictactoe).

# Overview
There are 3 types of requests:
1) Create Session
POST - http://alkindi.pythonanywhere.com/session
2) Get Session Details
GET - http://alkindi.pythonanywhere.com/session
3) Play; make a move
POST - http://alkindi.pythonanywhere.com/session/play

# Documentation
API Documentation is available at: https://documenter.getpostman.com/view/25468658/2s8ZDeSy5r

# Status Codes
- Status 200: Success.
- Status 400: Something wrong with your request.
- Status 500: Something wrong with the server.

# Built With
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)

# Author
[**Ali Al Kindi**](https://github.com/alkindi17)
