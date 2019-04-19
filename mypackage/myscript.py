try:
    from . import foo
except:
    import foo

def main():
    print(foo.foofunction())

if __name__ == "__main__":
    main()