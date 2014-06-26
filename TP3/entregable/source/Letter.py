class Letter:
    def __init__(self, aString, binaryIn5By5Representation):
        self.stringValue = aString
        self.binary5By5 = binaryIn5By5Representation
        for i in range(0, len(self.binary5By5)):
            if self.binary5By5[i] == 0:
                self.binary5By5[i] = -1

    def reshapeEachBitIntoSquareOf(self, aDimension):
        rowCount = 5
        reshapedBinary = []
        for rowI in range(0, rowCount):
            row = self.ithRow(rowI)
            for dim in range(0, aDimension):
                reshapedRow = []
                for i in range(0, len(row)):
                    reshapedRow.extend(self.vectorOfValueAndLength(row[i], aDimension))
                reshapedBinary.extend(reshapedRow)

        return reshapedBinary

    def vectorOfValueAndLength(self, value, length):
        return [ value for i in range(0,length)]

    def ithRow(self, i):
        offsetI = i*5
        return self.binary5By5[offsetI:offsetI+5]

    def __str__(self):
        return self.stringValue