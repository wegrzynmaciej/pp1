def miesiac(n):
    if n < 1 or n > 12:
        return 'Błędny argument'
    nazwy = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec',
             'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień']
    return nazwy[n - 1]
