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
