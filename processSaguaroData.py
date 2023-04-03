import saguaro
import sys
import os


def main():
    if len(sys.argv) < 2:
        print("Usage: %s [input.csv]" % sys.argv[0])
        sys.exit(1)

    inputFileName = sys.argv[1]

    if not os.path.exists(inputFileName):
        print("Input file %s does not exist!" % (inputFileName))
        sys.exit(1)

    srcDir, srcFileName = os.path.split(os.path.abspath(inputFileName))
    print("srcDir %s, srcFileName %s, path separator: %s" %
          (srcDir, srcFileName, os.path.sep))

    outFileName = "symmetryData_" + srcFileName
    outFilePath = srcDir + os.path.sep + outFileName
    print("Outputting symmetry data to %s" % (outFilePath))

    if os.path.exists(outFilePath):
        print(
            "%s already exists. Ok to delete and overwrite? [yes/no]" % outFileName)
        resp = input()
        if resp.lower() != "yes":
            print("Exiting without making changes")
            sys.exit(0)
        os.remove(outFilePath)

    inFile = open(inputFileName, "r")
    outFile = open(outFilePath, "w")

    saguaroMap = {}
    armCount = 0
    totalLength = 0.0
    for line in inFile:
        valid, plotNo, sID, recorder, date, easting, northing, sHeight, armDeg, aHeight, bHeight, cHeight, dHeight, stemDist = parseRow(
            line)
        if not valid:
            continue

        arm = saguaro.SaguaroArm(
            aHeight, bHeight, cHeight, dHeight, stemDist, armDeg, sHeight)
        totalLength += arm.getLength()
        armCount += 1

        sKey = str(plotNo) + ":" + str(sID)
        if sKey in saguaroMap:
            currSaguaro = saguaroMap[sKey]
            currSaguaro.addArm(
                aHeight, bHeight, cHeight, dHeight, stemDist, armDeg)
        else:
            newSaguaro = saguaro.Saguaro(
                plotNo, sID, recorder, date, easting, northing, sHeight)
            newSaguaro.addArm(aHeight, bHeight, cHeight,
                              dHeight, stemDist, armDeg)
            saguaroMap[sKey] = newSaguaro
    inFile.close()

    print("Calculated data for %d arms on %d saguaros. Average arm length: %f" %
          (armCount, len(saguaroMap.keys()), totalLength / float(armCount)))
    outFile.write("Plot_Number,Saguaro_Number,Recorder,Date,Easting,Northing,Saguaro_Height,Number_Of_Arms,Symmetry_Score,Overall_Arm_Vector_Magnitude,Overall_Arm_Vector_Direction\n")
    for key in saguaroMap:
        currSaguaro = saguaroMap[key]
        outFile.write(currSaguaro.getOutputRow() + "\n")
    outFile.close()


PlotIdx = 0
SagIdx = 1
RecorderIdx = 2
DateIdx = 3
EastingIdx = 4
NorthingIdx = 5
SagHeightIdx = 6
ArmDegIdx = 9
AHeightIdx = 10
BHeightIdx = 11
CHeightIdx = 12
DHeightIdx = 13
StemDistIdx = 14
ColsPerLine = 18


def parseRow(line):
    vals = str(line).split(",")
    if len(vals) != ColsPerLine:
        return False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    plotNo, valid = isValidInt(vals[PlotIdx])
    if not valid:
        return False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    sID, valid = isValidInt(vals[SagIdx])
    if not valid:
        return False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    recorder = vals[RecorderIdx]
    date = vals[DateIdx]

    easting, valid = isValidInt(vals[EastingIdx])
    if not valid:
        return False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    northing, valid = isValidInt(vals[NorthingIdx])
    if not valid:
        return False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    sHeight, valid = isValidFloat(vals[SagHeightIdx])
    if not valid:
        return False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    armDeg, valid = isValidFloat(vals[ArmDegIdx])
    if not valid:
        return False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    aHeight, valid = isValidFloat(vals[AHeightIdx])
    if not valid:
        return False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    bHeight, valid = isValidFloat(vals[BHeightIdx])
    if not valid:
        return False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    cHeight, valid = isValidFloat(vals[CHeightIdx])
    if not valid:
        return False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    dHeight, valid = isValidFloat(vals[DHeightIdx])
    if not valid:
        return False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    stemDist, valid = isValidFloat(vals[StemDistIdx])
    if not valid:
        return False, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    return True, plotNo, sID, recorder, date, easting, northing, sHeight, armDeg, aHeight, bHeight, cHeight, dHeight, stemDist


def isValidInt(inputStr):
    retVal = 0
    try:
        retVal = int(inputStr)
        return retVal, True
    except:
        return 0, False


def isValidFloat(inputStr):
    retVal = 0.0
    try:
        retVal = float(inputStr)
        return retVal, True
    except:
        return 0.0, False


if __name__ == '__main__':
    main()
