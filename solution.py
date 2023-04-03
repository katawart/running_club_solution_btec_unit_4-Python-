mens_record = [9.58, 9.86, 9.87]        #[World, European, British] Men's Records
womens_record = [10.49, 10.73, 10.99]   #[World, European, British] Women's Records

race = []                               #The race to be input

#Validation loop for gender selection
flag = True
while flag:
    gender = input("Please input the gender of racers M(ale) or F(emale)")   #The gender of the race
    gender = gender.lower()
    #If gender M or F set flag to false, confirm selection
    #Otherwise inform user that selection is invalid
    if gender == "m" or gender == "f" or gender == "male" or gender == "female":
        print("You are recording races for", gender)
        flag = False
    else:
        print("The input you selected was not recognised.")

#validation loop for number of racers
flag = True
while flag:
    no_of_racers = int(input("How many racers in race 4 - 8"))                   #Number of racers
    #If number input is greater than or equal 4 and less than or equal 8, confirm number
    #Otherwise inform user selection invalid
    if no_of_racers >= 4 and no_of_racers <= 8:
        print("There are", no_of_racers ,"in the race")
        flag = False
    else:
        print("You have entered an invalid number of runners.")

#Asks for inputs for each runner's time
for i in range (1, no_of_racers + 1):
    print(i)
    racer_time = round(float(input("Type the time for runner in lane: "+str(i))),2) #Racer's time to 2 decimal places
    race.append(racer_time)
    #Checks if record broken
    
    if gender == "m" or gender == "male":
        if racer_time < mens_record[0]:
            print("World record broken")
        elif racer_time < mens_record[1]:
            print("European record broken")
        elif racer_time < mens_record[2]:
            print("British record broken")
        else:
            print("No record broken")
    else:
        if racer_time < womens_record[0]:
            print("World record broken")
        elif racer_time < womens_record[1]:
            print("European record broken")
        elif racer_time < womens_record[2]:
            print("British record broken")
        else:
            print("No record broken")        

print(race)
race.sort(reverse=True)
print(race)


