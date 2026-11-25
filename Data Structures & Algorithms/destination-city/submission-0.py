class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        rec = {} # city -> frequency
        for i in range(len(paths)): 
            if paths[i][0] in rec:
                rec[paths[i][0]] += 1
            else:
                rec[paths[i][0]] = 1
            if paths[i][1] in rec:
                rec[paths[i][1]] += 1
            else:
                rec[paths[i][1]] = 1

        p = []
        for key in rec:
            if rec[key] == 1:
                p.append(key)

        for i in range(len(paths)): 
            if paths[i][1] == p[0]: 
                return p[0]
            elif paths[i][1] == p[1]: 
                return p[1]



