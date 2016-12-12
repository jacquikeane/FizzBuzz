import sys

class Error (Exception): pass

class ClassB:
    def __init__(self, max_number=100):
        self.max_number = max_number


    def _is_fizzy(self, number):
        return number % 3 == 0


    def _is_buzzy(self, number):
        return number % 5 == 0


    def _number_to_string(self, number):
        to_return = []

        if self._is_fizzy(number):
            to_return.append('Fizz')

        if self._is_buzzy(number):
            to_return.append('Buzz')
            
        if len(to_return) > 0:
            return ''.join(to_return)
        else:
            return str(number)


    def run(self, outfile=None):
        if outfile is None:
            f = sys.stdout
        else:
            try:
                f = open(outfile, 'w')
            except:
                raise Error('Error opening file ' + outfile)

        for i in range(1, self.max_number + 1, 1):
            print(self._number_to_string(i), file=f)

        if outfile is not None:
            f.close()

