#!/bin/bash

#Ensures only one argument is supplied to the script
if [ "$#" -ne 1 ]; then
    echo "Usage: ./generate_report.sh <exp_name>"
    exit 1
fi

EXP_NAME="$1"

#Line renders report: qmd -> jupyter -> latex -> pdf. -P flag passes config and generates the report based on the config parameters and results
quarto render report_template.qmd -P exp_name:"$EXP_NAME" -o "$EXP_NAME.pdf" --output-dir "$EXP_NAME/report"
echo "done"
echo "report in $EXP_NAME/report"
