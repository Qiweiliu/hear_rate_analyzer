import numpy as np


class Validator:

    def get_percentage_similarity(self, operand_a, operand_b):
        operand_a = np.median(operand_a)
        operand_b = np.median(operand_b)
        similarity = abs(operand_a - operand_b) \
                     / ((operand_a + operand_b) / 2)
        similarity = np.around(similarity, decimals=6)
        return similarity

    def validate(self, result, ground_truth):
        percentage_difference = {}
        for key, content in result.items():
            similarity = self.get_percentage_similarity(
                np.array(content),
                np.array(ground_truth[key])
            )
            percentage_difference[key] = similarity
        return percentage_difference
