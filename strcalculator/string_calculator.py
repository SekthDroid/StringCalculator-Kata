__author__ = 'SekthDroid'


class StringCalculator(object):
    def add(self, param):
        if "," in param:
            numbers = param.split(",")
            return int(numbers[0]) + int(numbers[1])

        if param:
            return int(param)
        return 0