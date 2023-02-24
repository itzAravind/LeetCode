class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")
#        id_list = list(address)
#        for i in range(len(id_list)):
#            if id_list[i] == ".":
#                id_list[i] = "[.]"
#        return ("".join(id_list))