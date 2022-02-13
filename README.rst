Basic usage
***********
    apyori-run < data/transaction.tsv

Use TSV output
**************
    apyori-run -f tsv < data/transaction.tsv

Fields of output mean:
- Base item.
- Appended item.
- Support.
- Confidence.
- Lift.

Specify the minimum support
***************************
    apyori-run -s 0.5 < data/transaction.tsv

Specify the minimum confidence
******************************
    apyori-run -c 0.5 < data/transaction.tsv
