import pickle
import os
# import time

UI = '''
1. Add new dish
2. Delete dish
3. View dishes
4. Update dish
5. Search
6. Reset all
7. Exit
'''

UI2 = '''
1. Filter by prep time.
2. Filter by ingredient.
3. Filter by dish first letter.
4. Search by dish name. 
5. Exit
'''

class Dish:
    #These are the properties on the Dish Class (name)
    def __init__(self, dishName, prepTime, ingredients):
        self.dishName = dishName
        self.prepTime = prepTime
        self.ingredients = ingredients

    #how the dishes are displayed (come back and fix spacing if needed)
    def __str__(self):
        return "{:<25} {:<20} {:<20}".format(self.dishName, self.prepTime, self.ingredients)
    

class Application:
    def __init__(self, database):
        self.database = database
        self.dishes = {}

        #if a database does not exist, write a new one
        if not os.path.exists(self.database):
            file_pointer = open(self.database, "wb")
            pickle.dump({}, file_pointer)
            file_pointer.close()

        #if a database does exist, read and load to dishes library
        else:
            with open(self.database, "rb") as dish_list:
                self.dishes = pickle.load(dish_list)
    
    def getDetails(self):
        dishName = input("Dish Name: ")
        prepTime = int(input("Prep Time: "))
        ingredients = input("Dish Ingredients: ")
        return dishName, prepTime, ingredients

    def add(self):
        dishName, prepTime, ingredients = self.getDetails()
        #uses a dictionary 
        #key: the dish name
        #value: the Dish object containing attributes
        if dishName not in self.dishes:
            self.dishes[dishName] = Dish(dishName, prepTime, ingredients)
        else:
            print("Dish is already in your dish list!")


    def delete(self):
        dishName = input("What dish do you want to delete?: ")
        if dishName in self.dishes: 
            del self.dishes[dishName]
            print("Your dish has been deleted!")
        else: 
            print("The dish you entered is not in your list.")


    def viewDishes(self):
        if self.dishes:
            print("{:<25} {:<20} {:<20}".format("DISH NAME", "PREP TIME",  "INGREDIENTS"))
            for dish in self.dishes.values():
                print(dish)
        else:
            print("You have no dishes in your list.")

    def updateDish(self):
        dishName = input("What dish do you want to update?: ")
        if dishName in self.dishes: 
            print("Enter new details.")
            dishName, prepTime, ingredients = self.getDetails()
            self.dishes[dishName].__init__(dishName, prepTime, ingredients)
            print("Successfully updated!")
        else:
            print("Dish not found.")

    def search(self):
        app = Application2(self.dishes)
        option = " "
        while option != "5":
            print(app)
            option = input("Enter an option from the list above: ")
            if option == "1":
                app.byPrepTime()
            elif option == "2":
                app.byIngredient()
            elif option == "3":
                app.byFirstLetter()
            elif option == "4":
                app.byDishName()
            elif option == "5":
                print("Exiting search...")
            else: 
                print("Try again. You selected an invalid option.")

    def resetAll(self):
        self.dishes = {}
        print("Dishes have been reset!")

    #destructor method: called when all references to the object have been deleted
    def __del__(self):
        with open(self.database, 'wb') as db:
            pickle.dump(self.dishes, db)

    #represents the class object as a string
    def __str__(self):
        return UI

class Application2:
    def __init__(self, dishes):
        self.dishes = dishes

    def byPrepTime(self):
        time = int(input("Return dishes that take __ min or less: "))
        if self.dishes:
            print("{:<25} {:<20} {:<20}".format("DISH NAME", "PREP TIME",  "INGREDIENTS"))
            for dishName in self.dishes:
                prepTime = getattr(self.dishes[dishName], "prepTime")
                if prepTime <= time: 
                    print(self.dishes[dishName])
                else:
                    pass
        else:
            print("You have no dishes in your list.")
    
    def byIngredient(self):
        ingredient_input = input("What ingredient/s do you want your dish to have?: ").replace(" ", "")
        ingredient = ingredient_input.split(",")
        # if self.dishes:
        #     print("{:<25} {:<20} {:<20}".format("DISH NAME", "PREP TIME",  "INGREDIENTS"))
        #     for dishName in self.dishes:
        #         ingredients = getattr(self.dishes[dishName], "ingredients")
        #         ingredientsList = ingredients.split(",")
        #         if ingredient in ingredientsList:
        #             print(self.dishes[dishName])
        #         else:
        #             pass
            
        if self.dishes:
            print("{:<25} {:<20} {:<20}".format("DISH NAME", "PREP TIME",  "INGREDIENTS"))
            for dishName in self.dishes:
                ingredients = getattr(self.dishes[dishName], "ingredients").replace(" ", "")
                #list of each ingredient in a dish
                ingredientsList = ingredients.split(",")
                
                match = 0
                noMatch = 0 

                for i in ingredient: 
                    if i in ingredientsList: 
                        match = match + 1
                    else:
                        noMatch = noMatch + 1
                if match == len(ingredient) and noMatch == 0: 
                    print(self.dishes[dishName])
                else:
                    pass
        else:
            print("You have no dishes in your list.")


    def byFirstLetter(self):
        firstLetterInput = input("What letter do you want to search by?: ")
        if self.dishes:
            print("{:<25} {:<20} {:<20}".format("DISH NAME", "PREP TIME",  "INGREDIENTS"))
            for dishName in self.dishes: 
                word = getattr(self.dishes[dishName], "dishName")
                firstLetter = word[0]
                if firstLetter == firstLetterInput:
                    print(self.dishes[dishName])
                else: 
                    pass
        else: 
            print("You have no dishes in your list.")

    def byDishName(self):
        dishNameInput = input("What dish are you looking for?: ")
        if dishNameInput in self.dishes:
            print(self.dishes[dishNameInput])
        else:
            print("Dish not found.")


    def __str__(self):
        return UI2


def main():
    app = Application("dishes7.data")
    option = " "
    while option != "7":
        print(app)
        option = input("Enter an option from the list above: ")
        if option == "1":
            app.add()
        elif option == "2":
            app.delete()
        elif option == "3":
            app.viewDishes()
        elif option == "4":
            app.updateDish()
        elif option == "5":
            app.search()
        elif option == "6":
            app.resetAll()
        elif option == "7":
            print("Exiting...")
        else: 
            print("Try again. You selected an invalid option.")

if __name__ == "__main__":
    main()