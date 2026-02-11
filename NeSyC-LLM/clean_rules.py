import re
import sys

def clean_rules(input_path, output_path):
    with open(input_path, 'r') as f:
        lines = f.readlines()

    valid_rules = set()
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # 1. Must end with '.'
        if not line.endswith('.'):
            continue
            
        # 2. Balanced parentheses
        if line.count('(') != line.count(')'):
            continue
            
        # 3. Basic ASP safety checks (optional but good)
        if not line.startswith(':-'):
             # If it's a positive rule (head :- body), it's fine. 
             # But usually ILP rules here are constraints ':- ...' or definitions.
             # The existing file sample showed ':- ...'.
             # README says "discards all positive/effect rules" in the original code, 
             # but "Example of a valid rules file" shows mostly constraints ':- ...'.
             # Wait, the valid example shows ONLY ':- ...'.
             # But the known issue says "discards all positive/effect rules" is a BUG.
             # So we should ALLOW positive rules if they exist.
             pass

        valid_rules.add(line)

    sorted_rules = sorted(list(valid_rules))
    
    with open(output_path, 'w') as f:
        for rule in sorted_rules:
            f.write(rule + '\n')
    
    print(f"Cleaned rules. Kept {len(valid_rules)} unique valid rules out of {len(lines)} lines.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_rules.py <input_file> <output_file>")
        sys.exit(1)
    
    clean_rules(sys.argv[1], sys.argv[2])
