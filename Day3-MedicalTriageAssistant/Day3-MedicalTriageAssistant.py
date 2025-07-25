print("🩺 Welcome to the Medical Triage Assistant 🩺")
print("Please answer the following questions to assess your condition.")
age = int(input("What is your age? "))
fever = input("Do you have a fever? (yes/no): ").lower()
cough = input("Do you have a cough? (yes/no): ").lower()
shortness_of_breath = input("Do you have shortness of breath? (yes/no): ").lower()
chest_pain = input("Have you experienced chest pain? (yes/no): ").lower()
exposure = input("Have you travelled recently or had contact with a sick person? (yes/no): ").lower()


print("Analyzing your responses...")
print("====================")
print("Triage Result: ")

#Emergency conditions
if chest_pain == "yes" or  shortness_of_breath == "yes":
    print("Recommendation: Go to emergency room immediately.")
    print("Reason: Serious symptoms detected(chest pain or difficultry breathing).")

#High risk age + symptoms
elif (age < 1 or age > 65) and fever == "yes" and cough == "yes": 
    print("Recommendation: Go to emergency room immediately.")
    print("Reason: High-risk age with fever and cough.")

#Moderate symptoms + exposure
elif fever == "yes" and cough == "yes" and exposure == "yes":
    print("Recommendation: Visit a clinic within 24 hours. ")
    print("Reason: You have symptoms and possible exposure risk.")

#Mild symptoms only
elif fever == "yes" or cough == "yes": 
    print("You can monitor your symptoms at home for now.")
    print("Please rest, stay hydrated and avoid close contact with others.")
    print("Seek medical care if you notice any of the following: ")
    print("Persistent high fever")
    print("Worsening cough or difficulty breathhing")
    print("Chest pain")
    print("Confusion or severe fatigue")
    print("Blue lips or face")

#No symptoms
else: 
    print("No concerning symptoms detected.")
    print("You can monitor at home. Stay saf and take precautions.")

print("====================")