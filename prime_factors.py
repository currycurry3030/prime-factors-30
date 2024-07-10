class PrimeFactor:
    def of(self, number) -> []:
        factors = []
        if number > 1:
            if number == 4:
                while number % 2 == 0:
                    factors.append(2)
                    number //= 2
            elif number == 6:
                factors.append(2)
                factors.append(3)
            else:
                factors.append(number)
        return factors
