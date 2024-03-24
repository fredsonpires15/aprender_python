from _001_pilhas import Stack



def exp_em_falta(exp):

    par_fechados , par_abertos  = 0, 0
    
    col_abertos, col_fechados   = 0, 0
    
    chav_abertos, chav_fechados = 0, 0


    
    for ch in exp:
        if ch in exp:
            if ch == '(':
                par_abertos += 1
            elif ch == ')':
                par_fechados += 1
            elif  ch == '[':
                col_abertos += 1
            elif  ch == ']':
                col_fechados
            elif  ch == '{':
                chav_abertos += 1
            elif  ch == '}':
                chav_fechados += 1
    
        if par_abertos > par_fechados:
            return 'Falta fechar parênteses ")"'
        
        elif par_abertos < par_fechados:
            return 'Falta abrir parênteses "("'
        
        elif col_abertos > col_fechados:
            return 'Falta fechar o colchete: "]"'
        
        elif col_abertos < col_fechados:
            return 'Falta abrir o colchete: "[" '
        
        elif chav_abertos > chav_fechados:
            return 'Falta fechar o chaveta: "{" '
        
        elif chav_abertos < chav_fechados:
            return 'Falta fechar o chaveta: "}" '
    

def parent_equilibri(exp):
    pilha = Stack()

    em_falta = exp_em_falta(exp)

    for ch in exp:
        if ch == '(' or ch == '[' or ch == '{':
            p = pilha.push(ch)

            return em_falta 
        
        elif ch == ')' or ch == ']' or ch =='}':
            if p.is_empty():
                return   em_falta
            
        
            topo = p.pop()

            if not emparelhado(ch, topo):
                return False


    return p.is_empty()

def emparelhado(ch_1, ch_2):
    return( ch_1 == ')' and ch_2 == '(')  or (ch_1 == ']' and ch_2 == '[')  or (ch_1=='}' and ch_2 == '{')
    

    
if __name__ == '__main__':
    p1 = parent_equilibri('(e({))')
    p2 = exp_em_falta('(({))') 
    print(p2)
    
    
    



    
    
    