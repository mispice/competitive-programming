class Solution:
    def sortSentence(self, s: str) -> str:
        sent = s.split()
        recon = ''
        for i in range(len(sent)):
            sindex = i
            for a in range(i+1,len(sent)):
                if int(list(sent[sindex])[-1]) > int(list(sent[a])[-1]):
                    sindex = a
            num_rev = sent[sindex][0:-1]
            recon += str(num_rev)+ ' '
            sent[i],sent[sindex] = sent[sindex],sent[i]

        return recon.strip()
    
