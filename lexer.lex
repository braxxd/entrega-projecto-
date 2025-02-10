%{
#include <stdio.h>
#include <stdlib.h>
#include "lexer.h"  
%}

%%

\[                    { printf("Corchete de apertura: %s\n", yytext); }
\]                    { printf("Corchete de cierre: %s\n", yytext); }
\(                    { printf("Paréntesis de apertura: %s\n", yytext); }
\)                    { printf("Paréntesis de cierre: %s\n", yytext); }

[0-9]+(\.[0-9]+)?      { printf("Número: %s\n", yytext); }           
[+-/*=]                 { printf("Operador: %s\n", yytext); }         
[a-zA-Z_][a-zA-Z0-9_]*  { printf("Identificador: %s\n", yytext); }   
\"[^\"]*\"             { printf("Cadena de texto: %s\n", yytext); }   
'[^']*'                { printf("Carácter: %s\n", yytext); }         
\/\/[^\n]*             { printf("Comentario de una línea: %s\n", yytext); } 
\/\*[^*]*\*+([^/*][^*]*\*+)*\/ { printf("Comentario multilínea: %s\n", yytext); }  

[ \t\n]                { /* Ignorar espacios y saltos de línea */ }   

;                      { printf("Punto y coma: %s\n", yytext); } 
\{                     { printf("Llave de apertura: %s\n", yytext); }  
\}                     { printf("Llave de cierre: %s\n", yytext); }  
.                      { printf("Carácter no reconocido: %s\n", yytext); } 

%%

int yywrap() {
    return 1;
}

int main(void) {
   
    yylex();  
    return 0;
}