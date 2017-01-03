import collections,sys,hashlib

class Processor:
    charactersArray = []
    codeCharactersArray = []

    exception = False

    def __init__(self, key, message):
        self.key = key
        self.message = message

    def repeatable_random(self, seed):
        hash = seed
        while True:
            try:
                hash = hashlib.md5(hash).digest()
            except Exception:
                hash = hashlib.md5(hash.encode('utf8')).digest()
            for c in hash:
                yield c

    def charIndexArray(self, length):
        resultArray = []
        for i in self.repeatable_random(self.key):
            if i < length and i not in resultArray:
                resultArray.append(i)
                if len(resultArray) == length:
                    return resultArray

    def initStartingAlphabet(self, mType):
        # 97 indexes - 0-97
        if mType.lower() == "e1":
            charactersString = r""" !"#$%'()*+,-./0123456789:;<=>&?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]\^_`abcdefghijklmnopqrstuvwxyz{|}~"""
        else:
            charactersString = r""" !"#$%'()*+,-./0123456789:;<=>&?@ABCDEFGHIJ""" + "\t" + "\n" +  """KLMNOPQRSTUVWXYZ[]\^_`abcdefghijklmnopqrstuvwxyz{|}~"""
        for n in self.key:
            for c in range(0,len(self.charactersArray)):
                if n==self.charactersArray[c]:
                    break
                elif c==(len(self.charactersArray) - 1):
                    print("Invalid Key - %s is not a valid character." % (n))
                    self.exception = True
                    return

        resultsArray = self.charIndexArray(len(charactersString))
        for i in resultsArray:
            self.charactersArray.append(charactersString[i])

    def validateKeyRepeat(self):
        d = collections.defaultdict(int)
        for c in self.key:
            d[c] += 1
        repeated = []
        for c in sorted(d, key=d.get, reverse=True):
            if d[c] > 1:
                repeated.append(c)
        if len(repeated) > 0:
            print("Invalid Key - %s were repeated." % (repeated))
            self.exception = True
            return

    def createCodeCharacters(self):
        for n in self.charactersArray:
            self.codeCharactersArray.append(n)
        for n in self.key[::-1]:
            for c in range(0,len(self.codeCharactersArray)):
                if n==self.codeCharactersArray[c]:
                    del self.codeCharactersArray[c]
                    self.codeCharactersArray.insert(0, n)
                    break
        for n in self.message:
            for c in range(0,len(self.charactersArray)):
                if n==self.charactersArray[c]:
                    break
                elif c==(len(self.charactersArray) - 1):
                    print("Invalid Message - %s is not a valid character." % (n))
                    self.exception = True
                    return

    def initGypting(self, mOF):
        self.charactersArray = []
        self.codeCharactersArray = []
        self.validateKeyRepeat()
        self.initStartingAlphabet(mOF)
        self.createCodeCharacters()

    def egyptIt(self, mType, eD):
        self.initGypting(mType)
        if self.exception:
            return "ERROR"
        encodedString = ""
        for n in range(0,len(self.message)):
            if eD == "egyptIt":
                index = self.charactersArray.index(self.message[n])
                encodedString = encodedString + self.codeCharactersArray[index]
            else:
                index = self.codeCharactersArray.index(self.message[n])
                encodedString = encodedString + self.charactersArray[index]
        return encodedString
