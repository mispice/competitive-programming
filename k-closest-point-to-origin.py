class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        final_val = []
        ordered_list = []
        curr_val = 0
        val=0
        for i in range(len(points)):
            curr_val = sqrt(pow(points[i][0] - 0, 2) + pow(points[i][1] - 0, 2))
            real_port = curr_val.real
            imag_port = curr_val.imag
            curr_val = real_port + imag_port
            final_val.append((curr_val, points[i]))
        final_val.sort()
        for i in range(k):
            ordered_list.append(final_val[i][1])
        return ordered_list
