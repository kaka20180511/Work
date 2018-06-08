"""
时间：2017/12/20
功能：封装了歩科与和利时驱动器逻辑程序，歩科逻辑程序需要修改
已完成
"""
import sys

"""
开始导入串口驱动相关模块
"""
import serial
import time
import binascii
import xlrd  # 导入模块

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_down_list import Ui_Dialog

import area


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):

        super(Dialog, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('Quicktron快仓')  # 设置窗口名称

        self.dictProvince = area.dictProvince
        self.dictCity = area.dictCity
        self.dictTown = area.dicTown

        self.pushButton_ok.hide()

        self.comboBox_province.clear()  # 清空items
        self.comboBox_province.addItem('请选择')

        for k, v in self.dictProvince.items():
            self.comboBox_province.addItem(v, k)

    @pyqtSlot(int)
    def on_comboBox_province_activated(self, index):

        key = self.comboBox_province.itemData(index)

        self.comboBox_town.clear()  # 清空items
        self.comboBox_city.clear()  # 清空items
        if key:
            # self.lblResult.setText('未选择！')
            self.comboBox_city.addItem('请选择')
            # 初始化
            for k, v in self.dictCity[key].items():
                self.comboBox_city.addItem(v, k)

    @pyqtSlot(int)
    def on_comboBox_city_activated(self, index):

        key = self.comboBox_city.itemData(index)

        self.comboBox_town.clear()  # 清空items
        if key:
            self.comboBox_town.addItem('请选择')
            # 初始化驱动器型号
            for k, v in self.dictTown[key].items():
                self.comboBox_town.addItem(v, k)

    @pyqtSlot(int)
    def on_comboBox_town_activated(self, index):

        self.pushButton_ok.show()

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
    def Hls_Data(self, town_name, province_name):
        if (town_name == "ID1"):
            just_data = "HlsID1data.txt"
            file_write = "ID1RightOrder.xls"
        else:
            if (town_name == "ID2"):
                just_data = "HlsID2data.txt"
                file_write = "ID2RightOrder.xls"
            else:
                if (town_name == "ID4"):
                    just_data = "HlsID4data.txt"
                    file_write = "ID4RightOrder.xls"
                else:
                    just_data = "HlsID5data.txt"
                    file_write = "ID5RightOrder.xls"
        """
        此处之后开始给驱动器发数据和收数据
        """
        # 配置串口
        ser = serial.Serial(
            port=province_name,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=5
        )
        ser.close()
        ser.open()

        """
        将16进制询问命令从表格中读出，转换成ASCII码
        """
        x = 0  # 配置读取命令表的起始行

        def Data_Read():
            data = xlrd.open_workbook(file_write)  # 打开文件
            table = data.sheets()[0]  # 通过索引顺序获取一个工作表
            Rxd = table.cell(x, 1).value  # 获取第2行第2列这个位置的数据
            # print(Rxd)
            a = str(Rxd)
            a_list = []
            for i in a.split():  # 拆分字符串
                a_list.append(binascii.a2b_hex(i))
            return a_list

        Save_Data = open('实时驱动器参数.txt', 'w')
        #########################################
        z = 512
        while (z):

            x = x + 1
            z = z - 1
            # time.sleep(0.5)
            ser.writelines(Data_Read())
            time.sleep(0.00001)
            out = ser.read(7)  # 此处要非常注意，如果字符数判断不对会导致串口延时5秒再重复读取，导致程序很慢
            #############################
            # 实时刷新GUI界面
            QApplication.processEvents()
            # x = x+1
            # z = z-1

            """
            ASCII码转换成16进制数据，读出
            调用BinAscii模块其中的b2a_hex()函数，可把以ASCII编码的文字以十六进制表示：
            """
            # print (binascii.b2a_hex(out))
            team1 = binascii.b2a_hex(out)
            team2 = team1.decode('utf-8')
            # print(team2)
            # team3 = team2[6:10]+"\n"
            team3 = team2[6:10]  # team3=FFFF
            team4 = int(team3, 16)  # 16进制转10进制，此时team4=0x0000FFFF (计算机自动将16位转换为32位)
            """
            下面9行都是过滤负数的方法：
            例如：team4=-1;二进制原码=1000 0001;反码=1111 1110;补码=1111 1111
            十六进制 = FFFF;32768的二进制=1000 0000 0000 0000;
            -1&32768 = 1000 0001 0000 0000 & 1000 0000 0000 0000 = 1000 0000 0000 0000;
            -1二进制后面的8个0是补充的。因为负数二进制原码的最高位是1，所以与32768进行&运算肯定
            等于32768，肯定不等于0。
            """
            # print(team4)
            team6 = team4 & 32768  # 用原码按位与的方法过滤掉正数，留下负数
            # print(team6)
            if team6 != 0:
                team4 = ((~team4) & 0xffff) + 1  # 等于1
                """
                ~team4 = 0xFFFF0000
                (0xFFFF0000)&(0x0000FFFF)=0
                """
                print(team4)
                team4 = team4 * -1
                print(team4)
            team5 = str(team4) + "\n"  # 16进制转10进制
            # print(team2)
            # print(team3)
            Save_Data.write(team5)  # 将按位转换的数据保存
            # Save_Data.close()
            print(team5)
            ############################
            self.progressBar.setValue(x)  # 添加进度条，使进度条实时更新。
        ############################
        Save_Data.close()
        ser.close()
        ##########################################
        # 检查本地驱动器源文件参数个数是否正确
        a = open(just_data)  # 打开本地正确的数据
        line_number = 0
        for b in (a):
            lineb = b.strip("\n")
            line_number = line_number + 1

        print(line_number)
        a.close()
        ##########################################
        #################################
        """
        #比对两个文件内的数据
        """
        a = open(just_data)  # 打开本地正确的数据
        b = open('实时驱动器参数.txt')
        c = open('参数对比文件.txt', 'w')
        row = 0  # 行号
        for linea, lineb in zip(a, b):
            linea = linea.strip('\n')  # 用strip+换行符“\n”进行分片，将数据中换行符去掉
            lineb = lineb.strip('\n')
            print(lineb)  # 验证“实时驱动器参数”读取是否正确

            # 依次取出a和b里面的内容按行先对比，再按列对比。
            row += 1
            formatting = str(row)  # 统一转换成字符串
            
            sequence = hex(row - 1)
            print(sequence)
            (head1, end1) = sequence.split("x", 1)
            sequence_hex = str(end1)


            if not linea == lineb:  # 如果两个文档的第一个字符相等则继续第二个字符进行比较依次次往后推
                just_data_linea = str(linea)  # 统一转换成字符串
                wrong_data_linea = str(lineb)
                # 将数据添加格式保存
                synthetic_data = "序号:" + formatting + "  Fn_" + sequence_hex + "  正确数据:" + just_data_linea + "  错误数据:" + wrong_data_linea + '\n'
                c.write(synthetic_data)
                print(synthetic_data)

                """
                列数据判断，根据需求确定是否需要添加
                """
                col = 0  # 列号赋初值
                for chara, charb in zip(linea, lineb):  # 计算列号
                    col += 1  # 差异数据的列号
                    if not chara == charb:  # 判断两列数据是否吻合
                        # print("差异数据行号是:%d ,差异数据列号是：:%d"%(row,col))
                        # synthetic_data ="序号: "+formatting+" 正确数据: "+just_data_linea+" 错误数据: "+wrong_data_linea+'\n'
                        # print(synthetic_data)
                        # c.write(synthetic_data)
                        break
                        # QApplication.processEvents()

        # QApplication.processEvents()

        a.close()
        b.close()
        c.close()
        #############################################

        with open('参数对比文件.txt', "r") as f:  # 迭代打开TXT文本
            txt = f.read()  # 读取整个文档内容，注意，此方法只适合读MB范围的文件
            if txt == "" and line_number == 512:
                txt = "参数检验通过！"
                self.textEdit.setPlainText(txt)  # 显示读取的文档内容

            if txt != "" and line_number == 512:
                self.textEdit.setPlainText(txt)  # 显示读取的文档内容

            if line_number != 512:
                txt = "本地源文件数据丢失，请检查相应的文件！"
                self.textEdit.setPlainText(txt)  # 显示读取的文档内容
                # self.textEdit.setPlainText(txt)  # 显示读取的文档内容
                # print(txt)

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
    def Bk_Data(self, town_name, province_name):
        if (town_name == "ID1"):
            just_data = "BkID1data.txt"
            file_write = "ID1BkRightOrder.xls"
        else:
            if (town_name == "ID2"):
                just_data = "BkID2data.txt"
                file_write = "ID2BkRightOrder.xls"
            else:
                if (town_name == "ID4"):
                    just_data = "BkID4data.txt"
                    file_write = "ID4BkRightOrder.xls"
                else:
                    just_data = "BkID5data.txt"
                    file_write = "ID5BkRightOrder.xls"
        """
        此处之后开始给驱动器发数据和收数据
        """
        # 配置串口
        ser = serial.Serial(
            port=province_name,
            baudrate=38400,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=5
        )
        ser.close()
        ser.open()

        """
        将16进制询问命令从表格中读出，转换成ASCII码
        """
        x = 0  # 配置读取命令表的起始行

        def Data_Read():
            data = xlrd.open_workbook(file_write)  # 打开文件
            table = data.sheets()[0]  # 通过索引顺序获取一个工作表
            Rxd = table.cell(x, 1).value  # 获取第2行第2列这个位置的数据
            # print(Rxd)
            a = str(Rxd)
            a_list = []
            for i in a.split():  # 拆分字符串
                a_list.append(binascii.a2b_hex(i))

            print(a_list)
            return a_list

        Save_Data = open('实时驱动器参数.txt', 'w')
        #########################################
        z = 411
        y = 101
        while (z):

            x = x + 1
            y = y + 1
            z = z - 1
            # time.sleep(0.5)
            ser.writelines(Data_Read())
            # print(str(Data_Read()))
            # time.sleep(0.00001)
            out = ser.read(10)  # 此处要非常注意，如果字符数判断不对会导致串口延时5秒再重复读取，导致程序很慢
            # ser.close()

            #############################
            # 实时刷新GUI界面
            QApplication.processEvents()
            # x = x+1
            # z = z-1

            """
            ASCII码转换成16进制数据，读出
            调用BinAscii模块其中的b2a_hex()函数，可把以ASCII编码的文字以十六进制表示：
            """
            # print (binascii.b2a_hex(out))
            team1 = binascii.b2a_hex(out)
            team2 = team1.decode('utf-8')
            # print(team2)

            """
            #team3 = team2[10:18]  # team3=FFFF
            split_Effective_judgement = str(team2[2:4]) #获取报文有效值判断位
            print(split_Effective_judgement)
            split_0_10 = team2[0:10]
            split_10_12 = team2[10:12]
            split_12_14 = team2[12:14]
            split_14_16 = team2[14:16]
            split_16_18 = team2[16:18]
            team3 = split_0_10 + split_16_18 + split_14_16 + split_12_14 + split_10_12
            """
            split_Effective_judgement = str(team2[2:4])  # 获取报文有效值判断位
            # print(split_Effective_judgement)
            if split_Effective_judgement == "43":  # 如果返回的报文的功能码是43，则四个字节都是有效位；
                split_10_12 = team2[10:12]
                split_12_14 = team2[12:14]
                split_14_16 = team2[14:16]
                split_16_18 = team2[16:18]
                team3 = split_16_18 + split_14_16 + split_12_14 + split_10_12

            if split_Effective_judgement == "4b":  # 如果返回的报文的功能码是4B，则前两个字节都是有效位；
                split_10_12 = team2[10:12]
                split_12_14 = team2[12:14]
                # split_14_16 = team2[14:16]
                # split_16_18 = team2[16:18]
                # team3 = split_16_18 + split_14_16 + split_12_14 + split_10_12
                team3 = split_12_14 + split_10_12

            """
            if split_Effective_judgement == "4b":#如果返回的报文的功能码是4B，则前两个字节都是有效位；
                split_10_12 = team2[10:12]
                split_12_14 = team2[12:14]
                split_14_16 = [00]
                split_16_18 = [00]
                team3 = split_16_18 + split_14_16 + split_12_14 + split_10_12
            """

            if split_Effective_judgement == "4f":  # 如果返回的报文的功能码是4F，则前一个字节是有效位；
                split_10_12 = team2[10:12]
                #  split_12_14 = [00]
                # split_14_16 = [00]
                # split_16_18 = [00]
                # team3 = split_16_18 + split_14_16 + split_12_14 + split_10_12
                team3 = split_10_12

            if split_Effective_judgement == "80":  # 如果返回的报文的功能码是80，则四个字节全部为无效位；
                # split_10_12 = [11]
                # split_12_14 = [00]
                # split_14_16 = [00]
                # split_16_18 = [00]
                # team3 = split_16_18 + split_14_16 + split_12_14 + split_10_12
                team3 = "de0b6b3a763ffff"
                # print(team3)

            team4 = int(team3, 16)  # 16进制转10进制，此时team4=0x0000FFFF (计算机自动将16位转换为32位)
            """
            下面9行都是过滤负数的方法：
            例如：team4=-1;二进制原码=1000 0001;反码=1111 1110;补码=1111 1111
            十六进制 = FFFF;32768的二进制=1000 0000 0000 0000;
            -1&32768 = 1000 0001 0000 0000 & 1000 0000 0000 0000 = 1000 0000 0000 0000;
            -1二进制后面的8个0是补充的。因为负数二进制原码的最高位是1，所以与32768进行&运算肯定
            等于32768，肯定不等于0。
            """
            # print(team3)
            team6 = team4 & 32768  # 用原码按位与的方法过滤掉正数，留下负数
            # print(team6)
            if team6 != 0:
                team4 = ((~team4) & 0xffff) + 1  # 等于1
                """
                ~team4 = 0xFFFF0000
                (0xFFFF0000)&(0x0000FFFF)=0
                """
                # print(team4)
                team4 = team4 * -1
                # print(team4)
            team5 = str(team4) + "\n"  # 16进制转10进制
            # print(team2)
            # print(team3)
            Save_Data.write(team5)  # 将按位转换的数据保存
            # Save_Data.close()
            # print(team5)
            ############################
            self.progressBar.setValue(y)  # 添加进度条，使进度条实时更新。
        ############################
        Save_Data.close()
        ser.close()

        #################################

        ##########################################
        # 检查本地驱动器源文件参数个数是否正确
        a = open(just_data)  # 打开本地正确的数据
        line_number = 0
        for b in (a):
            lineb = b.strip("\n")
            line_number = line_number + 1

        print(line_number)
        a.close()
        ##########################################
        """
        #比对两个文件内的数据
        """
        a = open(just_data)  # 打开本地正确的数据

        b = open('实时驱动器参数.txt')
        c = open('参数对比文件.txt', 'w')
        row = 0  # 行号
        for linea, lineb in zip(a, b):
            linea = linea.strip('\n')  # 用strip+换行符“\n”进行分片，将数据中换行符去掉
            lineb = lineb.strip('\n')
            print(lineb)  # 验证“实时驱动器参数”读取是否正确

            # 依次取出a和b里面的内容按行先对比，再按列对比。
            row += 1
            formatting = str(row)  # 统一转换成字符串
            if not linea == lineb:  # 如果两个文档的第一个字符相等则继续第二个字符进行比较依次次往后推
                just_data_linea = str(linea)  # 统一转换成字符串
                wrong_data_linea = str(lineb)
                # 将数据添加格式保存
                synthetic_data = "序号:" + formatting + "  正确数据:" + just_data_linea + "  错误数据:" + wrong_data_linea + '\n'
                c.write(synthetic_data)
                print(synthetic_data)

                """
                列数据判断，根据需求确定是否需要添加
                """
                col = 0  # 列号赋初值
                for chara, charb in zip(linea, lineb):  # 计算列号
                    col += 1  # 差异数据的列号
                    if not chara == charb:  # 判断两列数据是否吻合
                        # print("差异数据行号是:%d ,差异数据列号是：:%d"%(row,col))
                        # synthetic_data ="序号: "+formatting+" 正确数据: "+just_data_linea+" 错误数据: "+wrong_data_linea+'\n'
                        # print(synthetic_data)
                        # c.write(synthetic_data)
                        break
                        # QApplication.processEvents()

        # QApplication.processEvents()

        a.close()
        b.close()
        c.close()
        #############################################

        with open('参数对比文件.txt', "r") as f:  # 迭代打开TXT文本
            txt = f.read()  # 读取整个文档内容，注意，此方法只适合读MB范围的文件
            if txt == "" and line_number == 411:
                txt = "参数检验通过！"
                self.textEdit.setPlainText(txt)  # 显示读取的文档内容

            if txt != "" and line_number == 411:
                self.textEdit.setPlainText(txt)  # 显示读取的文档内容

            if line_number != 411:
                txt = "本地源文件数据丢失，请检查相应的文件！"
                self.textEdit.setPlainText(txt)  # 显示读取的文档内容
                # self.textEdit.setPlainText(txt)  # 显示读取的文档内容
                # print(txt)

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////#


    @pyqtSlot()
    def on_pushButton_ok_clicked(self):
        self.textEdit.setPlainText("正在读取数据，请稍等。。。")  # 显示读取的文档内容
        # 取当前索引
        province_index = self.comboBox_province.currentIndex()
        city_index = self.comboBox_city.currentIndex()
        town_index = self.comboBox_town.currentIndex()
        #
        province_name = self.comboBox_province.itemText(province_index)
        city_name = self.comboBox_city.itemText(city_index)
        town_name = self.comboBox_town.itemText(town_index)
        # 显示结果
        self.lblResult.setText('{}-{}-{}'.format(province_name, city_name, town_name))
        ##############################################################
        # print(province_name)
        # print(city_name)
        print(town_name)

        print(province_name)

        if (city_name == "和利时"):
            self.Hls_Data(town_name, province_name)  # 注意此处参数不要加self

        if (city_name == "歩科"):
            self.Bk_Data(town_name, province_name)


if __name__ == '__main__':
    #   import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
    
