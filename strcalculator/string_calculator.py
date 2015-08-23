__author__ = 'SekthDroid'


class StringCalculator(object):
    def add(self, param):
        delimiter = ","
        if "//" in param:
            delimiter = str(param)[2]
            param = str(param).replace("//" + delimiter + "\n", "")

        if "\n" in param:
            param = param.replace("\n", delimiter)

        if delimiter in param:
            numbers = param.split(delimiter)
            result = sum([int(i) for i in numbers])
            return result

        if param:
            return int(param)

        return 0