class IteravelPalavras:
    def __init__(self, palavras):
        self.palavras = palavras

    def __iter__(self):
        return IteradorPalavras(self.palavras)


class IteradorPalavras:
    def __init__(self, palavras):
        self.palavras = palavras
        self.index = 0

    def __next__(self):
        try:
            palavra = self.palavras[self.index]
        except IndexError:
            raise StopIteration()

        self.index += 1
        return palavra

    def __iter__(self):
        return self


palavras = ["python", "javascript", "elixir", "rust"]
iteravel_palavras = IteravelPalavras(palavras)

for palavra in iteravel_palavras:
    print(palavra)

# python
# javascript
# elixir
# rust
