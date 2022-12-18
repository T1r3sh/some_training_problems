from itertools import compress


class Solution(object):

    """
    Solution class
    Contain solution of wrong paretheses issue
    """

    def is_valid(self, s: str) -> tuple[bool, str]:
        """Checking if parentheses is correctly placed

        Args:
            s (string): input string

        Returns:
            tuple(bool, str):   Tuple, first value is bool meaning if string is correct
                                second value is str pointing which parethese is incorrectly placed
        """
        openstack = []
        for char in s:
            if char == '(':
                openstack.append(char)
            elif char == ')':
                try:
                    openstack.pop()
                except IndexError:
                    return False, char
        if len(openstack) > 0:
            return False, '('
        return True, ''
    
    # new is slightly faster
    def new_search_char(self, s: str, char: str) -> list[int]:
        """New version of search algo. 

        Args:
            s (str): input string
            char (str): string to search in s string

        Returns:
            list[int]: all first indices of each char sequence in s string
        """
        idx = [i for i, x in enumerate(s) if x == char]
        out = []
        for i in idx:
            out.append(i)
            if len(out)>1 and out[-1]-out[-2] == 1:
                out.pop(-1)
        return out
    
    def search_char(self, s: str, char: str) -> list[int]:
        """ Searches for the first indices of char sequences in  string s
    
        Args:
            s (str): input string
            char (str): string to search in s string

        Returns:
            list[int]: all first indices of each char sequence in s string
        """
        idx = []
        for i, elem in enumerate(s):
            if elem == char:
                idx.append(i)
        dismap = [j-i for i, j in zip(idx[:-1], idx[1:])]
        out = [idx[0]]
        for p, dis in enumerate(dismap):
            if dis > 1:
                out.append(idx[p+1])
        return out

    def all_deletion_options(self, s: str, char: str) -> list[str]:
        """ Function that generate all possible options of deleting char string from s string

        Args:
            s (str): input string
            char (str): string to delete in s string

        Returns:
            list[str]: all possible options of deleting char string from s string
        """
        idx_s = self.new_search_char(s, char)
        res = [list(s[:]) for _ in range(len(idx_s))]
        for i, index_s in enumerate(idx_s):
            res[i][index_s] = ''
        return [''.join(i) for i in res]

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        valid_info = self.is_valid(s)
        if valid_info[0]:
            return [s]
        list_of_possible_solution = self.all_deletion_options(s, valid_info[1])
        correct_strings = list(
            compress(
                list_of_possible_solution,
                [self.is_valid(i)[0] for i in list_of_possible_solution]
            )
        )
        if correct_strings:
            return correct_strings
        for elem in list_of_possible_solution:
            new_val = self.removeInvalidParentheses(elem)
            correct_strings.extend(new_val)
        max_len = max(map(len, correct_strings))
        string_with_minimum_changes = filter(
            lambda x: len(x) == max_len, correct_strings)
        return list(dict.fromkeys(string_with_minimum_changes))
