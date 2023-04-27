from lexer import tokens
import ply.yacc as yacc

#Esta es la estructura que debe tener mi codigo
def p_program(p):
    '''program : PROGRAM ID PUNCOM vars bloque  '''
    p[0] = "ACC"

#En las siguiente 4 reglas me ayudan a construir el area de las variables
#tanto como los distintitos tipos(en este caso solo int y float) como la cantidad
def p_vars(p):
    '''vars : VAR id DOSPUN TIPO PUNCOM asignacion_id'''


def p_id(p):
    '''id : ID acum_id'''


def p_acum_id(p):
    '''acum_id : COMA ID acum_id
                | empty'''

def p_asignacion_id(p):
    '''asignacion_id : id DOSPUN TIPO PUNCOM asignacion_id
                  | empty'''


# Reglas para arreglos
def p_array(p):
    '''array : ID CORCHIZQ exp CORCHDER'''

def p_array_init(p):
    '''array_init : array IGUAL CORCHIZQ lista_exp CORCHDER'''

def p_lista_exp(p):
    '''lista_exp : expresion multiples_exp'''

def p_multiples_exp(p):
    '''multiples_exp : COMA expresion multiples_exp
                     | empty'''

#Esta regla define los tipos de variables que 
def p_TIPO(p):
    '''TIPO : INT
            | FLOAT
            | BOOL'''


#Esta regla establece la semantica de un bloque de codigo
def p_bloque(p):
    '''bloque : LLAVIZQ multiples_estatutos LLAVDER'''


#Esta regla define los diferente estatutos y la que le sigue
# me ayuda a poder establecer mas de un estatuto, ya sea varias asignaciones 
# o varias condiciones (if else) 
def p_estatuto(p):
    '''estatuto : asignacion
                 | condicion_if
                 | condicion_while
                 | escritura'''
    

def p_multiples_estatutos(p):
    '''multiples_estatutos : estatuto multiples_estatutos
                       | empty'''
    

#Las sigueintes reglas son para establecer la semantica 
# de los difetenes tipos de estatutos 



#Regla para hacer la funcion de decremento e incremento (resta 1 o suma 1)
def p_INCREMENTO(p):
    '''INCREMENTO : MAS MAS'''


def p_DECREMENTO(p):
    '''DECREMENTO : MENOS MENOS'''


def p_asignacion(p):
    '''asignacion : ID IGUAL expresion PUNCOM
                  | ID INCREMENTO PUNCOM
                  | ID DECREMENTO PUNCOM'''
    
    
def p_expresion_and(p):
    'expresion : expresion AND expresion'


def p_expresion_or(p):
    'expresion : expresion OR expresion'


def p_escritura(p):
    '''escritura : PRINT PARIZQ print_expresion PARDER PUNCOM'''


def p_print_expresion(p):
    '''print_expresion : expresion multiples_print
                       | CTESTRING multiples_print'''


def p_multiples_print(p):
    '''multiples_print : COMA  print_expresion
                 | empty'''
    

def p_condicion_if(p):
    '''condicion_if : IF PARIZQ expresion PARDER bloque PUNCOM
                 | IF PARIZQ expresion PARDER bloque else_condicion PUNCOM'''


def p_else_condicion(p):
    '''else_condicion : ELSE bloque'''


def p_condicion_while(p):
    '''condicion_while : WHILE PARIZQ expresion PARDER bloque PUNCOM'''

#Regla que define la jeraquia de dos expresiones
def p_expresion(p):
    '''expresion : exp 
                 | exp MAYOR exp
                 | exp MENOR exp
                 | exp DIFF exp
                 | exp mas_igual exp
                 | exp menor_igual exp
                 | exp igual_igual exp'''

def p_mas_igual(p):
    '''mas_igual : MAYOR IGUAL'''

def p_menor_igual(p):
    '''menor_igual : MENOR IGUAL'''

def p_igual_igual(p):
    '''igual_igual : IGUAL IGUAL'''


#Las siguientes dos reglas suman o restan 2 terminos con una llamada recursiva
def p_exp(p):
    '''exp : termino exp_operacion'''


def p_exp_operacion(p):
    '''exp_operacion : MAS termino exp_operacion
                     | MENOS termino exp_operacion
                     | empty'''
    
#Las siguientes dos reglas multiplican o dividen 2 factores con una llamada recursiva

def p_termino(p):
    '''termino : factor termino_operador'''


def p_termino_operador(p):
    '''termino_operador : POR factor termino_operador
                        | DIV factor termino_operador
                        | MOD factor termino_operador
                        | empty'''
    

def p_factor(p):
    '''factor : PARIZQ expresion PARDER
              | MAS var_cte
              | MENOS var_cte
              | var_cte
              | empty'''


def p_var_cte(p):
    '''var_cte : ID
               | CTEI
               | CTEF
               | CTEB'''

def p_empty(p):
    '''empty :'''
    pass


parser = yacc.yacc()
def parse(data):
    return parser.parse(data)