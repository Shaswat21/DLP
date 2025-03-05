%{
#include <stdio.h>
%}
%%
[0-9]+ {printf("%s\n",yytext);}
.
%%
int yywrap(void){}
int main(){
yylex();
return 0;
}