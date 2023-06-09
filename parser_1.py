from pickle import FLOAT, INT
from lexer import tokens
import ply.yacc as yacc
from semantic_cube import BOOL, CHAR, SEMANTIC_CUBE


#Esta es la estructura que debe tener mi codigo
def p_program(p):
    '''program : PROGRAM ID PUNCOM vars bloque  '''
    p[0] = "ACC"

#En las siguiente 4 reglas me ayudan a construir el area de las variables
#tanto como los distintitos tipos(en este caso solo int y float) como la cantidad
def p_vars(p):
    '''vars : VAR id DOSPUN TIPO  PUNCOM asignacion_id'''
    for var in p[2]:
        add_variable_to_table(var, p[4])

def p_id(p):
    '''id : ID acum_id'''
    p[0] = [p[1]] + p[2]

def p_acum_id(p):
    '''acum_id : COMA ID acum_id
                | empty'''
    if len(p) > 2:
        p[0] = [p[2]] + p[3]
    else:
        p[0] = []


def p_asignacion_id(p):
    '''asignacion_id : id DOSPUN TIPO PUNCOM asignacion_id
                  | empty'''


# Reglas para arreglos

#Esta regla define los tipos de variables que 
def p_TIPO(p):
    '''TIPO : INT
            | FLOAT
            | BOOL
            | CHAR'''
    
#Punto neuralgico para reconocer el tipo de var


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
    '''INCREMENTO : ID MAS MAS PUNCOM'''


def p_DECREMENTO(p):
    '''DECREMENTO : ID MENOS MENOS PUNCOM'''


def p_asignacion(p):
    '''asignacion : ID IGUAL expresion PUNCOM'''

    
    
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
    

#Reglas de parser para recibir condiciones
def p_condicion_if(p):
    '''condicion_if : IF PARIZQ expresion PARDER bloque PUNCOM
                 | IF PARIZQ expresion PARDER bloque else_condicion PUNCOM'''


def p_else_condicion(p):
    '''else_condicion : ELSE bloque'''


def p_condicion_while(p):
    '''condicion_while : WHILE PARIZQ expresion PARDER bloque PUNCOM'''



#Regla de parser para recibir funciones
def p_funcion(p):
    '''funcion : VOID ID PARIZQ vars_func PARDER vars bloque PUNCOM
               | INT ID PARIZQ vars_func PARDER vars bloque PUNCOM
               | FLOAT ID PARIZQ vars_func PARDER vars bloque PUNCOM
               | BOOL ID PARIZQ vars_func PARDER vars bloque PUNCOM
               | CHAR ID PARIZQ vars_func PARDER vars bloque PUNCOM'''
    
 
def p_condicion_for(p):
    '''condicion_for : FOR ID IGUAL expresion TO expresion DO bloque'''

def p_vars_func(p):
    '''vars_func : TIPO ID COMA vars_func
                 | TIPO ID
                 | empty'''

#Regla que define la jeraquia de dos expresiones
def p_expresion(p):
    '''expresion : exp 
                 | exp MAYOR exp
                 | exp MENOR exp
                 | exp DIFF exp
                 | exp mas_igual exp
                 | exp menor_igual exp
                 | exp igual_igual exp
                 | exp diff_igual exp'''
    

def p_mas_igual(p):
    '''mas_igual : MAYOR IGUAL'''

def p_menor_igual(p):
    '''menor_igual : MENOR IGUAL'''

def p_igual_igual(p):
    '''igual_igual : IGUAL IGUAL'''

def p_diff_igual(p):
    '''diff_igual : DIFF IGUAL'''


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
               | CTEB
               | CTEC'''

def p_empty(p):
    '''empty :'''
    pass


#Pilas que guardan los operadores y operandos
operador_stack = []
operando_stack = []
tipos_stack = []

#Pila que nos ayuda a mantener el flujo del programa
salto_stack = []

cuad_cont = 0
cuad = []


#Direccion de memoria
const_int = 0
const_float = 1000
const_char = 3000
local_int = 4000
local_float = 5000
local_bool = 6000
local_char = 7000
global_int = 8000
global_float = 9000
global_bool = 10000
global_char = 11000

# Define the symbol table as a dictionary
symbol_table = {}

# Implement the analyze_semantics() function
def analyze_semantics(ast):
    if isinstance(ast, BinOpNode):
        left_type = analyze_semantics(ast.left)
        right_type = analyze_semantics(ast.right)
        if left_type != right_type:
            raise TypeError("Type mismatch in binary operation")
        return left_type
    elif isinstance(ast, IntNode):
        return "int"
    elif isinstance(ast, FloatNode):
        return "float"
    else:
        raise TypeError(f"Unknown AST node type: {type(ast).__name__}")

def analyze_semantics(ast):
    if isinstance(ast, AssignNode):
        variable_name = ast.variable_name
        if variable_name not in symbol_table:
            raise NameError(f"Variable {variable_name} is not declared")
        analyze_semantics(ast.value)
    elif isinstance(ast, VarNode):
        variable_name = ast.variable_name
        if variable_name not in symbol_table:
            raise NameError(f"Variable {variable_name} is not declared")
    elif isinstance(ast, DeclNode):
        variable_name = ast.variable_name
        if variable_name in symbol_table:
            raise NameError(f"Variable {variable_name} is already declared")
        symbol_table[variable_name] = ast.type_name
    else:
        for child in ast.children:
            analyze_semantics(child)


parser = yacc.yacc()
def parse(data):
    return parser.parse(data)
#ast = parser.parse(source_code, lexer=lexer)
#analyze_semantics(ast)