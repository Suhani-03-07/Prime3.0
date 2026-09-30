color = input("Enter  color for traffic light: ")

match color:
    case "Green" | "green":
        print("GO")
    case "Yellow" | "yellow":
        print("START")
    case "Red" | "red":
        print("STOP")
    case _:
        print("Wrong Color Entered!")            