class SpellChecker:

    def __init__(self, database):
        self.database = database

    def levenshtein_distance(self, first_string, second_string):
        number_of_rows = len(second_string) + 1
        number_of_cols = len(first_string) + 1
        matrix = self.make_matrix(number_of_rows, number_of_cols)
        for i in range(1, number_of_rows):
            for j in range(1, number_of_cols):
                if first_string[j - 1] == second_string[i - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                else:
                    matrix[i][j] = min(
                        matrix[i - 1][j], 
                        matrix[i - 1][j - 1], 
                        matrix[i][j - 1]
                    ) + 1
                    
        return matrix[number_of_rows - 1][number_of_cols - 1]


    def make_matrix(self, number_of_rows, number_of_cols):
        matrix = [
            [0 for x in range(number_of_cols)] 
            for y in range(number_of_rows)
        ]
        for row in matrix:
            for num in row:
                num = 0
        i = 0
        for col in matrix[0]:
            matrix[0][i] = i
            i += 1
        i = 0
        for row in matrix:
            row[0] = i
            i += 1
        return matrix


    def check(self, word, ignorance=0.34):
        """
        :param ignorance: Number of allowed mistakes per character
        """
        maxdistance = len(word) * ignorance + 1
        result = []
        for item in self.database:
            distance = self.levenshtein_distance(word, item)
            if distance <= maxdistance:
                result.append(item)

        return result
