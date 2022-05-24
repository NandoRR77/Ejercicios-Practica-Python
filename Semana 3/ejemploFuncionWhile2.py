def main():
    print("Alcancia principal")
    
    objetivo = float(input("Cuánto desea ahorrar?: "))
    
    ahorrado = 0.0
    while objetivo >= ahorrado:
        ahorrado += float(input("Cuánto va a depositar?: "))
    
    print(f"Ha alcanzado el objetivo esperado ahorrando ${ahorrado}, le sobran ${ahorrado - objetivo}")
        
if __name__ == "__main__":
    main()
