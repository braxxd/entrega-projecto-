#ifndef LEXER_H
#define LEXER_H

enum TokenType {
    TOKEN_IF = 256,
    TOKEN_ELSE,
    TOKEN_WHILE,
    TOKEN_RETURN,
    TOKEN_ID,
    TOKEN_NUMBER,
    TOKEN_EQ,
    TOKEN_ASSIGN,
    TOKEN_PLUS,
    TOKEN_MINUS,
    TOKEN_MUL,
    TOKEN_DIV,
    TOKEN_SEMICOLON,
    TOKEN_ERROR
};

extern int yylex();

#endif