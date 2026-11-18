class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

a = Node("Budi")
b = Node("Sari")
c = Node("Dedi")

a.next = b
b.next = c

sekarang = a
while sekarang:
    print(sekarang.nama, end=" -> ")
    sekarang = sekarang.next
print("None")