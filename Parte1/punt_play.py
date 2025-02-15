class punt_play:
    def __init__(self, game_id, teams, yards, quarter):
        self.game_id = game_id
        self.teams = teams
        self.yards = yards
        self.quarter = quarter

    def __eq__(self, other):
        """
        Implements equality comparison
        Returns True if yards are equal, False otherwise
        """
        if not isinstance(other, punt_play):
            return NotImplemented
        return self.yards == other.yards

    def __lt__(self, other):
        """
        Implements less than comparison
        Returns True if self.yards < other.yards
        """
        if not isinstance(other, punt_play):
            return NotImplemented
        return self.yards < other.yards

    def __gt__(self, other):
        """
        Implements greater than comparison
        Returns True if self.yards > other.yards
        """
        if not isinstance(other, punt_play):
            return NotImplemented
        return self.yards > other.yards

    def __le__(self, other):
        """
        Implements less than or equal comparison
        """
        if not isinstance(other, punt_play):
            return NotImplemented
        return self.yards <= other.yards

    def __ge__(self, other):
        """
        Implements greater than or equal comparison
        """
        if not isinstance(other, punt_play):
            return NotImplemented
        return self.yards >= other.yards