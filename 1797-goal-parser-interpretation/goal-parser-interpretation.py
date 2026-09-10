class Solution:
    def interpret(self, command: str) -> str:
        s=""
        i=0
        while  i <(len(command)):
            if command[i]=="G":
                s+="G"
                i+=1
            elif command[i]=="(" and command[i+1]==")":
                s+="o"
                i+=1
            elif  command[i]=="(" and command[i+1]=="a" and command[i+2]=="l" and command[i+3]==")":
                s+="al"
                i+=3
            else:
                i+=1
        return s