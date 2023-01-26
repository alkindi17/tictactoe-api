## Tic-Tac-Toe API

# Introduction
This API allows you to play Tic-Tac-Toe. You and someone can play together (not online multiplayer, unless you want to use the power of the API to make it online (; ). You can also play against a computer, either against a computer that uses random algorithm, or a computer that uses MiniMax algorithm, which you can't win against.

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

# Authentication
No authentication needed, you just have to store the session ID for the session duration, because you will need it to send requests to the API, to get the session details, and to play in the session.

# Error Codes
- Status 200: Most probably, everything is OK.
- Status 400: Most probably, the request has something wrong.
- Status 500: Most probably, error in the server.

# Built With
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)

# Author
[**Ali Al Kindi**](https://github.com/alkindi17)
