class Core:

    def remove_prefix_until(self, string: str, prefix: str) -> str:
        """
        Remove the beginning of the string until the first occurrence of the prefix.
        """
        index = string.find(prefix)
        if index == -1:
            raise ValueError(f"Prefix '{prefix}' not found in string.")
        return string[index + len(prefix):]
    
    def remove_suffix_until(self, string: str, suffix: str) -> str:
        """
        Remove the end of the string until the last occurrence of the suffix.
        """
        index = string.rfind(suffix)
        if index == -1:
            raise ValueError(f"Suffix '{suffix}' not found in string.")
        return string[:index]

    
    def clean_from_special_characters(self, string: str) -> str:
        """
        Remove special characters from the string.
        """
        return string.replace(' ', '').replace('/', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('-', '')
    
    def clean_from_special_characters_without_minus(self, string: str) -> str:
        """
        Remove special characters from the string.
        """
        return string.replace(' ', '').replace('/', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '')
    
    def get_last_number_sequence(self, string: str) -> str:
        """
        Get the last sequence of digits from the string, separated from other characters by a space, "(", ")", "[", "]", "-" or "/".
        """
        # Remove all non-digit characters from the string
        cleaned_string = ''.join(char if char.isdigit() else ' ' for char in string)
        # Split the cleaned string into parts and return the last part
        parts = cleaned_string.split()
        return parts[-1] if parts else ''