import os
import glob
import argparse

import pandas as pd


def combine_csv_to_xlsx(path: str, output: str) -> None:
    """Combine all CSV files in *path* into an Excel workbook."""
    all_files = glob.glob(os.path.join(path, "*.csv"))
    writer = pd.ExcelWriter(output, engine="xlsxwriter")

    for f in all_files:
        df = pd.read_csv(f)
        sheet_name = os.path.splitext(os.path.basename(f))[0]
        df.to_excel(writer, sheet_name=sheet_name, index=False)

    writer.close()


def combine_xlsx_to_csv(path: str, output: str) -> None:
    """Combine all XLSX files in *path* into a single CSV file."""
    all_files = glob.glob(os.path.join(path, "*.xlsx"))
    dfs = [pd.read_excel(f) for f in all_files]
    if dfs:
        combined = pd.concat(dfs, ignore_index=True)
    else:
        combined = pd.DataFrame()
    combined.to_csv(output, index=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Combine CSV or XLSX files")
    parser.add_argument(
        "--mode",
        choices=["csv_to_xlsx", "xlsx_to_csv"],
        default="csv_to_xlsx",
        help="Conversion direction",
    )
    parser.add_argument(
        "--path",
        default="./",
        help="Directory containing the files",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Name of the output file",
    )
    args = parser.parse_args()

    if args.mode == "csv_to_xlsx":
        output = args.output or "out.xlsx"
        combine_csv_to_xlsx(args.path, output)
    else:
        output = args.output or "out.csv"
        combine_xlsx_to_csv(args.path, output)


if __name__ == "__main__":
    main()

