def product_except_self(n):
    new =[]
    for i in range(len(n)):
        product=1
        for j in range(len(n)):
            if i != j:
                product*=n[j]

        new.append(product)
    return new
def main():
    n = [1, 2, 3, 4]
    result = product_except_self(n)
    print(result)   

if __name__ == "__main__":  
    main()