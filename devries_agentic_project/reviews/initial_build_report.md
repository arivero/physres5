# Initial build report

Commands run from repository root:

```bash
make numbers
make test
make inventory
make manuscript
pdfinfo manuscript/main.pdf | grep Pages
```

Results:

- numerical script runs and prints the DeVries roots;
- Python tests pass: 4 passed;
- PDF inventory contains 30 local PDFs and all are represented in `context/source_inventory.md`;
- REVTeX seed manuscript compiles with `pdflatex` through the `make manuscript` target;
- initial seed manuscript page count: 12 pages.

The manuscript is a seed for Codex expansion, not the final 35--50 page paper. The task packets specify the expansion route.
