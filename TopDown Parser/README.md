**Overview**

A non-recursive implementation of a top-down parser from scratch using a tree data structure instead of stack.
The parse table can be modified to use a different grammar.



**Default Grammar:**

*Terminals:* [a,+,*,(,)]

*Non-Terminals:* [A,B,C,D,E]

*Characters having special meanings:* [eps,$]



**Rules:**

A -> CB

B -> +CB | eps

C -> ED

D -> *ED | eps

E -> (A) | a
