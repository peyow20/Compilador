
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARR ARRAY BOOL COMA CORCHDER CORCHIZQ CTEB CTEF CTEI CTESTRING DIFF DIV DOSPUN ELSE FLOAT ID IF IGUAL INT LLAVDER LLAVIZQ MAS MAYOR MENOR MENOS MOD OR PARDER PARIZQ POR PRINT PROGRAM PUNCOM VAR WHILEprogram : PROGRAM ID PUNCOM vars bloque  vars : VAR id DOSPUN TIPO PUNCOM asignacion_idid : ID acum_idacum_id : COMA ID acum_id\n                | emptyasignacion_id : id DOSPUN TIPO PUNCOM asignacion_id\n                  | emptyarray : ID CORCHIZQ exp CORCHDERarray_init : array IGUAL CORCHIZQ lista_exp CORCHDERlista_exp : expresion multiples_expmultiples_exp : COMA expresion multiples_exp\n                     | emptyTIPO : INT\n            | FLOAT\n            | BOOLbloque : LLAVIZQ multiples_estatutos LLAVDERestatuto : asignacion\n                 | condicion_if\n                 | condicion_while\n                 | escrituramultiples_estatutos : estatuto multiples_estatutos\n                       | emptyINCREMENTO : MAS MASDECREMENTO : MENOS MENOSasignacion : ID IGUAL expresion PUNCOM\n                  | ID INCREMENTO PUNCOM\n                  | ID DECREMENTO PUNCOMexpresion : expresion AND expresionexpresion : expresion OR expresionescritura : PRINT PARIZQ print_expresion PARDER PUNCOMprint_expresion : expresion multiples_print\n                       | CTESTRING multiples_printmultiples_print : COMA  print_expresion\n                 | emptycondicion_if : IF PARIZQ expresion PARDER bloque PUNCOM\n                 | IF PARIZQ expresion PARDER bloque else_condicion PUNCOMelse_condicion : ELSE bloquecondicion_while : WHILE PARIZQ expresion PARDER bloque PUNCOMexpresion : exp \n                 | exp MAYOR exp\n                 | exp MENOR exp\n                 | exp DIFF exp\n                 | exp mas_igual exp\n                 | exp menor_igual expmas_igual : MAYOR IGUALmenor_igual : MENOR IGUALexp : termino exp_operacionexp_operacion : MAS termino exp_operacion\n                     | MENOS termino exp_operacion\n                     | emptytermino : factor termino_operadortermino_operador : POR factor termino_operador\n                        | DIV factor termino_operador\n                        | MOD factor termino_operador\n                        | emptyfactor : PARIZQ expresion PARDER\n              | MAS var_cte\n              | MENOS var_cte\n              | var_cte\n              | emptyvar_cte : ID\n               | CTEI\n               | CTEF\n               | CTEBempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,7,26,],[0,-1,-16,]),'ID':([2,6,8,12,14,15,16,17,24,28,33,34,35,46,47,49,54,55,63,65,66,67,68,69,70,71,72,74,75,78,79,80,89,98,100,112,120,123,125,127,],[3,10,18,18,-17,-18,-19,-20,40,41,41,41,41,41,41,41,-26,-27,10,-25,41,41,41,41,41,41,41,41,41,41,41,41,41,-45,-46,-30,-35,-38,-36,10,]),'PUNCOM':([3,26,28,29,30,36,37,38,39,41,42,43,44,45,48,50,51,52,53,56,57,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,87,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,115,116,117,118,119,121,124,126,],[4,-16,-65,54,55,63,-13,-14,-15,-61,65,-39,-65,-65,-59,-60,-62,-63,-64,-23,-24,-65,-65,-65,-65,-65,-65,-65,-47,-65,-65,-50,-51,-65,-65,-65,-55,-57,-58,112,-28,-29,-40,-45,-41,-46,-42,-43,-44,-65,-65,-65,-65,-65,-56,120,123,-48,-49,-52,-53,-54,125,127,-37,]),'VAR':([4,],[6,]),'LLAVIZQ':([5,63,85,86,93,94,122,127,128,],[8,-65,8,8,-2,-7,8,-65,-6,]),'LLAVDER':([8,11,12,13,14,15,16,17,27,54,55,65,112,120,123,125,],[-65,26,-65,-22,-17,-18,-19,-20,-21,-26,-27,-25,-30,-35,-38,-36,]),'IF':([8,12,14,15,16,17,54,55,65,112,120,123,125,],[19,19,-17,-18,-19,-20,-26,-27,-25,-30,-35,-38,-36,]),'WHILE':([8,12,14,15,16,17,54,55,65,112,120,123,125,],[20,20,-17,-18,-19,-20,-26,-27,-25,-30,-35,-38,-36,]),'PRINT':([8,12,14,15,16,17,54,55,65,112,120,123,125,],[21,21,-17,-18,-19,-20,-26,-27,-25,-30,-35,-38,-36,]),'DOSPUN':([9,10,23,25,40,64,92,],[22,-65,-3,-5,-65,-4,114,]),'COMA':([10,35,40,41,43,44,45,48,50,51,52,53,61,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,89,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,115,116,117,118,119,],[24,-65,24,-61,-39,-65,-65,-59,-60,-62,-63,-64,89,89,-65,-65,-65,-65,-65,-65,-65,-47,-65,-65,-50,-51,-65,-65,-65,-55,-57,-58,-65,-28,-29,-40,-45,-41,-46,-42,-43,-44,-65,-65,-65,-65,-65,-56,-48,-49,-52,-53,-54,]),'IGUAL':([18,68,69,],[28,98,100,]),'MAS':([18,28,31,33,34,35,41,44,45,46,48,50,51,52,53,66,67,68,69,70,71,72,74,75,77,78,79,80,81,83,84,89,98,100,104,105,106,107,108,109,117,118,119,],[31,47,56,47,47,47,-61,74,-65,47,-59,-60,-62,-63,-64,47,47,47,47,47,47,47,47,47,-51,47,47,47,-55,-57,-58,47,-45,-46,74,74,-65,-65,-65,-56,-52,-53,-54,]),'MENOS':([18,28,32,33,34,35,41,44,45,46,48,50,51,52,53,66,67,68,69,70,71,72,74,75,77,78,79,80,81,83,84,89,98,100,104,105,106,107,108,109,117,118,119,],[32,49,57,49,49,49,-61,75,-65,49,-59,-60,-62,-63,-64,49,49,49,49,49,49,49,49,49,-51,49,49,49,-55,-57,-58,49,-45,-46,75,75,-65,-65,-65,-56,-52,-53,-54,]),'PARIZQ':([19,20,21,28,33,34,35,46,66,67,68,69,70,71,72,74,75,78,79,80,89,98,100,],[33,34,35,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-45,-46,]),'INT':([22,114,],[37,37,]),'FLOAT':([22,114,],[38,38,]),'BOOL':([22,114,],[39,39,]),'ELSE':([26,110,],[-16,122,]),'CTEI':([28,33,34,35,46,47,49,66,67,68,69,70,71,72,74,75,78,79,80,89,98,100,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-45,-46,]),'CTEF':([28,33,34,35,46,47,49,66,67,68,69,70,71,72,74,75,78,79,80,89,98,100,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-45,-46,]),'CTEB':([28,33,34,35,46,47,49,66,67,68,69,70,71,72,74,75,78,79,80,89,98,100,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-45,-46,]),'POR':([28,33,34,35,41,45,46,48,50,51,52,53,66,67,68,69,70,71,72,74,75,78,79,80,83,84,89,98,100,106,107,108,109,],[-65,-65,-65,-65,-61,78,-65,-59,-60,-62,-63,-64,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-57,-58,-65,-45,-46,78,78,78,-56,]),'DIV':([28,33,34,35,41,45,46,48,50,51,52,53,66,67,68,69,70,71,72,74,75,78,79,80,83,84,89,98,100,106,107,108,109,],[-65,-65,-65,-65,-61,79,-65,-59,-60,-62,-63,-64,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-57,-58,-65,-45,-46,79,79,79,-56,]),'MOD':([28,33,34,35,41,45,46,48,50,51,52,53,66,67,68,69,70,71,72,74,75,78,79,80,83,84,89,98,100,106,107,108,109,],[-65,-65,-65,-65,-61,80,-65,-59,-60,-62,-63,-64,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-65,-57,-58,-65,-45,-46,80,80,80,-56,]),'MAYOR':([28,33,34,35,41,43,44,45,46,48,50,51,52,53,66,67,73,74,75,76,77,78,79,80,81,83,84,89,104,105,106,107,108,109,115,116,117,118,119,],[-65,-65,-65,-65,-61,68,-65,-65,-65,-59,-60,-62,-63,-64,-65,-65,-47,-65,-65,-50,-51,-65,-65,-65,-55,-57,-58,-65,-65,-65,-65,-65,-65,-56,-48,-49,-52,-53,-54,]),'MENOR':([28,33,34,35,41,43,44,45,46,48,50,51,52,53,66,67,73,74,75,76,77,78,79,80,81,83,84,89,104,105,106,107,108,109,115,116,117,118,119,],[-65,-65,-65,-65,-61,69,-65,-65,-65,-59,-60,-62,-63,-64,-65,-65,-47,-65,-65,-50,-51,-65,-65,-65,-55,-57,-58,-65,-65,-65,-65,-65,-65,-56,-48,-49,-52,-53,-54,]),'DIFF':([28,33,34,35,41,43,44,45,46,48,50,51,52,53,66,67,73,74,75,76,77,78,79,80,81,83,84,89,104,105,106,107,108,109,115,116,117,118,119,],[-65,-65,-65,-65,-61,70,-65,-65,-65,-59,-60,-62,-63,-64,-65,-65,-47,-65,-65,-50,-51,-65,-65,-65,-55,-57,-58,-65,-65,-65,-65,-65,-65,-56,-48,-49,-52,-53,-54,]),'AND':([28,33,34,35,41,42,43,44,45,46,48,50,51,52,53,58,59,61,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,115,116,117,118,119,],[-65,-65,-65,-65,-61,66,-39,-65,-65,-65,-59,-60,-62,-63,-64,66,66,66,-65,-65,-65,-65,-65,-65,-65,-47,-65,-65,-50,-51,-65,-65,-65,-55,66,-57,-58,-65,66,66,-40,-45,-41,-46,-42,-43,-44,-65,-65,-65,-65,-65,-56,-48,-49,-52,-53,-54,]),'OR':([28,33,34,35,41,42,43,44,45,46,48,50,51,52,53,58,59,61,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,115,116,117,118,119,],[-65,-65,-65,-65,-61,67,-39,-65,-65,-65,-59,-60,-62,-63,-64,67,67,67,-65,-65,-65,-65,-65,-65,-65,-47,-65,-65,-50,-51,-65,-65,-65,-55,67,-57,-58,-65,67,67,-40,-45,-41,-46,-42,-43,-44,-65,-65,-65,-65,-65,-56,-48,-49,-52,-53,-54,]),'PARDER':([33,34,35,41,43,44,45,46,48,50,51,52,53,58,59,60,61,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,88,89,90,91,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,113,115,116,117,118,119,],[-65,-65,-65,-61,-39,-65,-65,-65,-59,-60,-62,-63,-64,85,86,87,-65,-65,-65,-65,-65,-65,-65,-65,-65,-47,-65,-65,-50,-51,-65,-65,-65,-55,109,-57,-58,-31,-65,-34,-32,-28,-29,-40,-45,-41,-46,-42,-43,-44,-65,-65,-65,-65,-65,-56,-33,-48,-49,-52,-53,-54,]),'CTESTRING':([35,89,],[62,62,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'vars':([4,],[5,]),'bloque':([5,85,86,122,],[7,110,111,126,]),'id':([6,63,127,],[9,92,92,]),'multiples_estatutos':([8,12,],[11,27,]),'estatuto':([8,12,],[12,12,]),'empty':([8,10,12,28,33,34,35,40,44,45,46,61,62,63,66,67,68,69,70,71,72,74,75,78,79,80,89,104,105,106,107,108,127,],[13,25,13,50,50,50,50,25,76,81,50,90,90,94,50,50,50,50,50,50,50,50,50,50,50,50,50,76,76,81,81,81,94,]),'asignacion':([8,12,],[14,14,]),'condicion_if':([8,12,],[15,15,]),'condicion_while':([8,12,],[16,16,]),'escritura':([8,12,],[17,17,]),'acum_id':([10,40,],[23,64,]),'INCREMENTO':([18,],[29,]),'DECREMENTO':([18,],[30,]),'TIPO':([22,114,],[36,124,]),'expresion':([28,33,34,35,46,66,67,89,],[42,58,59,61,82,95,96,61,]),'exp':([28,33,34,35,46,66,67,68,69,70,71,72,89,],[43,43,43,43,43,43,43,97,99,101,102,103,43,]),'termino':([28,33,34,35,46,66,67,68,69,70,71,72,74,75,89,],[44,44,44,44,44,44,44,44,44,44,44,44,104,105,44,]),'factor':([28,33,34,35,46,66,67,68,69,70,71,72,74,75,78,79,80,89,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,106,107,108,45,]),'var_cte':([28,33,34,35,46,47,49,66,67,68,69,70,71,72,74,75,78,79,80,89,],[48,48,48,48,48,83,84,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'print_expresion':([35,89,],[60,113,]),'mas_igual':([43,],[71,]),'menor_igual':([43,],[72,]),'exp_operacion':([44,104,105,],[73,115,116,]),'termino_operador':([45,106,107,108,],[77,117,118,119,]),'multiples_print':([61,62,],[88,91,]),'asignacion_id':([63,127,],[93,128,]),'else_condicion':([110,],[121,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID PUNCOM vars bloque','program',5,'p_program','parser_1.py',6),
  ('vars -> VAR id DOSPUN TIPO PUNCOM asignacion_id','vars',6,'p_vars','parser_1.py',12),
  ('id -> ID acum_id','id',2,'p_id','parser_1.py',16),
  ('acum_id -> COMA ID acum_id','acum_id',3,'p_acum_id','parser_1.py',20),
  ('acum_id -> empty','acum_id',1,'p_acum_id','parser_1.py',21),
  ('asignacion_id -> id DOSPUN TIPO PUNCOM asignacion_id','asignacion_id',5,'p_asignacion_id','parser_1.py',24),
  ('asignacion_id -> empty','asignacion_id',1,'p_asignacion_id','parser_1.py',25),
  ('array -> ID CORCHIZQ exp CORCHDER','array',4,'p_array','parser_1.py',30),
  ('array_init -> array IGUAL CORCHIZQ lista_exp CORCHDER','array_init',5,'p_array_init','parser_1.py',33),
  ('lista_exp -> expresion multiples_exp','lista_exp',2,'p_lista_exp','parser_1.py',36),
  ('multiples_exp -> COMA expresion multiples_exp','multiples_exp',3,'p_multiples_exp','parser_1.py',39),
  ('multiples_exp -> empty','multiples_exp',1,'p_multiples_exp','parser_1.py',40),
  ('TIPO -> INT','TIPO',1,'p_TIPO','parser_1.py',44),
  ('TIPO -> FLOAT','TIPO',1,'p_TIPO','parser_1.py',45),
  ('TIPO -> BOOL','TIPO',1,'p_TIPO','parser_1.py',46),
  ('bloque -> LLAVIZQ multiples_estatutos LLAVDER','bloque',3,'p_bloque','parser_1.py',51),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','parser_1.py',58),
  ('estatuto -> condicion_if','estatuto',1,'p_estatuto','parser_1.py',59),
  ('estatuto -> condicion_while','estatuto',1,'p_estatuto','parser_1.py',60),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','parser_1.py',61),
  ('multiples_estatutos -> estatuto multiples_estatutos','multiples_estatutos',2,'p_multiples_estatutos','parser_1.py',65),
  ('multiples_estatutos -> empty','multiples_estatutos',1,'p_multiples_estatutos','parser_1.py',66),
  ('INCREMENTO -> MAS MAS','INCREMENTO',2,'p_INCREMENTO','parser_1.py',76),
  ('DECREMENTO -> MENOS MENOS','DECREMENTO',2,'p_DECREMENTO','parser_1.py',80),
  ('asignacion -> ID IGUAL expresion PUNCOM','asignacion',4,'p_asignacion','parser_1.py',84),
  ('asignacion -> ID INCREMENTO PUNCOM','asignacion',3,'p_asignacion','parser_1.py',85),
  ('asignacion -> ID DECREMENTO PUNCOM','asignacion',3,'p_asignacion','parser_1.py',86),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_and','parser_1.py',90),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_or','parser_1.py',94),
  ('escritura -> PRINT PARIZQ print_expresion PARDER PUNCOM','escritura',5,'p_escritura','parser_1.py',98),
  ('print_expresion -> expresion multiples_print','print_expresion',2,'p_print_expresion','parser_1.py',102),
  ('print_expresion -> CTESTRING multiples_print','print_expresion',2,'p_print_expresion','parser_1.py',103),
  ('multiples_print -> COMA print_expresion','multiples_print',2,'p_multiples_print','parser_1.py',107),
  ('multiples_print -> empty','multiples_print',1,'p_multiples_print','parser_1.py',108),
  ('condicion_if -> IF PARIZQ expresion PARDER bloque PUNCOM','condicion_if',6,'p_condicion_if','parser_1.py',112),
  ('condicion_if -> IF PARIZQ expresion PARDER bloque else_condicion PUNCOM','condicion_if',7,'p_condicion_if','parser_1.py',113),
  ('else_condicion -> ELSE bloque','else_condicion',2,'p_else_condicion','parser_1.py',117),
  ('condicion_while -> WHILE PARIZQ expresion PARDER bloque PUNCOM','condicion_while',6,'p_condicion_while','parser_1.py',121),
  ('expresion -> exp','expresion',1,'p_expresion','parser_1.py',125),
  ('expresion -> exp MAYOR exp','expresion',3,'p_expresion','parser_1.py',126),
  ('expresion -> exp MENOR exp','expresion',3,'p_expresion','parser_1.py',127),
  ('expresion -> exp DIFF exp','expresion',3,'p_expresion','parser_1.py',128),
  ('expresion -> exp mas_igual exp','expresion',3,'p_expresion','parser_1.py',129),
  ('expresion -> exp menor_igual exp','expresion',3,'p_expresion','parser_1.py',130),
  ('mas_igual -> MAYOR IGUAL','mas_igual',2,'p_mas_igual','parser_1.py',133),
  ('menor_igual -> MENOR IGUAL','menor_igual',2,'p_menor_igual','parser_1.py',136),
  ('exp -> termino exp_operacion','exp',2,'p_exp','parser_1.py',140),
  ('exp_operacion -> MAS termino exp_operacion','exp_operacion',3,'p_exp_operacion','parser_1.py',144),
  ('exp_operacion -> MENOS termino exp_operacion','exp_operacion',3,'p_exp_operacion','parser_1.py',145),
  ('exp_operacion -> empty','exp_operacion',1,'p_exp_operacion','parser_1.py',146),
  ('termino -> factor termino_operador','termino',2,'p_termino','parser_1.py',151),
  ('termino_operador -> POR factor termino_operador','termino_operador',3,'p_termino_operador','parser_1.py',155),
  ('termino_operador -> DIV factor termino_operador','termino_operador',3,'p_termino_operador','parser_1.py',156),
  ('termino_operador -> MOD factor termino_operador','termino_operador',3,'p_termino_operador','parser_1.py',157),
  ('termino_operador -> empty','termino_operador',1,'p_termino_operador','parser_1.py',158),
  ('factor -> PARIZQ expresion PARDER','factor',3,'p_factor','parser_1.py',162),
  ('factor -> MAS var_cte','factor',2,'p_factor','parser_1.py',163),
  ('factor -> MENOS var_cte','factor',2,'p_factor','parser_1.py',164),
  ('factor -> var_cte','factor',1,'p_factor','parser_1.py',165),
  ('factor -> empty','factor',1,'p_factor','parser_1.py',166),
  ('var_cte -> ID','var_cte',1,'p_var_cte','parser_1.py',170),
  ('var_cte -> CTEI','var_cte',1,'p_var_cte','parser_1.py',171),
  ('var_cte -> CTEF','var_cte',1,'p_var_cte','parser_1.py',172),
  ('var_cte -> CTEB','var_cte',1,'p_var_cte','parser_1.py',173),
  ('empty -> <empty>','empty',0,'p_empty','parser_1.py',176),
]
