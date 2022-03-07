# coding=utf-8
# ############### Version #################
# ############## Ver: V2.16 ################
# #########################################
# V1.37-3 add parameter == "SrNm" to globalVariable = "SrNm"
# V2.1 if pdcaName == "MLB_CFG_APPENED": parameter = "MLB_CFG_APPENED" (for QT0)
# V2.2 Before UOP test, disable START_CONTROLBIT SOF
# V2.3 replace expected “&” .replace("“", "\"").replace("”", "\"")
# V2.4 Add QT2_NED station & if pdcaName == "PMUREG_LDO13_VSEL":globalVariable = "PMUREG_LDO13_VSEL" & INIT_PMUADC_LDO13 & INIT_PMUADC_APPMUX_VLDO13
# V2.8 Fall back to version V2.4 
# V2.9 Update condition remove "()" IMU_MANU_ID & IMU_CHIP_ID
# V2.10 Move Main.csv to Tech folder
# V2.11 Remove if pdcaName == "PMUREG_LDO13_VSEL":globalVariable = "PMUREG_LDO13_VSEL" & INIT_PMUADC_LDO13 & INIT_PMUADC_APPMUX_VLDO13
# V2.12 Update "SA-COIL" condition
# V2.13 Remove OPERATOR expect value
# V2.14 if PDCA_TYPE ~= "" && PDCA_NAME == "" : PDCA_NAME = PARAMETER
# V2.15 Move Main.csv out of Tech folder
# V2.16 Remove PARSE function PARAMETER {{}}, replace "—" to "--", replace function name parse to PARSE


import os
import re
import csv
import sys


