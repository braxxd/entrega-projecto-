%{
#include <stdio.h>
#include <stdlib.h>
#include "lexer.h"  // Declaración de las funciones generadas por Flex
%}

%%

\[                    { printf("Corchete de apertura: %s\n", yytext); }
\]                    { printf("Corchete de cierre: %s\n", yytext); }
\(                    { printf("Paréntesis de apertura: %s\n", yytext); }
\)                    { printf("Paréntesis de cierre: %s\n", yytext); }

[0-9]+(\.[0-9]+)?      { printf("Número: %s\n", yytext); }           // Números enteros y decimales
[+-/*=]                 { printf("Operador: %s\n", yytext); }         // Operadores
[a-zA-Z_][a-zA-Z0-9_]*  { printf("Identificador: %s\n", yytext); }   // Identificadores (variables, funciones)
\"[^\"]*\"             { printf("Cadena de texto: %s\n", yytext); }   // Cadenas de texto entre comillas
'[^']*'                { printf("Carácter: %s\n", yytext); }          // Caracteres literales
\/\/[^\n]*             { printf("Comentario de una línea: %s\n", yytext); }  // Comentarios de una línea (//)
\/\*[^*]*\*+([^/*][^*]*\*+)*\/ { printf("Comentario multilínea: %s\n", yytext); }  // Comentarios multilínea (/* */)

[ \t\n]                { /* Ignorar espacios y saltos de línea */ }   // Espacios y saltos de línea

;                      { printf("Punto y coma: %s\n", yytext); }  // Reconocer punto y coma
\{                     { printf("Llave de apertura: %s\n", yytext); }  // Reconocer llave de apertura
\}                     { printf("Llave de cierre: %s\n", yytext); }  // Reconocer llave de cierre
.                      { printf("Carácter no reconocido: %s\n", yytext); }  // Cualquier otro carácter no reconocido

%%

int yywrap() {
    return 1;
}

int main(void) {
   
    yylex();  // Llamada a la función generada por Flex para analizar la entrada
    return 0;
}