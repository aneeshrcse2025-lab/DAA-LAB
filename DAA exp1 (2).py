import random

def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    matches, comparisons = [], 0
    
    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            matches.append(i)
            
    return matches, comparisons

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length, i = 0, 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
            
    return lps

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    matches, comparisons = [], 0
    i = j = 0
    
    while i < n:
        if pattern[j] == text[i]:
            comparisons += 1
            i += 1
            j += 1
            if j == m:
                matches.append(i - j)
                j = lps[j - 1]
        else:
            comparisons += 1
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return matches, comparisons

def rabin_karp(text, pattern, q=101):
    n, m = len(text), len(pattern)
    d = 256
    h = pow(d, m - 1, q)
    p_hash = 0
    t_hash = 0
    matches, comparisons = [], 0
    
    if n < m:
        return matches, comparisons

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
        
    for s in range(n - m + 1):
        comparisons += 1  # Increment for hash comparison
        if p_hash == t_hash:
            match = True
            for k in range(m):
                if text[s + k] != pattern[k]:
                    match = False
                    break
            if match:
                matches.append(s)
                
        if s < n - m:
            # Added + q safety inside formula
            t_hash = (d * (t_hash - ord(text[s]) * h + q) + ord(text[s + m])) % q
                
    return matches, comparisons

def performance_comparison():
    random.seed(42)
    text_large = ''.join(random.choices('ABCD', k=10000))
    patterns = ['AB', 'ABCD', 'ABCDAB', 'ABCDABCD']
    
    print(f'\n{"Pattern":>12} {"Naive":>10} {"KMP":>10} {"RK (Hashes)":>12}')
    print('-' * 49)
    
    for p in patterns:
        _, c1 = naive_search(text_large, p)
        _, c2 = kmp_search(text_large, p)
        _, c3 = rabin_karp(text_large, p)
        print(f'{p:>12} {c1:>10} {c2:>10} {c3:>12}')

if __name__ == "__main__":
    text = 'AABAACAADAABAABA'
    pattern = 'AABA'
    
    print(f'Text: {text}')
    print(f'Pattern: {pattern}')
    
    m1, c1 = naive_search(text, pattern)
    m2, c2 = kmp_search(text, pattern)
    m3, c3 = rabin_karp(text, pattern)
    
    print(f'\nNaive -> Matches at: {m1}, Comparisons: {c1}')
    print(f'KMP   -> Matches at: {m2}, Comparisons: {c2}')
    print(f'RK    -> Matches at: {m3}, Hash Matches/Ops: {c3}')
    
    performance_comparison()