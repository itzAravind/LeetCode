class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")
#        id_list = list(address)
#        for i in range(len(id_list)):
#            if id_list[i] == ".":
#                id_list[i] = "[.]"
#        return ("".join(id_list))

"""This is a Python class with a single method, defangIPaddr, which takes a string address as input and returns a string where each occurrence of "." in the input string is replaced with the string "[.]", effectively "defanging" the IP address.

The implementation of the defangIPaddr method is quite simple: it uses the built-in replace method of the string object to replace all occurrences of "." with "[.]" and returns the resulting string.

For example, if the input address is "192.168.0.1", the method will return "192[.]168[.]0[.]1". The replace method simply searches the input string for all occurrences of "." and replaces each one with "[.]", resulting in the defanged IP address.

Overall, this solution is a straightforward and efficient solution to the problem of defanging an IP address. It uses the built-in string method replace to perform the required transformation, which is a reliable and commonly-used way to manipulate strings in Python."""
