def add_tuple(tuple_a=(), tuple_b=()):
    # tuple_a üçün çatışmayan elementləri 0 ilə tamamlayırıq
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0

    # tuple_b üçün çatışmayan elementləri 0 ilə tamamlayırıq
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    # İki tuple-in ilk iki elementini toplayıb yeni tuple qaytarırıq
    return (a1 + b1, a2 + b2)
