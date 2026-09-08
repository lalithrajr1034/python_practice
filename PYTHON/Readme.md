Python is a high-level, platform-independent, compiled & interpreted, dynamically typed, object-oriented programming language.

```text
┌─────────────────────────────────┐
│       High-Level Language       │
│       Python / C# / Java        │
│          sourcecode.py          │
└──────────────┬──────────────────┘
               |
            Compiler
               │      (Compilation)
               ↓
┌─────────────────────────────────┐
│      Intermediate Language      │
│              (ILL)              │
│          bytecode.pyc           │
└──────────────┬──────────────────┘
               │
        Python Virtual Machine 
               │      (Interpretation)
               ↓
┌─────────────────────────────────┐
│          Machine LL             │
│           0s and 1s             │
└──────────────┬──────────────────┘
               │
               ↓
              CPU

High lavel language  - read by human not by machine
Intermediate LL      - not read by both human and machine 
Machine LL           - read by human and machine 


platform independent:
same code is run by every platform like windows, macos, linux because of pyton virtal machine

compiled and interpretation:
compiled: source code is converted to byte code 
interpretd: that byte code is executed line by line 



<h2>Histry Of Python</h2>
implementation: 1989
relesed       : 1991
who           : Guido van rossum
show name     : Monty Python’s Flying Circus