Python is a high-level, platform-independent, interpreted, dynamically typed, object-oriented programming language.

```text
┌─────────────────────────────────┐
│       High-Level Language       │
│       Python / C# / Java        │
│          sourcecode.py          │
└──────────────┬──────────────────┘
               │
               │ Compiler (Compilation)
               ↓
┌─────────────────────────────────┐
│      Intermediate Language      │
│              (ILL)              │
│          bytecode.pyc           │
└──────────────┬──────────────────┘
               │
               │ Python Virtual Machine
               │      (Interpretation)
               ↓
┌─────────────────────────────────┐
│          Machine LL             │
│           0s and 1s             │
└──────────────┬──────────────────┘
               │
               ↓
              CPU