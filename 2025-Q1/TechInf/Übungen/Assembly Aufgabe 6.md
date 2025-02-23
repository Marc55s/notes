## Aufgabe
- Bytes 1-4 und 2-3 sollen getauscht werden
```asm
.global _start
_start:
main:
@ switch bytes 1-4,2-3
ldr r0, =0x1234abcd
ldr r12, =0xFF

lsr r1, r0, #24
lsl r2, r0, #24
orr r1, r2,r1

and r3, r0, #0x00FF0000
lsr r3, #8
and r4, r0, #0x0000FF00
lsl r4, #8
orr r3, r3,r4

orr r5, r1,r3


bx lr
_end:

```


