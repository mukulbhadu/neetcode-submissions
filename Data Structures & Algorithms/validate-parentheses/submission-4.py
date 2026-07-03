class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range(0,len(s)):
            if(s[i]=='('):
                st.append(')')
            elif(s[i]=='{'):
                st.append('}')
            elif(s[i]=='['):
                st.append(']')
            else:
                if(len(st)==0):
                    return False
                elif(s[i]==st[-1]):
                    st.pop()
                else:
                    return False
                    
        if len(st)==0:
            return True
        return False