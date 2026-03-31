from math import sqrt


class CalculadoraService:

    @staticmethod
    def adicao(a:float, b:float) -> float:
        """ Soma dois números.

        Exemplo JSON:
            {
                "a": 1,
                "b": 1
            }

        resultado: 2
        """
        return a + b

    @staticmethod
    def subtracao(a:float, b:float) -> float:
        """ Subtrai dois números.
        
        Exemplo JSON:
            {
                "a": 1,
                "b": 1
            }

        resultado: 0
        """
        return a - b

    @staticmethod
    def multiplicacao(a:float, b:float) -> float:
        """ Multiplica dois números.
        
        Exemplo JSON:
            {
                "a": 2,
                "b": 2
            }

        resultado: 4
        """
        return a * b

    @staticmethod
    def divisao(a:float, b:float) -> float:
        """ Divide dois números.
        
        Exemplo JSON:
            {
                "a": 4,
                "b": 2
            }

        resultado: 2
        """
        if b == 0:
            raise ValueError("Divisão por zero não permitida")
        return a / b

    @staticmethod
    def potenciacao(a:float, b:float) -> float:
        """ Potência de um número.
        
        Exemplo JSON:
            {
                "a": 2,
                "b": 3
            }

        resultado: 8
        """
        return a ** b

    @staticmethod
    def raiz_quadrada(a:float) -> float:
        """ Raiz quadrada de um número.

        Exemplo JSON:
            {
                "a": 9
            }

        resultado: 3
        """
        if a < 0:
            raise ValueError("Raiz de número negativo não permitida")
        return sqrt(a)

    @staticmethod
    def porcentagem(tipo:int, porcentagem:float, valor:float) -> float:
        """ Porcentagem de um número.

        Exemplo JSON:
            {
                "tipo": 1,
                "porcentagem": 20,
                "valor": 100
            }

        resultado: 120
        """
        if tipo == 1:  # Acréscimo
            return valor + (valor * porcentagem/100)
        elif tipo == 2:  # Desconto
            return valor - (valor * porcentagem/100)
        else:
            raise ValueError("Tipo inválido. Use 1 (acréscimo) ou 2 (desconto)")