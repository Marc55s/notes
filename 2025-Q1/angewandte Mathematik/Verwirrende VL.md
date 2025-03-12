# Coding-Teil
- Fibonacci
- Goldener Schnitt
```java
int fib(int n){
  if(n<=0)
    return 0;
  if(n == 1){
    return n;
  }
  return fib(n-2) + fib(n-1);
}

float golden_ratio(int n) {
 if(n == 0)
   return 1;
 else if(n == 1)
   return (sqrt(5)-1)/2;
  return golden_ratio(n-2) - golden_ratio(n-1);
 
}

void setup(){
  for(int i = 0; i<50;i++){
    //println(fib(i));
    println("phi("+i+") = "+golden_ratio(i));
  }
}

```
- Genauigkeit von Fließkommazahlen bei Rechnungen
# Fortgesetzte Verwirrung 
- Zelluläre Automaten