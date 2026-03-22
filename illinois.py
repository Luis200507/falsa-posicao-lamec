from mpmath import mp

mp.dps = 50

def mfp(f,n,tol=mp.mpf('1e-10'),max_iter=10000):
    step_size = mp.mpf('0.01')
    int_a=mp.mpf('0')
    int_b=int_a+step_size
    f_roots = []
    lst_update = ''
    
    def skip_int():
        nonlocal int_a, int_b
        int_a=int_b
        int_b += step_size

    for nb in range(n):
        i=0
        init_int_a=int_a
        while f(int_a)*f(int_b)>0 and 0<=i<max_iter:
            skip_int()
            i+=1
        
        if i==max_iter:
            print(f'Sem raízes no intervalo de {init_int_a} - {int_b}')

            break
        
        if f(int_b) == 0:
            f_roots.append(int_b)
            skip_int()
            continue
        elif f(int_a) == 0:
            f_roots.append(int_a)
            skip_int()
            continue

        a=int_a
        b=int_b
        fa = f(a)
        fb = f(b)
        while abs(b-a)>tol:
            xn = ((a*fb-b*fa)/(fb - fa))
            fxn = f(xn)
            if fa*fxn<0:
                if lst_update=='b':
                    fa/=2
                b=xn
                fb = fxn
                lst_update = 'b'
            else:
                #print('bb')
                if lst_update=='a':
                    fb/=2
                a=xn
                fa = fxn
                lst_update = 'a'
 
        skip_int()
        f_roots.append(xn)
    
    print("\nraizes:\n\n", [str(x) for x in f_roots], "\n")

mfp(lambda x: x**4-2*x**3+3*x-10, 3) # funcao anonima, numero de raizes 

