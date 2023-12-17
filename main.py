
from transformers import pipeline

classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")

while True:
    s = input("Введите строку (exit для выхода): ")
    if s == "exit":
        break

    c = classifier(s)[0]

    if c["label"] in {"POSITIVE", "NEGATIVE", "NEUTRAL"} and c["score"] > 0.7:
        if c["label"] == "POSITIVE":
            res = "тональность текста положительная"
        elif c["label"] == "NEGATIVE":
            res = "тональность текста негативная"
        else:
            res = "тональность текста нейтральная"
    else:
        res = "не удалось определить тональность текста"

    print(f"{res}")
