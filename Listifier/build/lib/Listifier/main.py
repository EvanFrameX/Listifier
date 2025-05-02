import random
import ctypes
from typing import Any, Callable, Dict, List, Tuple

# ========================
# 1. SHUFFLING & RANDOMNESS
# ========================


def recursive_shuffle(lst: List[Any]) -> List[Any]:
    """Ultra-shuffles a list using recursive random merging"""
    if len(lst) <= 1:
        return lst.copy()
    mid = len(lst) // 2
    return random_merge(recursive_shuffle(lst[:mid]),
                        recursive_shuffle(lst[mid:]))


def random_merge(a: List[Any], b: List[Any]) -> List[Any]:
    """Merges two lists with coin-flip randomness"""
    merged = []
    while a and b:
        merged.append(a.pop(0) if random.choice([True, False]) else b.pop(0))
    return merged + a + b


def fractal_shuffle(lst: List[Any], depth: int = 3) -> List[Any]:
    """Shuffles at multiple recursion levels"""
    if depth == 0 or len(lst) <= 1:
        return lst.copy()
    random.shuffle(lst)
    mid = len(lst) // 2
    return fractal_shuffle(lst[:mid], depth - 1) + fractal_shuffle(
        lst[mid:], depth - 1)


def recursive_roulette(lst: List[Any], depth: int = 0) -> List[Any]:
    """Creates nested random partitions with transformations"""
    if len(lst) <= 1 or depth > 3:
        return lst

    split_prob = random.uniform(0.25, 0.75)
    group_a, group_b = [], []

    for item in lst:
        if isinstance(item, list):
            processed = recursive_roulette(item, depth + 1)
            (group_a
             if random.random() < split_prob else group_b).append(processed)
        else:
            (group_a if random.random() < split_prob else group_b).append(item)

    transformations = [
        lambda x: x, lambda x: x[::-1],
        lambda x: sorted(x, key=lambda k: random.random()),
        lambda x: x + [random.randint(0, 100)]
    ]

    return [
        random.choice(transformations)(recursive_roulette(group_a, depth + 1)),
        random.choice(transformations)(recursive_roulette(group_b, depth + 1))
    ]


# ========================
# 2. SORTING & ORDERING
# ========================


def recursive_reverse_sort(lst: List[Any]) -> List[Any]:
    """Merge sort implementation returning descending order"""
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    return reverse_merge(recursive_reverse_sort(lst[:mid]),
                         recursive_reverse_sort(lst[mid:]))


def reverse_merge(a: List[Any], b: List[Any]) -> List[Any]:
    """Merges two sorted lists in descending order"""
    merged = []
    while a and b:
        merged.append(a.pop(0) if a[0] > b[0] else b.pop(0))
    return merged + a + b


def chaos_sort(lst: List[Any], threshold: float = 0.3) -> List[Any]:
    """Randomly chooses to sort or shuffle sublists"""
    if len(lst) <= 1:
        return lst.copy()
    if random.random() < threshold:
        random.shuffle(lst)
        return lst
    mid = len(lst) // 2
    return chaos_sort(lst[:mid], threshold) + chaos_sort(lst[mid:], threshold)


def recursive_quick_sort(lst: List[Any]) -> Any:
    '''custom function using the .sort() method'''
    return lst.sort()


def low_high_sort(lst: List[Any], reverse: bool = False) -> List[Any]:
    '''sorts the list from lowest to highest'''
    sample = lst.copy()
    if not reverse:
        sample.sort()
    else:
        sample.sort(reverse=True)

    return sample


# ========================
# 3. LIST STRUCTURE OPERATIONS
# ========================


def recursive_flatten(lst: List[Any]) -> List[Any]:
    """Turns nested lists into a flat list"""
    if not isinstance(lst, list):
        return [lst]
    return [item for sublist in lst for item in recursive_flatten(sublist)]


def recursive_subsets(lst: List[Any]) -> List[List[Any]]:
    """Generates all possible subsets (power set)"""
    if not lst:
        return [[]]
    head, *tail = lst
    tail_subsets = recursive_subsets(tail)
    return tail_subsets + [[head] + subset for subset in tail_subsets]


def recursive_chunk(lst: List[Any], size: int) -> List[List[Any]]:
    """Splits list into chunks of specified size"""
    if not lst:
        return []
    return [lst[:size]] + recursive_chunk(lst[size:], size)


def recursive_rotate(lst: List[Any], n: int) -> List[Any]:
    """Rotates list right by n positions"""
    if n == 0 or not lst:
        return lst.copy()
    return recursive_rotate(lst[-1:] + lst[:-1], n - 1)


# ========================
# 4. ELEMENT OPERATIONS
# ========================


def get_element_ids(lst: List[Any]) -> List[Tuple[int, int]]:
    """Returns memory addresses with indices"""

    def _mapper(sub, acc, idx):
        return acc if not sub else _mapper(sub[1:], acc +
                                           [(id(sub[0]), idx)], idx + 1)

    return _mapper(lst, [], 0)


def recursive_replace(lst: List[Any], condition: Callable[[Any], bool],
                      replacement: Any) -> List[Any]:
    """Replaces elements matching condition"""
    if not lst:
        return []
    head = replacement if condition(lst[0]) else lst[0]
    return [head] + recursive_replace(lst[1:], condition, replacement)