class Parser(object):
    def __init__(self, path):
        self.stations = ["QT0", "QT1", "QT2", "TILT1", "SA_QT0", "QT_SPIRIT", "QT2_NED", "QT2_POSTROXER", "QT2REL", "QT1REL",
                         "SA_FCM", "QT1_GRAPECOEX", "QT1_GRAPECOEX_REL", "QT_GATEKEEPER", "QT3", "QT3REL", "QT3GRR",
                         "BCM_COMBO", "SACOIL_DOE", "SACOIL", "SA_MAGNET", "SA_COIL"]
        self.csvSourcePath = os.path.expanduser('~')
        self.csvPath = path
        self.ovlDirPath = self.csvSourcePath + "/Station_Plan"

    @staticmethod
    def renamecsv(inlist, inx):
        k = []
        for i in range(len(inlist)):
            if len(inlist[i][inx]) > 2 and inlist[i][inx][-2:] in ["_" + str(x) for x in range(10)]:
                k.append(inlist[i][inx])
            while inlist[i][inx] in k and inlist[i][inx] != "":
                inlist[i][inx] = inlist[i][inx] + "*"
            k.append(inlist[i][inx])
            if inlist[i][inx].count("*") >= 1:
                inlist[i][inx] = inlist[i][inx][:-inlist[i][inx].count("*")] + "_" + str(inlist[i][inx].count("*"))

        return inlist

    def mainCreate(self, file):
        mainTab = [["Enable", "TEST_ITEM", "Technology", "Production", "Audit", "Loop", "COF", "SOF", "SAC"]]
        titleFlag = {"testName": 1, "Technology": 0, "newTest": "", "newTest1": ""}
        header = file[0]

        for i in range(len(header)):
            if header[i] == "TEST_ITEM":
                titleFlag["testName"] = i
            elif header[i] == "TEST_GROUP":
                titleFlag["Technology"] = i

        for row in file[1:]:
            sof = ""
            sac = ""
            if row[titleFlag["testName"]] != titleFlag["newTest"] or row[titleFlag["Technology"]] != titleFlag["newTest1"]:
                Name = row[titleFlag["testName"]]
                Technology = row[titleFlag["Technology"]].replace(" ", "_").replace("-", "").replace("__", "_")
                titleFlag["newTest"] = Name
                titleFlag["newTest1"] = row[titleFlag["Technology"]]
                # if Name == "START_CONTROLBIT":
                #     sof = 1
                # if Name == "TEST_END" or Name == "END_CONTROLBIT" or Name == "UNIT STANDBY":
                #     sac = 1
                row = [1, Name, Technology, 1, 1, "", "", sof, sac]
                mainTab.append(row)

        return self.renamecsv(mainTab, 1)

    def techCreate(self, file, modulesDir, parsePath):
        title = ["TEST_GROUP", "TEST_ITEM", "FUNCTION", "PARAMETER", "CONDITIONAL_ITEM", "PDCA_TYPE", "PDCA_NAME",
                 "GLOBAL_VARIABLE", "EXPECTED_VALUE", "Upper", "Lower", "Units", "TIMEOUT", "SOE", "SAC"]
        techTab = [title]
        modulesDataTab = [title[1:]]
        parseTitle = ["PARAMETER", "PARSE", "CONDITIONAL_ITEM", "COMMAND"]
        parseName = [parseTitle]

        techFlag = {"group": 0, "TEST_ITEM": 1, "CONDITIONAL_ITEM": 2, "FUNCTION": 4, "PARAMETER": 5, "PDCA_NAME": 6,
                    "PDCA_TYPE": 10,
                    "GLOBAL_VARIABLE": 7, "EXPECTED_VALUE": 8, "units": 9}
        header = file[0]
        for i in range(len(header)):
            if header[i] == "TEST_ITEM":
                techFlag["TEST_ITEM"] = i
            elif header[i] == "FUNCTION":
                techFlag["FUNCTION"] = i
            elif header[i] == "PARAMETER":
                techFlag["PARAMETER"] = i
            elif header[i] == "CONDITIONAL_ITEM":
                techFlag["CONDITIONAL_ITEM"] = i
            elif header[i] == "PDCA_NAME":
                techFlag["PDCA_NAME"] = i
            elif header[i] == "PDCA_TYPE":
                techFlag["PDCA_TYPE"] = i
            elif header[i] == "EXPECTED_VALUE":
                techFlag["EXPECTED_VALUE"] = i
            elif header[i] == "GLOBAL_VARIABLE":
                techFlag["GLOBAL_VARIABLE"] = i
            elif header[i] == "TEST_GROUP":
                techFlag["TEST_GROUP"] = i
            elif header[i] == "UNIT":
                techFlag["UNIT"] = i
            elif header[i] == "TIMEOUT":
                techFlag["TIMEOUT"] = i
            elif header[i] == "DESCRIPTION":
                techFlag["DESCRIPTION"] = i

        preName = ""
        groupName = ""
        modules_name = set()
        for row in file[1:]:
            row[techFlag["TEST_GROUP"]] = row[techFlag["TEST_GROUP"]].replace(" ", "_").replace("-", "").replace("__", "_")
            modules_name.add(row[techFlag["TEST_GROUP"]])
            group = row[techFlag["TEST_GROUP"]]
            item = row[techFlag["TEST_ITEM"]]
            action = row[techFlag["FUNCTION"]]
            parameter = row[techFlag["PARAMETER"]].replace("，", ",").replace("“", "\"").replace("”", "\"")
            # condition = row[techFlag["CONDITIONAL_ITEM"]]
            condition = self.parserCondition(str(row[techFlag["CONDITIONAL_ITEM"]])).strip().replace("|", "||").replace("||||", "||")
            pdcaName = row[techFlag["PDCA_NAME"]]
            pdcaType = row[techFlag["PDCA_TYPE"]]
            globalVariable = row[techFlag["GLOBAL_VARIABLE"]]
            expected = row[techFlag["EXPECTED_VALUE"]].replace("“", "\"").replace("”", "\"")
            units = row[techFlag["UNIT"]]
            upper = ""
            lower = ""
            timeout = row[techFlag["TIMEOUT"]]
            soe = ""
            sac = ""

            if action == "DIAGS" and parameter == "INPUTSN":
                action = "INPUTSN"
            if action == "FIXTURE" and parameter.find("dbgpwroff") != -1:
                action = "SPAM"
            if action == "parse":
                action = "PARSE"

            if condition != "":
                if condition.find("BOOST1_AFSM_2") != -1 and pdcaName.find("boost2") != -1:
                    condition = condition.replace("BOOST1_AFSM_2", "BOOST2_AFSM_1")
                if condition.find("IMU_MANU_ID") != -1 and condition.find("IMU_CHIP_ID") != -1:
                    condition = condition.replace("(", "").replace(")", "")
                if condition.find("(") != -1 and condition.find(")") != -1 and condition.find("SA_EEEE") != -1 and condition.find("N143") != -1:
                    condition = "SA_EEEE==P01J || SA_EEEE==PFGF || SA_EEEE==PFGJ || SA_EEEE==PFGG || SA_EEEE==PFGH || SA_EEEE==MWVX || SA_EEEE==MWVV || SA_EEEE==PXKY || SA_EEEE==PXFW || SA_EEEE==Q7F9 || SA_EEEE==Q8VL|| SA_EEEE==Q8VN && DUT_TYPE==N143"
                if condition.find("(") != -1 and condition.find(")") != -1 and condition.find("SA_EEEE") != -1 and condition.find("N149") != -1:
                    condition = "SA_EEEE==P01J || SA_EEEE==PFGF || SA_EEEE==PFGJ || SA_EEEE==PFGG || SA_EEEE==PFGH || SA_EEEE==MWVX || SA_EEEE==MWVV || SA_EEEE==PXKY || SA_EEEE==PXFW || SA_EEEE==Q7F9 || SA_EEEE==Q8VN && DUT_TYPE==N149"

            if pdcaType == "KEY" and action == "DIAGS":
                pdcaType = ""

            if pdcaName == "IMU_MANU_ID" and condition == "":
                expected = ""

            if pdcaName == "MLB_CFG_APPENED":
                parameter = "MLB_CFG_APPENED"

            if action == "PARSE" and parameter.find("{{") != -1 and parameter.find("}}") != -1:
                parameter = parameter.replace("{", "").replace("}", "")

            if action == "DIAGS" and parameter.find("—") != -1:
                parameter = parameter.replace("—", "--")
            

            # Test plan does not set sn as a global variable
            if parameter == "MLB_SN":
                globalVariable = "MLBSN"
            if parameter == "sn":
                globalVariable = "sn"
            if parameter == "SrNm":
                globalVariable = "SrNm"
            if pdcaName == "PMUREG_LDO13_VSEL":
                globalVariable = "PMUREG_LDO13_VSEL"
            if pdcaName == "INIT_PMUADC_LDO13":
                globalVariable = "INIT_PMUADC_LDO13"
            if pdcaName == "INIT_PMUADC_APPMUX_VLDO13":
                globalVariable = "INIT_PMUADC_APPMUX_VLDO13"

            if expected != "" and expected.find("[") != -1:
                if expected.find(":") != -1:
                    upper = re.findall(r":\s*[-\d.]+", expected)
                    lower = re.findall(r"[-\d.]+\s*:", expected)
                    if upper:
                        upper = upper[0].replace(":", "")
                    else:
                        upper = ""
                    if lower:
                        lower = lower[0].replace(":", "")
                    else:
                        lower = ""
                if expected.find(",") != -1:
                    upper = re.findall(r",\s*[-\d.]+", expected)
                    lower = re.findall(r"[-\d.]+\s*,", expected)
                    if upper:
                        upper = upper[0].replace(",", "")
                    else:
                        upper = ""
                    if lower:
                        lower = lower[0].replace(",", "")
                    else:
                        lower = ""
                expected = ""
            if upper != "" or lower != "" or units != "" or row[techFlag["PDCA_TYPE"]] == "KEY":
                if units == "":
                    units = "NA"
            else:
                units = ""

            if preName == item and groupName == group:
                item = ""
            else:
                preName = item
                groupName = group

            # Add <> to expect value
            if expected != "" and (expected.count("<") == 0 and expected.count("\"") == 0):
                expected = "<" + expected + ">"

            if action == "OPERATOR":
                expected = ""

            # Remove space from limit
            if upper.find(" ") != -1:
                upper = upper.replace(" ", "")

            if lower.find(" ") != -1:
                lower = lower.replace(" ", "")

            if item == "START_CONTROLBIT":
                action = "DRCB_Start"
            elif item == "END_CONTROLBIT":
                action = "DRCB_Finish"

            if pdcaName == "" and pdcaType != "":
                pdcaName = row[techFlag["PARAMETER"]]

            if pdcaName == "":
                pdcaName = row[techFlag["DESCRIPTION"]]

            if pdcaName != "Read Control Bit Information (station specific command)":
                techTab.append([group, item, action, parameter, condition, pdcaType, pdcaName, globalVariable,
                                expected, upper, lower, units, timeout, soe, sac])
                modulesDataTab.append([item, action, parameter, condition, pdcaType, pdcaName, globalVariable,
                                       expected, upper, lower, units, timeout, soe, sac])
            if action == "PARSE" or action == "PARSEHEX" or action == "PARSE&RETRY"  or action == "FAILSTOP":
                parseName.append([parameter, "", condition, ""])

        modulesDataTab = self.renamecsv(modulesDataTab, 0)

        modules_name = list(modules_name)
        for i in modules_name:
            modules_row = [title[1:]]
            for index in range(len(techTab)):
                if i == techTab[index][0]:
                    modules_row.append(modulesDataTab[index])
            modulesPath = modulesDir + i + ".csv"
            with open(modulesPath, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(modules_row)
            with open(parsePath + "/Parse.csv", "w") as f:
                writer = csv.writer(f)
                writer.writerows(parseName)

    def parserCondition(self, condition):
        conditon_item = re.findall(r"([<>=!]+)([\w\s\-\.\/]*)", condition)
        for item in range(len(conditon_item)):
            p = "\"" + conditon_item[item][1].strip() + "\" "
            condition = re.sub(r"[<>=!]+[\w\s\-\.\/]+", conditon_item[item][0] + p, condition, 1)

        return condition

    def parser(self, sta):
        with open(self.csvPath) as f:
            data = csv.reader(f)
            file = list(data)
        title = ["TEST_GROUP", "TEST_ITEM", "CONDITIONAL_ITEM", "DESCRIPTION", "FUNCTION", "PARAMETER",
                "PDCA_NAME", "COMBINEC", "GLOBAL_VARIABLE", "EXPECTED_VALUE", "UNIT", "PDCA_TYPE",
                "TIMEOUT", "ERROR_MSG"]
        if set(file[0][:14]) != set(title):
            print("The Test plan title is malformed")
            return
        if len(sta) > 2 and sta[2] in self.stations and sta[2] in file[0]:
            csvTitle = [sta[2]]
        elif len(sta) > 2 and sta[2] not in self.stations:
            print(sta[2] + "Station name is invalid, Please input ==>" + str(self.stations))
            return
        elif len(sta) > 2 and sta[2] not in file[0]:
            print("The Plan is exclusive the " + sta[2] + " Station")
            return
        else:
            csvTitle = []
            for i in range(len(file[0])):
                if i > 13 and type(file[0][i]) is str and file[0][i] in self.stations:
                    csvTitle.append(file[0][i])

        if not os.path.exists(self.ovlDirPath):
            os.mkdir(self.ovlDirPath, 0o777)

        for i in range(len(csvTitle)):
            stationName = csvTitle[i]
            stationDir1 = self.ovlDirPath + "/" + stationName
            stationDir = stationDir1 + "/Assets"
            modulesDir = stationDir + "/Tech/"
            path1 = stationDir + "/TestPlan"
            path = path1 + "/" + stationName + ".csv"
            mainPath = stationDir + "/Main.csv"
            parsePath = stationDir

            if not os.path.exists(stationDir1):
                os.mkdir(stationDir1, 0o777)
            if not os.path.exists(stationDir):
                os.mkdir(stationDir, 0o777)
            if not os.path.exists(path1):
                os.mkdir(path1, 0o777)
            if not os.path.exists(modulesDir):
                os.mkdir(modulesDir, 0o777)

            singleStation = [["TEST_GROUP", "TEST_ITEM", "CONDITIONAL_ITEM", "DESCRIPTION", "FUNCTION", "PARAMETER",
                              "PDCA_NAME", "COMBINEC", "GLOBAL_VARIABLE", "EXPECTED_VALUE", "UNIT", "PDCA_TYPE",
                              "TIMEOUT", "ERROR_MSG", stationName]]
            techFlag = {}
            header = file[0]
            for v in range(len(header)):
                if header[v] == "TEST_GROUP":
                    techFlag["TEST_GROUP"] = v
                elif header[v] == "TEST_ITEM":
                    techFlag["TEST_ITEM"] = v
                elif header[v] == "CONDITIONAL_ITEM":
                    techFlag["CONDITIONAL_ITEM"] = v
                elif header[v] == "DESCRIPTION":
                    techFlag["DESCRIPTION"] = v
                elif header[v] == "FUNCTION":
                    techFlag["FUNCTION"] = v
                elif header[v] == "PARAMETER":
                    techFlag["PARAMETER"] = v
                elif header[v] == "PDCA_NAME":
                    techFlag["PDCA_NAME"] = v
                elif header[v] == "COMBINEC":
                    techFlag["COMBINEC"] = v
                elif header[v] == "GLOBAL_VARIABLE":
                    techFlag["GLOBAL_VARIABLE"] = v
                elif header[v] == "EXPECTED_VALUE":
                    techFlag["EXPECTED_VALUE"] = v
                elif header[v] == "UNIT":
                    techFlag["UNIT"] = v
                elif header[v] == "PDCA_TYPE":
                    techFlag["PDCA_TYPE"] = v
                elif header[v] == "TIMEOUT":
                    techFlag["TIMEOUT"] = v
                elif header[v] == "ERROR_MSG":
                    techFlag["ERROR_MSG"] = v

            for j in range(len(header)):
                if header[j] == stationName:
                    stationDefault_index = j
                    for _index in range(len(file)):
                        if str(file[_index][stationDefault_index]) == "TRUE":
                            TEST_GROUP = file[_index][techFlag["TEST_GROUP"]]
                            TEST_ITEM = file[_index][techFlag["TEST_ITEM"]]
                            CONDITIONAL_ITEM = file[_index][techFlag["CONDITIONAL_ITEM"]]
                            DESCRIPTION = file[_index][techFlag["DESCRIPTION"]]
                            FUNCTION = file[_index][techFlag["FUNCTION"]]
                            PARAMETER = file[_index][techFlag["PARAMETER"]]
                            PDCA_NAME = file[_index][techFlag["PDCA_NAME"]]
                            COMBINEC = file[_index][techFlag["COMBINEC"]]
                            GLOBAL_VARIABLE = file[_index][techFlag["GLOBAL_VARIABLE"]]
                            EXPECTED_VALUE = file[_index][techFlag["EXPECTED_VALUE"]]
                            UNIT = file[_index][techFlag["UNIT"]]
                            PDCA_TYPE = file[_index][techFlag["PDCA_TYPE"]]
                            TIMEOUT = file[_index][techFlag["TIMEOUT"]]
                            ERROR_MSG = file[_index][techFlag["ERROR_MSG"]]

                            singleStation.append([TEST_GROUP, TEST_ITEM, CONDITIONAL_ITEM, DESCRIPTION, FUNCTION,
                                                  PARAMETER, PDCA_NAME, COMBINEC, GLOBAL_VARIABLE, EXPECTED_VALUE,
                                                  UNIT, PDCA_TYPE, TIMEOUT, ERROR_MSG, file[_index][stationDefault_index]])

            with open(path, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(singleStation)

            with open(mainPath, 'w') as f:
                writer = csv.writer(f)
                writer.writerows(self.mainCreate(singleStation))

            self.techCreate(singleStation, modulesDir, parsePath)

            print("=========================================================================")
            print("================ " + stationName + " Test Plan ================")
            os.system("ls " + path1)
            print("================ " + stationName + " TechCSVs ================")
            os.system("ls " + modulesDir)
            print("=========================================================================\n")


if __name__ == "__main__":
    a = sys.argv
    PLAN = Parser(a[1])
    PLAN.parser(a)
