%{
#include <stdio.h>
%}
%%
[Cc][Hh][Aa][Rr][Uu][Ss][Aa][Tt]   { printf("university"); }
.|\n          { printf("%s", yytext); }
%%
int yywrap(void){}
int main(){
yylex();
return 0;
}