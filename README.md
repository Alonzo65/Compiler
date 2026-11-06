# KXI Compiler

A compiler for the KXI programming language, written in Python as my senior project.

This project takes KXI source code through tokenization, parsing, semantic analysis, and assembly generation. It also provides separate modes for inspecting tokens, visualizing the abstract syntax tree (AST), and checking a program before generating assembly.

## Features

- **Lexical and syntax analysis** using PLY.
- **AST construction and visualization** using pydot and Graphviz.
- **Symbol tables and semantic checks** for declarations, scope, types, assignments, function calls, parameters, return values, array indexing, and control flow.
- **Visitor-based transformations** that prepare expressions, statements, and function calls for code generation.
- **Assembly generation** targeting the project's virtual machine instruction set.

The KXI grammar includes classes, public and private members, constructors, methods, arrays, arithmetic and Boolean expressions, `if`/`else`, `while`, `switch`, and console input/output with `cin` and `cout`. The included [C.kxi](Compiler/C.kxi) demonstration exercises recursion, arithmetic precedence, function calls, and control flow.

## Getting started

Use Python 3.10 or newer. Copies of PLY and pydot are included in the repository; install `pyparsing` for pydot's DOT parser support.

```sh
git clone https://github.com/Alonzo65/Compiler.git
cd Compiler/Compiler
python -m pip install pyparsing
```

Run the commands below from this inner `Compiler` directory. If your system uses `python3` for Python 3, substitute it for `python`.

Check the included demonstration, then generate assembly:

```sh
python Parser.py C.kxi -s
python Parser.py C.kxi -c
```

The compiler writes the generated assembly to `output.asm` in the current directory. **Executing it requires the matching assembler and virtual machine, which are not included in this repository.**

## Compiler modes

```sh
python Parser.py <source-file> <flag>
```

| Flag | Purpose | Result |
| --- | --- | --- |
| `-l` | Run the lexer | Prints each token's type, line number, and value |
| `-p` | Parse and visualize the program | Writes the AST to `output.png`; requires Graphviz |
| `-s` | Build symbol tables and run semantic checks | Prints diagnostics when errors are found |
| `-c` | Run the compilation pipeline | Writes assembly to `output.asm` |

For example:

```sh
python Parser.py lexer-test.kxi -l
python Parser.py C.kxi -p
```

### AST visualization

To use `-p`, install [Graphviz](https://graphviz.org/download/) and make its `bin` directory available on your system's `PATH`. Confirm that the terminal can find it with:

```sh
dot -V
```

Then run a parsing command and open the generated `output.png`.

## Small KXI example

Save this as `hello.kxi` inside the inner `Compiler` directory:

```text
void kxi2023 main() {
    int value = 2 + 3 * 4;
    cout << value;
    cout << '\n';
}
```

Check and compile it:

```sh
python Parser.py hello.kxi -s
python Parser.py hello.kxi -c
```

This produces `output.asm` for a program that prints `14` followed by a newline when run with the matching assembler and VM.

## Exploring the code

| File or directory | Role |
| --- | --- |
| [compilerLex.py](Compiler/compilerLex.py) | Keywords, tokens, and lexer rules |
| [Parser.py](Compiler/Parser.py) | Grammar, parser construction, command-line modes, and compilation pipeline |
| [nodes.py](Compiler/nodes.py) | AST and assembly node definitions |
| [symboltable.py](Compiler/symboltable.py) | Symbol table and activation record structures |
| [semStarter.py](Compiler/semStarter.py) | Runs the semantic validation passes |
| [visitor.py](Compiler/visitor.py) | AST visualization, symbol table construction, semantic checks, transformations, and code generation |
| [C.kxi](Compiler/C.kxi) | Larger demonstration with recursive Fibonacci, input/output, and control flow |
| [test_pytest.py](Compiler/test_pytest.py) | Parser tests for the sample inputs |
| [ply/](Compiler/ply/) and [pydot/](Compiler/pydot/) | Included third-party libraries |

Start with `compilerLex.py` and the grammar in `Parser.py` to follow how source code becomes an AST. The mode handling near the end of `Parser.py` shows the order of the semantic and code generation passes.

## Tests

The included pytest suite checks that eight sample inputs produce a parse tree. These tests also generate `output.png`, so Graphviz must be installed and available on `PATH`.

From the inner `Compiler` directory:

```sh
python -m pip install pytest
python -m pytest -q
```

The separate `lexer-test.kxi`, `syntax-test.kxi`, and `semantic-test.kxi` files are manual test inputs. The syntax and semantic files intentionally contain errors, identified in their comments.

## Usage notes

- Run `-s` and resolve reported errors before using `-c`. The compilation mode does not automatically stop after every semantic error.
- Each compilation replaces `output.asm`, and each AST visualization replaces `output.png`.
- PLY may report an unused `UNKNOWN` token and a shift/reduce conflict when constructing the parser. These warnings also appear when compiling the included demonstration.
