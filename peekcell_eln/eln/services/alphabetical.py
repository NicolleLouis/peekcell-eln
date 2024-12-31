class AlphabeticalService:
    @staticmethod
    def int_to_capital_letter(i: int) -> str:
        character_number = i%26 + 65
        return chr(character_number)
