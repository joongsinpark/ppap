

list = ["id", "type",
    "author",
    "title",
    "time",
    "numRecommend",
    "numClick",
    "shopLink",
    "affLink",
    "mainText",
    "product_inf",
    "price",
    "deliveryPrice",
    "mall",
    "done"]


string = "def get%s(self): return self.%s\ndef set%s(self, %s): self.%s = %s"


for i in list:
    print (string %(i.capitalize(),i,i.capitalize(),i,i,i))
