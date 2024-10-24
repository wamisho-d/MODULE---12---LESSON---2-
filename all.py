# Advanced Operations on Python Lists

# Task 1: Creating a List of Squares Using List Comprehension
def squares_list(n):
    """
    Creates a list of squares of numbers from 1 to n using list comprehension

    :param n: The upper bound of the range (inclusive).
    :retuen: A list of squares from 1 to n.

    """

    return [i ** 2 for i in range(1, n + 1)]
# Example useage
print(squares_list(10)) 

# Time Complexity: O(n) Where n is the upper limit of the range.
# Space Complexity: O(n) because of the storage of the list of size n.

# Task 2: Reversing a Sublist Within a List
def reverse_sublist(lst, i, j):
    """
    Reverse a sublist within the list 1st from index i to j (inclusive).
    
    :param 1st: The list in which the sublist will be reversed.
    :param i: The starting index of the sublist.
    :param j: The ending index of the sublist.
    :return: The list with the sublist reversed.

    """
    lst[i:j+1] = lst[i:j+1][::-1]
    return lst

# Example usage
lst = [1, 2, 3, 4, 5, 6]
print(reverse_sublist(lst, 1, 4))  

# Time Complexity:  O(j - i + 1) because of slicing, reversing, reassigning the sublist.

# Space Complexity: O(j - i + 1) because of the additional space used for the sliced sublist.


# Task 3: Merging Two Sorted Lists
def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into s single sorted list.

    :param list1: The first sorted list.
    :param list2: The second sorted list.
    :return: A new sorted list containing all elements of list1 and list2.

    merged_list = [] # Initialize an empty list for the merged result
    i, j, = 0, 0 # initialize pointers for both lists

    # Traverse both lists and merge them
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j +=
    # Append any remaining elements from list1 or list2
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

    # Example usage
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]

    print(merge_sorted_lists(list1, list2)) # Output: [1, 2, 3, 4, 5, 6]

    """

# Time Complexity: O(n + m) where n and m are the lengths of list1 and list2 respectively

# Space Complexity: O(n + m) because of the creation of the new merged list.


# Dictionary Manipulation and Optimization

# Task 1: Merging two dictionaries
def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries. If there are common keys, values from the second dictionary are preserved.

    :param dict1: First dictionary
    :param dict2: Second dictionary
    :return: Merged dictionary
    """
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# Example Useage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dictionaries(dict1, dict2)) 

# Time Complexity: O(n + m) where n is the of dict1 and m is the size of dict2. Copying dict1 takes O(n), and updating it with dict2 takes O(n) and updating it with dict2 takes O(m).

# Space Complexity:  O(n + m) Since a new dictionary is created that contains the combined key-value pairs from both dictionaries.


# Task 2: Intersection of two dictionaries
def intersect_dictionaries(dict1, dict2):
    """
    Finds the intersections of two dictionaries. Returns a new dictionary containing keys common to both dictionaries.
    along with their values from the first dictionary.

    :param dict1: First dictionary
    :param dict2: Second dictionary
    :return: Dictionary containing common keys and their values
    """

    return {key: dict1[key] for key in dict1 if key in dict2}
    
# Example Useage: 
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
print(intersect_dictionaries(dict1, dict2))

# Time Complexity: O(n) where n is the size of dict1.  For each key in dict1, checking if it exists in dict2 is an O(1) operation because of hash table lookup.

# Space Complexity: O(k) where is the number of common keys, as a new dictionary is created to store the result.
   
    
# Task 3: Word frequncy counter
def word_frequency(words):
        """ 
        Counts the frequency of each unique word in a list using a dictionary.
        :param words: List of words
        :return: Dictionary with word frequencies
        """

        freq_dict = {}
        for word in words:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
        return freq_dict

 # Example Useage:
words_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'orange']
print(word_frequency(words_list))

# Time Complexity: O(n) where n is the number of words in the list. Each word is processed once, and dictionary updates(inserations or modifications) take O(1) time.

# Space Complexity: O(K) where k is the number of unique words in the list, as the dictionary stores the count for each unique word.

