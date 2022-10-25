class Solution: 
    def select(self, arr, i):
        sindex = i
        for a in range(i+1,len(arr)):
            if arr[sindex]>arr[a]:
                sindex = a
        return sindex
    
    def selectionSort(self, arr,n):
        #code here
        for j in range(n):
            sindex = self.select(arr, j)
            if min != j:
                var = arr[sindex]
                arr[sindex],arr[j] = arr[j],var
