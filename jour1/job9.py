def element_in_list(l, query):
    for element in l:
        if element == query:
            return True
    return False
l="plateforme"
query="e"
print(element_in_list(l, query))
