class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str=""
        for word in strs:
            encoded_str += str(len(word)) + "#"+ word
        return encoded_str
    def decode(self, s: str) -> List[str]:
       decoded_str=[]
       while s :
        hash_index=s.index("#")
        length=int(s[:hash_index])
        word=s[hash_index + 1 : hash_index +1+ length]
        decoded_str.append(word)
        s=s[hash_index+length+1:]
       return decoded_str

       


  
