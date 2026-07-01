class Solution:
    def encode(self, strs: List[str]) -> str:
        word = ""

        for i in range(len(strs)):
            l= len(strs[i])
            word+= str(l) + "_" + strs[i]

        return word

    def decode(self, s: str) -> List[str]:

        list=[]
        i=0
        while i<len(s):
            Scount=""
            while s[i] != "_":
                Scount+= s[i]
                i+=1

            count= int(Scount)
            i+=1

            list.append(s[i : i+count])
            i+=count


        return list
