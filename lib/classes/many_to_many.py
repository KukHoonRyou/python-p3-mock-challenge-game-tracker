class Game:
    
    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, "title") and len(title) > 0: # and not hasattr(self, "title") ??
           self._title = title
        else:
            raise Exception ("Invalid title value.") #string is immutable
        
    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        scores = [result.score for result in player.results() if result.game is self]
        if scores:
            return sum(scores) / len(scores)
        else:
            return 0
class Player:

    all = []

    def __init__(self, username):
        self.username = username
        type(self).all.append(self)

    @property
    def username (self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception ("Invalid username value")

    def results(self):
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        games_played = [result.game for result in self.results()]
        return games_played.count(game)
    
    @classmethod
    def highest_scored(cls, game):
        highest_score = 0 #set initial value
        highest_scoring_player = None # set initial value

        for player in cls.all:
            average_score = game.average_score(player)

            if average_score > highest_score:
                highest_score = average_score
                highest_scoring_player = player
        
        return highest_scoring_player


class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    @property
    def score (self):
        return self._score
    
    @score.setter
    def score (self, score):
        if isinstance(score, int) and not hasattr(self, "score") and 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception("Score must be an integer within 1 to 5000.")
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance (player, Player):
            self._player = player
        else:
            raise Exception("Invalid player value")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance (game, Game):
            self._game = game
        else:
            raise Exception("Invalid game value")
        
    
        