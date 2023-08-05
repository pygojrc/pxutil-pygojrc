

if __name__ == '__main__':
    import sys
    import subprocess
    argv = sys.argv
    if len(argv) == 1:
        subprocess.run("pip freeze > requrequirement.txt", shell=True)
        subprocess.run("/usr/bin/python3 setup.py sdist bdist_wheel", shell=True)
    elif len(argv) == 2:
        arg2 = argv[2]
        if arg2 == 'build':
            subprocess.run("pip freeze > requrequirement.txt", shell=True)
            subprocess.run("/usr/bin/python3 setup.py sdist bdist_wheel", shell=True)
        elif arg2 == 'upload':
            subprocess.run(
                "twine upload --repository testpypi dist/*", shell=True)
        else:
            print("arg error")
    else:
        print("too many args")