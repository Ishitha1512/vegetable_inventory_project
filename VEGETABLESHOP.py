veg=['brinjal','potato','onion','tomato','chilli','ladiesfinger','jerkin','carrot','beetroot','cabbage','cauliflower','radish','capsicum','sweetcorn','coriander']
quantity=[10,30,30,30,40,15,15,20,5,5,7,8,12,9,10]
price=[65,25,20,18,10,30,35,40,30,20,20,60,35,20,10]
cprice=[60,20,15,15,7,25,25,30,25,13,12,53,27,12,5]
profit=[]
l=len(veg)
for i in range(l):
     d = price[i]-cprice[i]
     profit.append(d)
users=[]
day_items=[]
day_qty=[]
day_amt=[]
day_profit=[]
while True:
    login=input('1.Admin\n2.User\n3.Exit\n Choose your option:')
    if login=='1':
         while True:
             option=input('What do you want to do?: \n 1.Inventory management\n 2. Reports\n 3.View customers\n 4.Exit\n Choose your option:')
             match(option):
                         case '1':
                              while True:
                                   im=input('Inventory management:\n 1.add item\n 2.update item\n 3.remove item\n 4.view inventory\n 5.Exit\n Choose your option:')
                                   match(im):
                                          case '1':
                                              item=input("Enter item:")
                                              veg.append(item)
                                              qty=float(input("Enter Quantity:"))
                                              quantity.append(qty)
                                              p=float(input("Enter price:"))
                                              price.append(p)
                                              cp=float(input("Enter cost price:"))
                                              cprice.append(cp)
                                              pf=p-cp
                                              profit.append(pf)
                                              print(f'{item} added to inventory..')
                                          case '2':
                                              item=input('Enter item you want to update:')
                                              idx=veg.index(item)
                                              opt=input('Do you want to update:\n 1.quantity\n 2.price\n 3.costprice\n Enter your option:')
                                              match(opt):
                                                   case '1':
                                                      q=input('Do you want to add(1) or subtract?(2)')
                                                      if q=='1':
                                                          qty=float(input('How many kgs to add:'))
                                                          quantity[idx]+=qty
                                                      elif q=='2':
                                                          qty=float(input('How many kgs to subtract:'))
                                                          quantity[idx]-=qty 
                                                      else:
                                                           print('Invalid option')
                                                           
                                                   case '2':
                                                      p=float(input('Enter new price:'))
                                                      price[idx]=p
                                                      profit[idx]=p-cprice[idx]
                                                   case '3':
                                                      cp=float(input('Enter new cost price:'))
                                                      cprice[idx]=cp
                                                      profit[idx]=price[idx]-cp
                                                   case _:
                                                        print('Invalid option')
                                              print(f'{item} updated successfully!')
                                                   
                                          case '3':
                                              item=input('Enter item you want to remove:')
                                              idx=veg.index(item)
                                              veg.remove(item)
                                              quantity.pop(idx)
                                              price.pop(idx)
                                              cprice.pop(idx)
                                              profit.pop(idx)
                                              print(f'{item} removed successfully!')
                                          case '4':
                                               print('='*10,'INVENTORY','='*10)
                                               print('ITEM',' '*9,'QTY',' '*2,'PRICE')
                                               for i in zip(veg,quantity,price):
                                                    print(f"{i[0]: <15}{i[1]: <5}{i[2]: <5}")
                                               print('='*40)
                                          case '5':
                                               break
                                          case _:
                                              print('Invalid option.')
                         
                         case '2':
                              while True:
                                   re=input('Reports:\n 1.day report\n 2.revenue report\n 3.itemized profit\n 4.Exit\n Choose your option:')
                                   for i in day_items:
                                        x=veg.index(i)
                                        y=day_items.index(i)
                                        pro=day_qty[y]*profit[x]
                                        day_profit.append(pro)
                                   match(re):
                                      case '1':
                                           print('='*15,'DAY REPORT','='*15)
                                           print('='*10,'SOLD ITEMS','='*10)
                                           print('ITEM',' '*9,'QTY',' PRICE')
                                           for i in zip(day_items,day_qty,day_amt):
                                              print(f"{i[0]: <15}{i[1]: <5}{i[2]: <5}")
                                           print('='*40)
                                           total=sum(day_amt)
                                           print('Total amout collected:',' '*5,total)
                                           print('='*40)
                                           print('='*10,'ITEMS NOT SOLD','='*10)
                                           for i in veg:
                                               if i not in day_items:
                                                   print(i)
                                           print('='*40)
                                      case '2':
                                           print('='*15,'REVENUE REPORT','='*15)
                                           total=sum(day_amt)
                                           d_profit=sum(day_profit)
                                           print('Total Revenue:',total)
                                           print('Total profit:',d_profit)
                                           print('='*40)
                                      case '3':
                                           print('='*15,'ITEMIZED PROFIT REPORT','='*15)
                                           print('ITEM',' '*9,'QTY',' PROFIT')
                                           for i in zip(day_items,day_qty,day_profit):
                                               print(f"{i[0]: <15}{i[1]: <5}{i[2]: <5}")
                                           print('='*40)
                                           total=sum(day_profit)
                                           print('Total profit:',' '*10,total)
                                           print('='*40)

                                      case '4':
                                           break
                                      case _:
                                          print('Invalid option')
                                          

                         case '3':
                              print('='*10,'CUSTOMER LIST','='*10)
                              for i,j in enumerate(users):
                                   print(i+1,j)
                              print('='*40)
                         case '4':
                              break
                         case _:
                                  print('Invalid option')
             
          
    if login=='2':
             user=input('Enter your name:')
             if user not in users:
                    users.append(user)
             cart_items=[]
             cart_qty=[]
             cart_price=[]

             while True:
                 opt=input(' 1.View products\n 2.Add to cart\n 3.update cart items\n 4.delete cart items\n 5.Billing\n 6.View cart\n 7.Exit\n Choose your option:')

                 match(opt):

                      case '1':
                           print('='*10,'PRODUCTS','='*10)
                           print('ITEM',' '*9,'QTY',' '*2,'PRICE')
                           for i in zip(veg,quantity,price):
                              print(f"{i[0]: <15}{i[1]: <5}{i[2]: <5}")
                           print('='*40)
                      case '2':
                           item=input("What do you want?")

                           if item in veg:
                               qty=float(input('How many kgs do you want?'))
                               idx=veg.index(item)
                               if qty<=quantity[idx]:
                                   amt=qty*price[idx]
                                   quantity[idx]-=qty
                                   cart_items.append(item)
                                   cart_qty.append(qty)
                                   cart_price.append(amt)
                                   print(f"{item} is added to cart!")
                               else:
                                   print(f"Insufficient inventory, only {quantity[idx]} kgs available.")
                           else:
                               print("Item not available.")
                      case '3':
                           item=input('Enter item you want to update')
                           idx=cart_items.index(item)
                           x=veg.index(item)
                           q=input('Do you want to add(1) or subtract(2) quantity')
                           if q=='1':
                               qty=float(input('How many kgs to add:'))
                               cart_qty[idx]+=qty
                               quantity[x]-=qty
                               cart_price[idx]=cart_qty[idx]*price[x]
                               print('Item successfully updated!')
                           elif q=='2':
                              qty=float(input('How many kgs to subtract:'))
                              cart_qty[idx]-=qty 
                              quantity[x]+=qty
                              cart_price[idx]=cart_qty[idx]*price[x]
                              print('Item successfully updated!')
                           else:
                               print('Invalid option')
                           
                                                                              
                      case '4':
                           item=input('Enter item to remove:')
                           x=cart_items.index(item)
                           cart_items.pop(x)
                           cart_qty.pop(x)
                           cart_price.pop(x)
                           print(f'{item} is successfully removed!')
                      case '5':
                           if len(cart_items)>0:
                                   print("Generating bill...")
                                   print('='*10,'VEGETABLE SHOP','='*15)
                                   for i in zip(cart_items,cart_qty,cart_price):
                                       print(f"{i[0]: <15}{i[1]: <5}{i[2]: <5}")
                                   print('='*37)
                                   total=sum(cart_price)
                                   print('Total:',' '*12,total)
                                   for  i in cart_items:
                                       idx=cart_items.index(i)
                                       if i not in day_items:
                                           day_items.append(i)
                                           day_qty.append(cart_qty[idx])
                                           day_amt.append(cart_price[idx])
                                       else:
                                           d=day_items.index(i)
                                           day_qty[d]+=cart_qty[idx]
                                           day_amt[d]+=cart_price[idx]
                           cart_items.clear()
                           cart_qty.clear()
                           cart_price.clear()
                      case '6':
                           print('='*10,'CART','='*10)
                           print('ITEM',' '*9,'QTY',' '*2,'PRICE')
                           for i in zip(cart_items,cart_qty,cart_price):
                              print(f"{i[0]: <15}{i[1]: <5}{i[2]: <5}")
                           print('='*40)
                      case '7':
                           break
                      case _:
                           print('Invalid option')

                 
    if login=='3':
        break
        
