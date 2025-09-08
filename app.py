import sys

def f_to_c(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9

def main():
    if len(sys.argv) != 2:
        print("Usage: python app.py <temperature_in_Fahrenheit>")
        sys.exit(1)
    try:
        f = float(sys.argv[1])
    except ValueError:
        print("Error: please provide a valid number.")
        sys.exit(1)
    c = f_to_c(f)
    print(f"{f}°F = {c:.2f}°C")

if __name__ == "__main__": 
    main()
    import time
    while True:
        time.sleep(60)

#aaaaaaaaSteste