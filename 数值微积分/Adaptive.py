# 自适应积分

import sympy as sp
import re
x = sp.symbols('x')


def Adaptive(expr, a0, b0, tol = 1e-6):
    Trapizoidal = lambda a, b: sp.N((b - a) / 2 *
                                    (expr.subs(x, a) + 
                                     expr.subs(x, b))) # 梯形法则
    Simpson = lambda a, b: sp.N(((b - a) / 6 *
                                 (expr.subs(x, a) + 
                                  expr.subs(x, b) + 
                                  4 * expr.subs(x, (a + b) / 2)))) # 辛普森法则
    Midpoint = lambda a, b: sp.N((b - a) *
                                 expr.subs(x, (a + b) / 2)) # 中点法则
    
    ans = 0; cnt = 0
    intervals = [(a0, b0, Simpson(a0, b0), tol)] # 栈
    while intervals: # 栈非空
        a, b, old_approx, tol = intervals.pop()
        c = (a + b) / 2
        # new1_approx = Trapizoidal(a, c); new2_approx = Trapizoidal(c, b)
        new1_approx = Simpson(a, c); new2_approx = Simpson(c, b)
        # if abs(old_approx - new1_approx - new2_approx) < 3 * tol:
        if abs(old_approx - new1_approx - new2_approx) < 10 * tol:
            ans += new1_approx + new2_approx
            cnt += 2 # 有效区间
        else:
            intervals.extend([(a, c, new1_approx, tol / 2), (c, b, new2_approx, tol / 2)])
    return 'Integrate: %s\nNumber of intervals: %s' % (ans, cnt)


if __name__ == '__main__':
    expr = sp.sympify(input())
    # a, b, tol = map(sp.sympify, re.split(r'[\s,;]+', input().strip()))
    a, b = map(sp.sympify, re.split(r'[\s,;]+', input().strip()))
    print(Adaptive(expr, a, b))