def recursive_insert(lst: List[Any], index: int, element: Any) -> List[Any]:
    """Inserts element at position recursively"""
    if index <= 0:
        return [element] + lst
    if not lst:
        return [element]
    return [lst[0]] + recursive_insert(lst[1:], index - 1, element)


# ========================
# 5. LIST ANALYSIS
# ========================


def recursive_frequency(lst: List[Any]) -> Dict[Any, int]:
    """Counts element frequencies"""
    if not lst:
        return {}
    head, *tail = lst
    counts = recursive_frequency(tail)
    counts[head] = counts.get(head, 0) + 1
    return counts


def list_fingerprint(lst: List[Any]) -> int:
    """Creates hash combining element IDs and values"""
    if not lst:
        return 0
    head, *tail = lst
    return hash((id(head), hash(head), list_fingerprint(tail)))


def are_permutations(a: List[Any], b: List[Any]) -> bool:
    """Checks if two lists are permutations"""
    if len(a) != len(b):
        return False
    if not a:
        return True
    try:
        idx = b.index(a[0])
    except ValueError:
        return False
    return are_permutations(a[1:], b[:idx] + b[idx + 1:])


# ========================
# 6. SPECIALIZED OPERATIONS
# ========================


def recursive_interleave(a: List[Any], b: List[Any]) -> List[Any]:
    """Merges two lists by alternating elements"""
    if not a and not b:
        return []
    return (([a[0]] if a else []) + ([b[0]] if b else []) +
            recursive_interleave(a[1:], b[1:]))


def recursive_zip(a: List[Any], b: List[Any]) -> List[Tuple[Any, Any]]:
    """Recursive implementation of zip(a, b)"""
    if not a or not b:
        return []
    return [(a[0], b[0])] + recursive_zip(a[1:], b[1:])


def recursive_rle(lst: List[Any]) -> List[Tuple[Any, int]]:
    """Run-length encoding (compresses consecutive duplicates)"""
    if not lst:
        return []
    count = 1
    while count < len(lst) and lst[count] == lst[0]:
        count += 1
    return [(lst[0], count)] + recursive_rle(lst[count:])


### ======================
### LIST GENERATION
### ======================


def recursive_generator(id: Any) -> List[Any]:
    """Generates a list based on a given ID"""
    if id == 0:
        return []
    if id == 1:
        return [1]
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return list(id(sample) + recursive_generator(id - 1))


def recursive_binary_tree(lst: List[Any]) -> List[Any]:
    sample: list[Any] = []
    binary: dict = {
        'a': '000000',
        'b': '000001',
        'c': '000010',
        'd': '000011',
        'e': '000100',
        'f': '000101',
        'g': '000110',
        'h': '000111',
        'i': '001000',
        'j': '001001',
        'k': '001010',
        'l': '001011',
        'm': '001100',
        'n': '001101',
        'o': '001110',
        'p': '001111',
        'q': '010000',
        'r': '010001',
        's': '010010',
        't': '010011',
        'u': '010100',
        'v': '010101',
        'w': '010110',
        'x': '010111',
        'y': '011000',
        'z': '011001'
    }

    for e in lst:
        if e in binary:
            sample.append(binary[lst])
        else:
            sample.append(id(e))
    return sample


def recursive_creator(lst: List[Any], key: Any) -> Any:
    sample: list[Any] = []
    sample2: list[Any] = []
    sample3: list[Any] = []
    for e in lst:
        sample.append(id(e))
    sample2 = sample[::-1]
    for e in sample2:
        sample3.append(ctypes.cast(e, ctypes.py_object).value)
    return sample3


### ======================
### LIST HANDLING
### ======================


def recursive_search(lst: List[Any], target: Any) -> Any:
    for e in lst:
        if e == target:
            return e
        else:
            return f'element {target} not found in array {lst}'


def recursive_unique(lst: List[Any]) -> List[Any]:
    return list(set(lst))


def recursive_sum(lst: List[int | float]) -> Any:
    sample: float = 0.0
    for e in lst:
        if isinstance(e, int | float):
            return f'failed to sum array {lst}'
        else:
            sample += e
    return sample


def recursive_element(lst: List[Any], key: Any) -> Any:
    sample: list[Any] = []
    for e in lst:
        sample.append(type(e))
    return sample


def recursive_type(lst: List[Any], key: Any) -> Any:
    sample: list[Any] = []
    for e in lst:
        sample.append(type(e))
    return sample


def recursive_filter(lst: List[Any], key: Any, should: bool) -> Any:
    sample: list[Any] = []
    for e in lst:
        if isinstance(e, key) and should:
            sample.append(e)


def recursive_assigner(lsta: List[Any], lstb: List[Any]) -> dict[Any, Any]:
    sample: dict[Any, Any] = {}
    for e in lsta:
        for f in lstb:
            if e == f:
                sample.update({e: f})
    return sample


def recursive_intersection(lsta: List[Any], lstb: List[Any]) -> List[bool]:
    sample: list[bool] = []
    for e in lsta:
        for f in lstb:
            sample.append(e == f)
    return sample
