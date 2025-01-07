class MultipleFunctions:
    def Subfields():
        print("""
            Sub-fields in AI are:
            Machine Learning
            Neural Networks
            Vision
            Robotics
            Speech Processing
            Natural Language Processing
            """)

    def OddEven():
        x=int(input("Enter a number:"))
        if (x%2 == 0):
            print(x," is Even number")
        else:
            print(x," is Odd number")


    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if ( gender.lower() == 'male' ):
            if ( age >= 21 ):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif( gender.lower() == 'female' ):
            if ( age >= 18 ):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            print("Kindly provide proper gender value")
            

    def percentage():
        s1=int(input("Subject1="))
        s2=int(input("Subject2="))
        s3=int(input("Subject3="))
        s4=int(input("Subject4="))
        s5=int(input("Subject5="))
        total= s1 + s2 + s3 + s4 + s5 
        percentage = ( total/500 ) * 100
        print("Total :",total)
        return(print("percentage :",format(percentage, ".14f")))

    def triangle():
        s1=int(input("Height:"))
        s2=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        area_of_triangle=(s1*s2)/2
        print("area_of_triangle=",area_of_triangle)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b1=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", h1+h2+b1 )

    