a=input("Vvedite den nedeli chtobi uznat raspisanie ")

if a in ["Ponedelnik","ponedelnik","Понедельник","понедельник"]:
    print("Segodnja: Matematika 1-2 urok, Fizika 3-4, Programmirovanie 5")
elif a in ["Vtornik","vtornik","Вторник","вторник"]:
    print("Segodnja: Angliskiy 2-3 urok, Himija 4, Russkiy 5")
elif a in ["Sreda","sreda","Среда","среда"]:
    print("Segodnja: Geograafia 1 urok, Literatura 2-3, Fizkultura 4-5")
elif a in ["Chetverg","chetverg","Четверг","четверг"]:
    print("Segodnja: Geograafia 1 urok, Literatura 2-3, Fizkultura 4-5")
elif a in ["","chetverg","Четверг","четверг"]:
    print("Segodnja: Geograafia 1 urok, Literatura 2-3, Fizkultura 4-5")
elif a in "Chetverg" or "chetverg" or "Четверг" or "четверг":
    print("Segodnja: Geograafia 1 urok, Literatura 2-3, Fizkultura 4-5")
elif a in ["Chetverg","chetverg","Четверг","четверг"]:
    print("Segodnja: Geograafia 1 urok, Literatura 2-3, Fizkultura 4-5")

