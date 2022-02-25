class IteravelPalavras:
    def __init__(self, palavras):
        self.palavras = palavras

    def __iter__(self):
        for palavra in self.palavras:
            yield palavra


palavras = ["python", "javascript", "elixir", "rust"]
iteravel_palavras = IteravelPalavras(palavras)

for palavra in iteravel_palavras:
    print(palavra)

# python
# javascript
# elixir
# rust
