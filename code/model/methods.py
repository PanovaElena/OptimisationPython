
class Method:
    
    def __init__(self):
        self.if_cancel_computing = False
        
    def set_if_cancel_computing(self, if_cancel=True):
        self.if_cancel_computing = if_cancel
    
    def _check_to_end_computing(self):
        return self.if_cancel_computing
                 
    def compute(self, f, borders, n_steps, eps, r):
        return self._compute(f, float(borders[0]), float(borders[1]),
                             int(n_steps), float(eps), float(r))
        
    def _compute(self, f, x1, x2, n_steps, eps, r):
        list_res = [(x1, f(x1)), (x2, f(x2))]
        x_star = x1
        iter = 0
        cur_eps = x2 - x1
        while not self._check_to_end_computing() \
              and iter < n_steps and cur_eps > eps:
            self._compute_params(r, list_res)
            points = max(((list_res[i], list_res[i+1])\
                          for i in range(len(list_res)-1)),  key=self._get_R)
            x_star = self._get_x_star(points)
            list_res.append((x_star, f(x_star)))
            list_res.sort(key=lambda x: x[0])
            cur_eps = points[1][0] - points[0][0]
            iter += 1
        n_steps = iter
        return x_star, f(x_star), cur_eps, n_steps, list_res



class BruteForce(Method):

    def _get_R(self, points):
        def compute_R(x0, x1):
            return x1 - x0
        return compute_R(points[0][0], points[1][0])
    
    def _get_x_star(self, points):
        def compute_x_star(x0, x1):
            return 0.5 * (x1+x0)
        return compute_x_star(points[0][0], points[1][0])

    def _compute_params(self, r, list_res):
        pass        
        

class SmartMethod(Method):
    
    def _compute_params(self, r, list_res):                    
        def compute_M(r, list_res):
            return r * max((abs((list_res[i+1][1]-list_res[i][1]) / (list_res[i+1][0]-list_res[i][0]))\
                        for i in range(len(list_res)-1)))                      
        self.M = compute_M(r, list_res)
        
                     

class PiyavskyMethod(SmartMethod):
    
    def _get_R(self, points):
        def compute_R(M, x0, x1, f0, f1):
            return 0.5 * M * (x1-x0) - (f1+f0)*0.5
        return compute_R(self.M, points[0][0], points[1][0], points[0][1], points[1][1])
    
    def _get_x_star(self, points):
        def compute_x_star(M, x0, x1, f0, f1):
            return 0.5 * (x1+x0) - (f1-f0) / (2*M)
        return compute_x_star(self.M, points[0][0], points[1][0], points[0][1], points[1][1])
        
      
class StronginMethod(SmartMethod):
    
    def _get_R(self, points):
        def compute_R(M, x0, x1, f0, f1):
            return M * (x1-x0) + (f1-f0)**2/(M * (x1-x0)) - 2*(f1+f0)
        return compute_R(self.M, points[0][0], points[1][0], points[0][1], points[1][1])
    
    def _get_x_star(self, points):
        def compute_x_star(M, x0, x1, f0, f1):
            return 0.5 * (x1+x0) - (f1-f0)/(2*M)
        return compute_x_star(self.M, points[0][0], points[1][0], points[0][1], points[1][1])  
     