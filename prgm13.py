class Card:
      def _init_(self,imageURL,price,rating,description,deliverywithin,comments,brandname):
          self.imageURL=imagrURL
          self.price=price
          self.rating=rating
          self.description=description
          self.delivarywithin=deliverywithin
          self.comments=comments
          self.brandname=brandname
          def printalldetails(self):
              print("product brand is:",self.brandname)
              print("product price is:",self.price)
              print("product rating is:",self.rating)

#object creation
commentsforlaptop = ["This is good","okay","Not good"]
laptop = Card("dummy-URL-1",45000,4.5,"This is a performant laptop","5 days",commentsforlaptop,"samsung")
laptop.printalldetils()
 #print(laptop.imageURL)
 #print(laptop.price)
 #print(laptop.rating)
 #print(laptop.description)

