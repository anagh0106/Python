print("".center(50,'-'),"Welcome To Our Hotel".center(50),"".center(50,'-'),sep='\n')
total: int=0
while True:
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Dinner")
    print("4. Desserts")
    print("5. Beverages")
    print("6. Exit")
    print("0. Print Bills")

    choice=int(input("Enter Your Choice -> "))

    match choice:
        case 1:
            print("\n--- Breakfast menu ---")
            print("1. Pancakes - Rs.30")
            print("2. French Toast - Rs.50")
            print("3. Coffee - Rs.10")
            print("4. Back To Main Menu")
            choice = int(input("Please select any option: "))
            match choice:
                case 1:
                    qty = int(input("How much qty of pancakes you want? -> "))
                    total+=qty * 30
                case 2:
                    qty = int(input("How much qty of french toast you want? -> "))
                    total+=qty * 50
                case 3:
                    qty = int(input("How much qty of coffee you want? -> "))
                    total+=qty * 10
                case 4:
                    continue
                case _:
                    print("Sorry! this item is not available for now...")
        case 2:
            print("\n--- Lunch menu ---")
            print("1. Punjabi Unlimited - Rs.360")
            print("2. Gujarati Unlimited - Rs.320")
            print("3. South Indian Unlimited - Rs.340")
            print("4. Go Back To Main Menu")
            choice = int(input("Please select any option: "))
            match choice:
                case 1:
                    qty = int(input("How much qty of Punjabi Dish you want? -> "))
                    total+=qty * 360
                case 2:
                    qty = int(input("How much qty of Gujarati Dish you want? -> "))
                    total+=qty * 320
                case 3:
                    qty = int(input("How much qty of South Indian Dish you want? -> "))
                    total+=qty * 340
                case 4:
                    continue
                case _:
                    print("Sorry! this item is not available for now...")
        case 3:
            print("\n--- Dinner menu ---")
            print("1. Italian Special - Rs.450")
            print("2. Mexican Feast - Rs.400")
            print("3. Chinese Delight - Rs.420")
            print("4. Back To Main Menu")
            choice = int(input("Please select any option: "))
            match choice:
                case 1:
                    qty = int(input("How much qty of Italian Dish you want? -> "))
                    total+=qty * 450
                case 2:
                    qty = int(input("How much qty of Mexican Dish you want? -> "))
                    total+=qty * 400
                case 3:
                    qty = int(input("How much qty of Chinese Dish you want? -> "))
                    total+=qty * 420
                case 4:
                    continue
                case _:
                    print("Sorry! this item is not available for now...")
        case 4:
            print("\n--- Desserts menu ---")
            print("1. Chocolate Lava Cake - Rs.150")
            print("2. Gulab Jamun - Rs.120")
            print("3. Ice Cream Sundae - Rs.180")
            print("4. Back To Main Menu")
            choice = int(input("Please select any option: "))
            match choice:
                case 1:
                    qty = int(input("How much qty of Chocolate Lava Cake you want? -> "))
                    total+=qty * 150
                case 2:
                    qty = int(input("How much qty of Gulab Jamun you want? -> "))
                    total+=qty * 120
                case 3:
                    qty = int(input("How much qty of Ice Cream Sundae you want? -> "))
                    total+=qty * 180
                case 4:
                    continue
                case _:
                    print("Sorry! this item is not available for now...")

        case 5:
            print("\n--- Beverages menu ---")
            print("1. Cold Coffee - Rs.120")
            print("2. Lemon Iced Tea - Rs.100")
            print("3. Fresh Lime Soda - Rs.80")
            print("4. Back To Main Menu")
            choice = int(input("Please select any option: "))
            match choice:
                case 1:
                    qty = int(input("How much qty of Cold Coffee you want? -> "))
                    total+=qty * 120
                case 2:
                    qty = int(input("How much qty of Lemon Iced Tea you want? -> "))
                    total+=qty * 100
                case 3:
                    qty = int(input("How much qty of Fresh Lime Soda you want? -> "))
                    total+=qty * 80
                case 4:
                    continue
                case _:
                    print("Sorry! this item is not available for now...")
        case 0:
            print(f"Your Total Bill Is {total}")
        case _:
            print("Enter Valid Choice")
            break
