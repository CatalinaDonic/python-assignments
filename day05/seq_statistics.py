def seq_statistics(fh):
    all_counts={'A':0, 'C':0, 'G':0,'T':0,'unknown':0}
    
    for f in fh:
        try:
            with open(f, 'r') as file:
                sequence=file.read().strip().upper()
                counts={'A':0, 'C':0, 'G':0,'T':0,'unknown':0}
                for character in sequence:
                    if character in counts:
                        counts[character] +=1
                    else:
                        counts['unknown'] +=1
                print(f"{f}")
                print_statistics(counts)
                for key in counts:
                    all_counts[key]+=counts[key]
        except FileNotFoundError:
            print(f"File {f} not found")

    print("All")
    print_statistics(all_counts)

def print_statistics(counts):
    total=sum(counts.values())
    for base in ['A', 'C', 'G', 'T', 'unknown']:
        count=counts.get(base,0)
        percentage=(count/total*100) if total>0 else 0
        print(f"{base}: {count:8d}{percentage:6.1f}%")
    print(f"Total: {total:8d}\n")
    
#Test on easy sequences to verify the results
if __name__=="__main__":
    seq_statistics(["day05/a_seq.txt", "day05/b_seq.txt"])