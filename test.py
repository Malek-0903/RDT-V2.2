angeleA=eval(input("enter angeleA:"))
angeleB=eval(input("enter angeleB:"))
angeleC=-eval(input("enter angeleC:"))

if (angeleA+ angeleC+ angeleB != 180):
    print("the triangle is not valid")
   
else:       
        
if ( angeleA>90 or angeleB>90 or angeleC>90):
        print("the traingle is vaild")
        print("this angele is obtuse")
    
elif ( angeleA==90 or angeleB==90 or angeleC==90):
         print("the traingle is vaild")
         print("this angle is right")
    
elif ( angeleA<90 or angeleB<90 or angeleC<90):
        print("the traingle is vaild")
        print("this angle is acute")