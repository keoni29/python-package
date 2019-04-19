try:
    from . import bar
except:
    import bar

def foofunction():
    return bar.barfunction()

if __name__ == "__main__":foofunction()