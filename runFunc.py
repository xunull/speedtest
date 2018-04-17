import os


def runTest(cmd, language):
    os.chdir('./codes')
    result = os.popen(cmd).read()
    print(language)
    print(result)
