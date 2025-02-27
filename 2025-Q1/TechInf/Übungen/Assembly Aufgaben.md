## Aufgabe 6
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

## Aufgabe 5
```asm
.global _start
_start:
main:

push {r4, r5, lr}
mov r0, #1
mov r1, #-1
mov r2, #15
mov r3, #0x80000000

mvn r0, r0
add r0, #1

mvn r1, r1
add r1, #1

mvn r2, r2
add r2, #1

mvn r3, r3
add r3, #1

@--------------------

rsb r4, r1, #0

@--------------------

sub r4, r2, r2, lsl #1

@--------------------
mov r5, #0x11111111
eor r4, r3, r5
add r4, r4, #1


pop {r4, r5, pc}
_end:
	
```
