from mpmath import mp

def mfp(f,n,tol=mp.mpf(f'1e-6'),max_iter=10000):
    step_size = mp.mpf('0.01')
    interval_a=mp.mpf('0') # intervalo a
    interval_b=interval_a+step_size # intervalo b
    f_roots = []
    
    
    def skip_int(): # pular intervalo em distancia = step_size 
        nonlocal interval_a, interval_b
        interval_a=interval_b
        interval_b += step_size
    def add_root(r):
        skip_int()
        f_roots.append(r)
    def aproximate(a,b):
        print(a, b)
        aprox_index = 0
        fa=f(a)
        fb=f(b)
        lst_update = ''
        while abs(b-a)>tol:
            xn = (a*fb-b*fa)/(fb - fa)
            fxn = f(xn)
            if fa*fxn<0:
                #print('x1')
                if lst_update=='b':
                    fa/=2
                b=xn
                fb = fxn
                lst_update = 'b'
            else:
                #print('x2')
                if lst_update=='a':
                    fb/=2
                a=xn
                fa = fxn
                lst_update = 'a'
            aprox_index+=1
        #print('x')
        return xn, aprox_index


    for nb in range(n):
        i=0 # tentativas de achar um intervalo que contenha raiz
        init_interval_a=interval_a # distancia {a} inicial em que tenta buscar intervalo com proxima raiz
        while f(interval_a)*f(interval_b)>0 and 0<=i<max_iter:
            skip_int()
            i+=1
        
        if i==max_iter:
            print(f'No roots found on interval: {init_interval_a} - {interval_b}')
            break
        if f(interval_b) == 0:
            add_root(interval_b)
            continue
        elif f(interval_a) == 0:
            add_root(interval_a)
            continue

        xn, aprox_iter = aproximate(interval_a, interval_b)
        # numero de iterações para aproximar, após achar o intervalo que tem raiz
 
        print(f'For the root number {nb+1}, was need {aprox_iter} iterations: {xn}')
        add_root(xn)
    
    print("\nRoots:\n\n", [str(x) for x in f_roots], "\n")

mfp(lambda x: (mp.cosh(x)*mp.cos(x))-1,3) # funcao anonima, numero de raizes 
    
