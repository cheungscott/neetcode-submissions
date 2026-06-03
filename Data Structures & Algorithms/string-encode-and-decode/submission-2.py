class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += f"{s}`"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        word = ""
        for c in s:
            if c == "`":
                decoded_strs.append(word)
                word = ""
            else:
                word += c
        return decoded_strs
        