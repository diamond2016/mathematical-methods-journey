## Notes on course

Choice of language (pythons vs java)

1. The "Notebook" Workflow (The Killer Feature)
The README specifies a "Deliverable" for almost every week (plots, animations, notebooks).

In Python: You use Jupyter Notebooks. You can write a mathematical formula in LaTeX, write the code immediately below it, and see the resulting graph in the same window. It becomes a "living textbook."
In Java: You are typically in an IDE (IntelliJ/Eclipse). To see a graph, you usually have to run the code, which pops up a separate window (like Swing or JavaFX). Your "notes" (the math) and your "code" (the implementation) will live in two different worlds.

2. The Scientific Ecosystem (The "Math-to-Code" Gap)
Python: Libraries like NumPy (arrays), SciPy (signal processing/integration), Matplotlib (plotting), and SymPy (symbolic math) are the industry standard.
Crucial Point: SymPy allows you to do Symbolic Math (e.g., you tell it diff(sin(x), x) and it returns cos(x)). This is incredibly helpful when you are learning the theory and want to verify your manual derivations.
Java: While you have Apache Commons Math, it is much more "verbose." You will spend more time writing boilerplate code (defining types, managing objects) than actually exploring the math. Java is built for engineering systems; Python is built for exploring data and math.

3. Visualization
Mathematical methods (like Mappings or Fourier transforms) are highly visual.

Python's matplotlib and plotly make it trivial to create heatmaps, complex planes, and animations.
Java's plotting libraries (like JFreeChart) are powerful for business charts (bar, line, pie), but they are much clunkier for high-level mathematical visualizations.
If you really want to use Java (The "Middle Ground")
If you feel that using Python will be a distraction because you'll be fighting the syntax, you can try this:

Use the IJava Kernel: You can actually install a Java kernel for Jupyter. This allows you to use the Jupyter Notebook interface (the "living textbook" feel) but write Java code inside the cells.

Libraries to use:
Apache Commons Math: For the heavy lifting (integrals, FFT, etc.).
JFreeChart: For the plots.
JavaFX: If you want to build the animations mentioned in Week 2.

Summary Comparison
| Feature | Python (Recommended) | Java (The Alternative) | | :--- | :--- | :--- | | Learning Curve | Low (Focus on math) | High (Focus on boilerplate/types) | | Documentation | Integrated (Notebooks) | Fragmented (Code vs. Notes) | | Symbolic Math | Excellent (SymPy) | Limited/Difficult | | Visualization | Instant & Beautiful | Requires more setup/boilerplate | | Industry Standard | Scientific Computing | Enterprise/Systems |

My advice: Treat Python as a "Mathematical Calculator" rather than a programming language. Don't worry about "learning Python" deeply; just learn the specific commands needed to plot and compute. This will keep your focus on the Mathematical Methods, which is the real goal of your journey.

Let's remain in python.

## General structure:
Every week has:

- notes.md (The Theory): This is your "Textbook." Use it to write down the mathematical definitions, derivations, and theorems. Use LaTeX for math (it's built into Markdown).

- exercise.ipynb (The Lab): This is your "Experiment." This is where you write code, run it, and see the graphs. It is an interactive playground.

## Jupyter "Quick Start"

Jupyter "Quick Start" (The Only Shortcuts You Need)

When you open a Notebook, you are in two modes: Command Mode (blue border) and Edit Mode (green border).

The "Must-Know" Shortcuts:

- Shift + Enter: Run the current cell and move to the next one. (The most important!)
- Esc: Switch to Command Mode (to move cells around).
- Enter: Switch to Edit Mode (to type code/text).
- A: Insert a cell Above (in Command Mode).
- B: Insert a cell Below (in Command Mode).
- M: Change a cell to Markdown (for writing math/text).
- Y: Change a cell to Code (for writing Python).
- DD: Delete a cell (in Command Mode).

## LaTeX "Quick Start"

The Two Rules of LaTeX in Markdown

1. Inline Math (The \$ ... \$ rule): Use single dollar signs when the math is part of a sentence.

Example: The value of $z$ is increasing.
Result: The value of $z$ is increasing.

2. Block Math (The \$$ ... \$$ rule): Use double dollar signs when you want the equation to be centered on its own line and look "big."

Example: $$z = x + iy$$
