from chess.views.deletetournaments import DeleteTournament
from chess.models.tournaments import Tournament


"""
Test
"""


class DeleteTournamentC:
    def __init__(self, data):
        self.data = data

    def call(self):
        deletetournament_view = DeleteTournament(self.data)
        choice = deletetournament_view.home()
        # suppression user choice
        Tournament.delete_tournament(choice)
        return "managetournament"
