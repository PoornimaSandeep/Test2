class super_market:
      veg = {'tamoto': 100, "Brinjal": 50, "Onion": 120}
      fruits = {'Mango': 100, "Orange": 40, "Grapes": 60}
      grains = {"chana dhal": 200, "Groundnut": 100, "otas": 300, "Rice": 120}
      cart={}



      def bill(self):
          i=0
          while(i<1):
              item = input("which item you are want type veg,fruits ,grains: ")
              v=0
              while(v<1):
                  if item == "veg":
                      print(super_market.veg)
                      product = input("Enter the product")
                      for i, j in super_market.veg.items():
                          if i == product:
                              price = j
                      super_market.cart[i] = j
                      v=int(input("you want more veg please give 0 else 1"))

              f=0
              while(f<1):
                  if item == "fruits":
                      print(super_market.fruits)
                      product = input("Enter the product")
                      for i, j in super_market.fruits.items():
                          if i == product:
                              price = j
                      super_market.cart[i] = j
                      f = int(input("you want more veg please give 0 else 1"))
                      # print(product, price)
              g=0
              while(g<0):
                  if item == 'grains':
                      print(super_market.grains)
                      product = input("Enter the product")
                      for i, j in super_market.grains.items():
                          if i == product:
                              price = j
                      super_market.cart[i] = j
                      g = int(input("you want more veg please give 0 else 1"))
                      # print(product, price)
              print(super_market.cart)



sp=super_market()
sp.bill()


