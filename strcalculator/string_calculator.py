__author__ = 'SekthDroid'


class StringCalculator(object):
    def add(self, param):
        if "," in param:
            numbers = param.split(",")
            result = sum([int(i) for i in numbers])
            return result

        if param:
            return int(param)

        return 0