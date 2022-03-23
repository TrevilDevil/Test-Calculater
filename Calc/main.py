import TMath
while True:
    X = input()
    if X == "Add":
        TMath.Add()
    elif X == "Sub":
        TMath.Sub()
    elif X == "Mult":
        TMath.Mult()
    elif X == "Div":
        TMath.Div()
    elif X == "Round":
        TMath.Round()
    elif X == "Compare":
        TMath.Compare()
    else:
        print("Please use capital letters and input avaliable commands")