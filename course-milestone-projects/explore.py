def main():
    try:
        nums=['1',2,3,4,5]
        for num in nums:
            print(num**2)
    except TypeError as e:
        print("Error: " + str(e))
    finally:
        print("Finally block executed")
        
if __name__ == "__main__":
    main()
