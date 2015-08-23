__author__ = 'SekthDroid'


class StringCalculator(object):
    def add(self, param):
        if not param:
            return 0

        delimiter = ","
        if self.contains_different_delimiter(param):
            delimiter = param[2]
            param = self.remove_delimiter_line(delimiter, param)

        if self.contains_blank_lines(param):
            param = param.replace("\n", delimiter)

        if delimiter in param:
            numbers = self.fetch_numbers_with_delimiter(delimiter, param)
            self.raise_negative_errors_if_needed(numbers)

            return sum(numbers)

        return int(param)

    def contains_blank_lines(self, param):
        return "\n" in param

    def contains_different_delimiter(self, param):
        return "//" in param

    def remove_delimiter_line(self, delimiter, param):
        return param.replace("//" + delimiter + "\n", "")

    def fetch_numbers_with_delimiter(self, delimiter, param):
        return [int(i) for i in param.split(delimiter) if int(i) < 1001]

    def raise_negative_errors_if_needed(self, numbers):
        negatives = [str(i) for i in numbers if i < 0]
        if len(negatives) > 0:
            raise ValueError("negatives not allowed: %s" % ",".join(negatives))
