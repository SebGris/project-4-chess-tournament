class IDGenerator:
    """Generates unique numeric IDs."""
    current_id = 0

    @classmethod
    def get_next_id(cls):
        cls.current_id += 1
        return cls.current_id
