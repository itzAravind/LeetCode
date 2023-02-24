class Solution:
    def interpret(self, command: str) -> str:
#       result = []
#        for i in range(len(command)):
#            if command[i] == "G":
#                result.append("G")
#            elif command[i] == "(":
#                if command[i+1] == ")":
#                    result.append("o")
#                else:
#                    result.append("al")
#        return "".join(result)

# Using replace()
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        return command