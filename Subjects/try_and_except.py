def errors(number: int,phrase: str,value: bool):
    try:
        return [1/number,value,phrase]
    except ZeroDivisionError as err:
        return err
    except TypeError:
        return "Wrong type"
    except ValueError:
        return "Wrong Value"

if __name__ == "__main__":
    print(errors(0,2,True))