__author__ = 'SekthDroid'


class StringCalculator(object):
    def remove_delimiter_line(self, delimiter, param):
        return param.replace("//" + delimiter + "\n", "")

    def add(self, param):
        delimiter = ","
        if "//" in param:
            delimiter = param[2]
            param = self.remove_delimiter_line(delimiter, param)

        if "\n" in param:
            param = param.replace("\n", delimiter)

        if delimiter in param:
            numbers = param.split(delimiter)
            negatives = [int(i) for i in numbers if int(i) < 0]
            if len(negatives) > 0:
                raise ValueError("negatives not allowed: %s" % ",".join(numbers))
            result = sum([int(i) for i in numbers])
            return result

        if param:
            return int(param)

        return 0