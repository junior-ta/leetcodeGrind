# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:
# string encode(vector<string> strs) {
#     // ... your code
#     return encoded_string;
# }


# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#     //... your code
#     return strs;
# }


# So Machine 1 does:
# string encoded_string = encode(strs);
# and Machine 2 does:
# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.


# Implement the encode and decode methods.

# Example 1:
# Input: dummy_input = ["Hello","World"]
# Output: ["Hello","World"]
#
# Explanation:
    # Machine 1:
    # Codec encoder = new Codec();
    # String msg = encoder.encode(strs);
    # Machine 1 ---msg---> Machine 2
    #
    # Machine 2:
    # Codec decoder = new Codec();
    # String[] strs = decoder.decode(msg);


# Example 2:
# Input: dummy_input = [""]
# Output: [""]


class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []

        for s in strs:
            parts.append(str(len(s)))
            parts.append("_")
            parts.append(s)

        return "".join(parts)

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


if __name__ == '__main__':
    test1= Solution()
    encoded=test1.encode([""])
    decoded=test1.decode(encoded)
    print(encoded)
    print(decoded)