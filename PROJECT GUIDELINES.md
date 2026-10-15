# Project Guidelines

## Python Source Code Documentation

Use NumPy-style docstrings to document every public function, class, and module. Document private code when its purpose or behavior is not obvious from the implementation. Docstrings must explain the contract and the reason behind non-obvious decisions, not repeat the code.

### General Rules

- Write a complete sentence in the first line of every docstring and end it with a period.
- The first line must be a one-sentence summary (≤ 72 chars).
- Describe what the function or class does, its important constraints, side effects, and failure behavior.
- Use `:param:`, `:returns:`, and `:raises:` for every parameter, return value, and exception callers may need to handle.
- Use `` `code` `` for code symbols and short code fragments. Use `:func:` or `:class:` when linking to a related function or class improves navigation.
- Document units, nullability, mutability, ordering, thread-safety, blocking behavior, and resource ownership when applicable.
- Keep documentation current with the implementation. Update it in the same change as the code it describes.
- Do not add `:author:`, `:version:`, or `:since:` tags. Git blame is the source of truth.
- Do not document private implementation details unless they prevent a likely maintenance mistake; prefer clear names and code first.

### Type Hints

All public functions and methods must have type hints. Use modern Python syntax:

- Use `X | Y` for unions (3.10+), not `Optional[X]` or `Union[X, Y]`.
- Use builtin generics: `list[int]`, `dict[str, Any]`, `tuple[int, ...]` — not `List[int]` from `typing`.
- Use `from __future__ import annotations` at the top of modules that need forward references.
- Annotate return types even for `None`-returning functions: `def log(msg: str) -> None:`.
- Use `TypeAlias` for complex type aliases: `Vector = list[float]`.

### Docstring Template (NumPy Style)

Use this template for public functions and methods. Keep only the sections that apply.

```python
def example(input: int, flag: bool = False) -> str:
    """Summarize what the function does in one sentence.

    Provide a longer description if the behavior is not obvious from
    the signature. Describe side effects, ordering, or important
    edge cases here.

    Parameters
    ----------
    input : int
        Meaning, valid range, and nullability.
    flag : bool, optional
        Meaning of the flag. Default is ``False``.

    Returns
    -------
    str
        Meaning of the result.

    Raises
    ------
    ValueError
        If ``input`` is negative.
    ExampleError
        If the operation cannot be completed.

    See Also
    --------
    :func:`related_function`
    :class:`RelatedClass`

    Examples
    --------
    >>> example(42)
    '42'
    """
```

Rules when completing the template:

- Start the summary with a verb: `Creates`, `Returns`, `Loads`, `Validates`, `Plots`.
- Describe observable behavior rather than the internal algorithm.
- List every exception that is part of the function contract. Do not list exceptions that cannot reasonably occur for callers.
- State whether a returned collection is mutable, whether it may be `None`, and whether it is a copy or a live view when that matters.
- For overrides, write documentation only when adding behavior or clarifying an inherited contract.
- For simple getters, setters, and `__init__` with obvious parameters, a docstring is optional when the name and signature fully express the behavior.

### Class Template

```python
class Example:
    """Represent or provide [the primary responsibility of this class].

    Describe important collaboration, lifecycle, invariants, or usage
    constraints.

    Parameters
    ----------
    arg : type
        Meaning of the argument.

    See Also
    --------
    :class:`RelatedClass`
    \"\"\"

    def __init__(self, arg: int) -> None:
        \"\"\"Initialize with [meaning of arg].\"\"\"
        self._arg = arg

    def perform(self, input: int) -> str:
        \"\"\"[Verb] [what the method does and the result or state change].

        Parameters
        ----------
        input : int
            Meaning, valid range, and nullability.

        Returns
        -------
        str
            Meaning of the result.

        Raises
        ------
        ValueError
            If ``input`` is invalid.
        """
```

### Module Docstring

Every module starts with a docstring:

```python
"""Plot f(x) = 1/(x+1) and its antiderivative h(x) = ln|x+1|.

Features:
    - Vertical asymptote at x = -1
    - Filled area: definite integral from 1 to 4
"""
```

- First line: one-sentence summary.
- Blank line.
- Optional extended description, features list, or usage notes.

### Modern Python Syntax

Use these idioms in all source code:

- **f-strings** over `%` or `.format()`: `f\"Value: {x}\"`.
- **`pathlib.Path`** over `os.path`: `Path(\"data/file.txt\").read_text()`.
- **`dataclasses`** for data-carrying classes: `@dataclass` with type hints.
- **`match`** for multi-branch logic (3.10+): `match status:` instead of long `if/elif` chains.
- **Context managers** for resource management: `with open(...) as f:`.
- **`__all__`** in `__init__.py` to declare the public API of a package.
- **`X | Y`** for union types, **`list[T]`** for builtin generics (3.9+).
- **`from __future__ import annotations`** at the top of modules that use forward references.
- **`@deprecated`** decorator (3.13+) or `:deprecated:` in docstring for deprecated APIs.
- **`enum`** for fixed sets of values, not magic strings or integers.
- **`Protocol`** (from `typing`) for structural subtyping when needed.

## Conventional Commits

Format:

```text
<type>(optional-scope): short description
```

Example:

```text
feat(integrals): add definite integral plot
```

| Type | Meaning |
|---|---|
| `feat` | Add a new user-visible feature |
| `fix` | Fix a bug or incorrect behavior |
| `docs` | Documentation-only changes |
| `refactor` | Change code structure without changing behavior |
| `test` | Add or modify tests |
| `chore` | Maintenance work that does not affect application behavior |
| `build` | Changes to dependencies, venv, or build configuration |
| `ci` | Changes to continuous integration or deployment workflows |
| `perf` | Improve performance |
| `style` | Formatting or stylistic changes with no behavior change |
| `revert` | Revert a previous commit |

Examples for this project:

```text
feat(integrals): add definite integral plot
feat(contours): add cauchy integral visualization
fix(residues): correct pole order calculation
docs: describe fourier series convergence
test(integrals): verify antiderivative at bounds
refactor(graph): extract axis setup helper
build: upgrade numpy
chore: remove generated build artifacts
ci: add ruff lint workflow
```

For breaking changes:

```text
feat(integrals)!: replace plot coordinate system
```

Or include a footer:

```text
feat(integrals): change plot output format

BREAKING CHANGE: existing PNG outputs must be regenerated
```

Recommended rules:

- Use the imperative mood: `add`, `fix`, `update`, not `added` or `fixes`.
- Keep the subject short, ideally under 72 characters.
- Do not end the subject with a period.
- Use `docs`, not `doc`, to follow the conventional name.
- Keep one logical change per commit.
- Use a scope when it adds clarity: `integrals`, `contours`, `residues`, `build`, or `docs`.
- Do not use `chore` for feature or bug-fix work.

## Linter

Run Ruff when source code is stable.

```bash
# Check
.venv/bin/ruff check .

# Auto-fix
.venv/bin/ruff check . --fix

# Format
.venv/bin/ruff format .
```

Configuration lives in `pyproject.toml` under `[tool.ruff]`."
