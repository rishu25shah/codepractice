def valid_palindrome(sen):
    sen=sen.split()
    sen="".join(sen)
    sen=sen.replace(",", "")
    sen=sen.replace(":", "")
    sen=sen.lower()
    reverse_sen=sen[::-1]
    if sen==reverse_sen:
        return True
    else:       
        return False
    

def main():
    sen="A man, a plan, a canal: Panama"
    result=valid_palindrome(sen)
    print(result)

if __name__=="__main__":
    main()