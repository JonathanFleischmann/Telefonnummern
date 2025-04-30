class Core:

    def remove_prefix_until(self, string: str, prefix: str) -> str:
        """
        Remove the beginning of the string until the first occurrence of the prefix.
        """
        index = string.find(prefix)
        if index == -1:
            raise ValueError(f"Prefix '{prefix}' not found in string.")
        return string[index + len(prefix):]
    
    def clean_from_special_characters(self, string: str) -> str:
        """
        Remove special characters from the string.
        """
        return string.replace(' ', '').replace('/', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '')