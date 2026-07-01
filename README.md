**Step by step approach to a leetcode question**

1. Evaluate the constraints and how they can help our code.
   For example: if we are trying to find the longest sequence, there is no need to start checking a sequence that is not assured to be longer than our current longest sequence's length.
   
2. Start by thinking hard about how the problem can be solved in one or two linear passes.

3. Consider iterating left to right, but alos right to left.

4. Find ingenious ways to store metadata: Hashset and map, Prefix, Suffix, inside a string, in buckets (an array of arrays)...
   Remeber that you can store different type of stuff in a hash even TUPLES, except mutable objects like lists, sets, dict, 
