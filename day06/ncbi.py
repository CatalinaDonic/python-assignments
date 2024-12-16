import argparse
import os
import csv
from datetime import datetime
from Bio import Entrez

Entrez.email = "catalina.donic@weizmann.ac.il"

# Search and download data from NCBI
def download_ncbi_data(database, term, number):
    print(f"Searching {database} for '{term}'...")
    handle = Entrez.esearch(db=database, term=term, retmax=number)
    search_results = Entrez.read(handle)
    handle.close()

    ids = search_results.get("IdList", [])
    total_found = search_results.get("Count", 0)

    print(f"Found {total_found} items. Downloading {number}...")

    filenames = []
    for i, id_ in enumerate(ids):
        handle = Entrez.efetch(db=database, id=id_, rettype="gb", retmode="text")
        filename = f"{term}_{i+1}.txt"
        with open(filename, "w") as f:
            f.write(handle.read())
        handle.close()
        filenames.append(filename)

    return filenames, total_found

# Log results to a CSV file
def log_results(date, database, term, number, total):
    log_file = "search_log.csv"
    file_exists = os.path.isfile(log_file)

    with open(log_file, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["date", "database", "term", "max", "total"])
        writer.writerow([date, database, term, number, total])

# Main function
def main():
    parser = argparse.ArgumentParser(description="Download data from NCBI.")
    parser.add_argument("--database", default="nucleotide", help="NCBI database to search (default: nucleotide)")
    parser.add_argument("--term", required=True, help="Search term")
    parser.add_argument("--number", type=int, default=10, help="Number of items to download (default: 10)")

    args = parser.parse_args()

    # Search and download
    filenames, total_found = download_ncbi_data(args.database, args.term, args.number)

    # Print downloaded filenames
    print("Downloaded files:")
    for filename in filenames:
        print(f"  {filename}")

    # Log the results
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_results(current_date, args.database, args.term, args.number, total_found)
    print("Results logged to search_log.csv")

if __name__ == "__main__":
    main()
