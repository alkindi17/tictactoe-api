import uuid
from flask_cors import CORS, cross_origin
from flask import Flask, request
import tictattoe as t
import players as p


app = Flask(__name__)
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

# store sessions using their id as a key
sessions = {}

def startSession(player_x, player_o, start):
    # Create a random id, a new session, asign them to each other
    # in the sessions dictionary
    id = uuid.uuid4().urn[9:]
    sessions.update({ id : t.GameSession(player_x, player_o, start) })

    # if first turn is bot, then let it play here
    session = sessions[id]
    if session.turn.reference != "human":
        session.play_single_turn(session.get_move(session.turn))

    return id


@app.route("/")
# @cross_origin()
def helloWorld():
   return ('<h1>Hello</h1><a href="https://github.com/alkindi17/tictactoe-api">https://github.com/alkindi17/tictactoe-api</a>')


@app.route('/session', methods=['GET', 'POST'])
# @cross_origin(headers=['Content-Type'])
def session():

    if request.method == 'POST':
        
        try:
            # default response in case something went wrong
            status = 500
            response = {
                "errors": [],
            }

            try:
                # get body of the request
                message = request.get_json()
                chosen_player_x = message["player_x"]
                chosen_player_o = message["player_o"]
                start = message["start"].lower()
            except:
                # response with errors if unable to get the body of the request
                status = 400
                response = {
                    "errors": ["Name Fields are probably incorrect, name fields should be 'player_x', 'player_o', and 'start'"]
                }
                return (response, status)

            ## validation 
            if start not in ["x","o"]:
                print(start)
                status = 400
                response["errors"].append("error in getting start, please choose either 'x' or 'o'")

            if chosen_player_x != "human" and chosen_player_o != "human":
                # do not allow both players to be bot
                status = 400
                response["errors"].append("you should choose atleast one player as a 'human'")
                return (response, status)

            # asign Player object as player_x
            if chosen_player_x == "human":
                player_x = p.HumanPlayer("x")
            elif chosen_player_x == "random":
                player_x = p.RandomAI("x")
            elif chosen_player_x == "minimax":
                player_x = p.MiniMaxAI("x")
            else:
                # if not "human" nor "random"
                status = 400
                response["errors"].append("error in getting player_x, please choose either 'human', 'random', or 'minimax'")
            
            # asign Player object as player_o
            if chosen_player_o == "human":
                player_o = p.HumanPlayer("o")
            elif chosen_player_o == "random":
                player_o = p.RandomAI("o")
            elif chosen_player_o == "minimax":
                player_o = p.MiniMaxAI("o")
            else:
                # if not "human" nor "random"
                status = 400
                response["errors"].append("error in getting player_o, please choose either 'human','random', or 'minimax'")
            
            # if no errors, create session and response with status 200
            if status != 400:

                id = startSession(player_x, player_o, start)
                session = sessions[id]

                status = 200
                response = {
                    "id": id,
                    "player_x" : session.player_x.reference,
                    "player_o" : session.player_o.reference,
                    "game_board" : session.board.board,
                    "next_turn" : session.turn.letter,
                    "result" : session.result
                }
            
            return (response, status)
        
        except:
            status = 500
            response = {
                "errors": ["error in server"]
            }
            return (response, status)
        


    if request.method == 'GET':

        try:
            message = request.get_json()
            id = message["id"]

            try:
                session = sessions[id]

            except:
                status = 400
                response = {
                    "errors": ["session id not found"]
                }
                return (response, status)
            
            status = 200
            response = {
                "id": id,
                "player_x" : session.player_x.reference,
                "player_o" : session.player_o.reference,
                "board": session.board.board,
                "next_turn" : session.turn.letter,
                "result" : session.result
            }

            return (response, status)
        
        except:
            status = 500
            response = {
                "errors": ["error in server"]
            }
            return (response, status)



@app.route('/session/play', methods=['POST'])
# @cross_origin(headers=['Content-Type'])
def play():
    if request.method == 'POST':
        # try:
        message = request.get_json()
        id = message["id"]
        chosen_cell = int(message["cell"])

        try:
            session = sessions[id]
        except:
            status = 400
            response = {
                "errors": ["session id not found"]
            }
            return (response, status)
        
        if not session.turn:
            status = 400
            response = {
                "errors": ["game has ended"],
                "player_x" : session.player_x.reference,
                "player_o" : session.player_o.reference,
                "board": session.board.board,
                "next_turn" : session.turn,
                "result" : session.result
            }
            return (response, status)

        if chosen_cell not in session.board.available_cells():
            status = 400
            response = {
                "errors": ["cell is not available, choose another one"],
                "board" : session.board.board
            }
            return (response, status)
        
        session.play_single_turn(chosen_cell)

        if session.result == "":
            if not session.turn.reference == "human":
                session.play_single_turn(session.get_move(session.turn))

        if session.turn:
            next_turn = session.turn.letter
        else:
            next_turn = session.turn

        status = 200
        response = {
            "id": id,
            "player_x" : session.player_x.reference,
            "player_o" : session.player_o.reference,
            "board": session.board.board,
            "next_turn" : next_turn,
            "result" : session.result
        }

        return (response, status)

        # except:
        #     status = 500
        #     response = {
        #         "errors": ["error in server"]
        #     }
        #     return (response, status)





if __name__ == "__main__":
    app.run(debug=True)
