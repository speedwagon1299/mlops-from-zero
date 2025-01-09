import wikipedia

def scrape(name):
    result = wikipedia.summary(name, sentences=1)
    return result

print(scrape("Microsoft"))